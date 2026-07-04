#!/usr/bin/env python3
"""Offline automatic checks for ontology evaluation results.

This script is intentionally conservative: it reports machine-checkable coverage,
missing items, broken evidence references, and possible hallucinations. It does
not make a final human grading decision.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MAX_VALIDATION_ERRORS = 200


class ValidationError(Exception):
    pass


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_optional_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return load_json(path)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def norm(value: Any) -> str:
    """Normalize ids, English names, snake_case, camelCase, and Chinese terms."""
    if value is None:
        return ""
    text = str(value).strip()
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    text = text.lower()
    return "".join(ch for ch in text if ch.isalnum())


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def local_ref(schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        return {}
    node: Any = schema
    for part in ref[2:].split("/"):
        node = node.get(part, {}) if isinstance(node, dict) else {}
    return node if isinstance(node, dict) else {}


def simple_validate(data: Any, schema: dict[str, Any]) -> list[str]:
    """Small JSON Schema subset validator used when jsonschema is unavailable."""
    errors: list[str] = []

    def add(message: str) -> None:
        if len(errors) < MAX_VALIDATION_ERRORS:
            errors.append(message)

    def check_type(value: Any, expected: Any) -> bool:
        expected_types = expected if isinstance(expected, list) else [expected]
        for item in expected_types:
            if item == "object" and isinstance(value, dict):
                return True
            if item == "array" and isinstance(value, list):
                return True
            if item == "string" and isinstance(value, str):
                return True
            if item == "integer" and isinstance(value, int) and not isinstance(value, bool):
                return True
            if item == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
                return True
            if item == "boolean" and isinstance(value, bool):
                return True
            if item == "null" and value is None:
                return True
        return False

    def visit(value: Any, node: dict[str, Any], path: str) -> None:
        if len(errors) >= MAX_VALIDATION_ERRORS:
            return
        if "$ref" in node:
            node = local_ref(schema, node["$ref"])
        expected_type = node.get("type")
        if expected_type is not None and not check_type(value, expected_type):
            add(f"{path}: expected {expected_type}, got {type(value).__name__}")
            return
        if "enum" in node and value not in node["enum"]:
            add(f"{path}: value {value!r} is not in enum {node['enum']!r}")
        if "const" in node and value != node["const"]:
            add(f"{path}: value {value!r} does not equal const {node['const']!r}")
        if isinstance(value, str):
            min_length = node.get("minLength")
            max_length = node.get("maxLength")
            pattern = node.get("pattern")
            if min_length is not None and len(value) < min_length:
                add(f"{path}: string is shorter than {min_length}")
            if max_length is not None and len(value) > max_length:
                add(f"{path}: string is longer than {max_length}")
            if pattern and not re.search(pattern, value):
                add(f"{path}: string does not match pattern {pattern!r}")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in node and value < node["minimum"]:
                add(f"{path}: number is less than {node['minimum']}")
            if "maximum" in node and value > node["maximum"]:
                add(f"{path}: number is greater than {node['maximum']}")
        if isinstance(value, dict):
            required = node.get("required", [])
            for key in required:
                if key not in value:
                    add(f"{path}: missing required property {key!r}")
            properties = node.get("properties", {})
            if node.get("additionalProperties") is False:
                for key in value:
                    if key not in properties:
                        add(f"{path}: additional property {key!r} is not allowed")
            for key, child in properties.items():
                if key in value:
                    visit(value[key], child, f"{path}.{key}")
        if isinstance(value, list):
            if "minItems" in node and len(value) < node["minItems"]:
                add(f"{path}: array has fewer than {node['minItems']} items")
            if node.get("uniqueItems"):
                seen: set[str] = set()
                for item in value:
                    marker = json.dumps(item, sort_keys=True, ensure_ascii=False)
                    if marker in seen:
                        add(f"{path}: array items are not unique")
                        break
                    seen.add(marker)
            item_schema = node.get("items")
            if isinstance(item_schema, dict):
                for index, item in enumerate(value):
                    visit(item, item_schema, f"{path}[{index}]")

    visit(data, schema, "$")
    if len(errors) >= MAX_VALIDATION_ERRORS:
        errors.append(f"validation stopped after {MAX_VALIDATION_ERRORS} errors")
    return errors


def validate_json(data: Any, schema: dict[str, Any]) -> list[str]:
    """Use jsonschema when installed, otherwise use the local subset validator."""
    try:
        from jsonschema import Draft202012Validator  # type: ignore
    except Exception:
        return simple_validate(data, schema)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    messages = []
    for error in errors[:MAX_VALIDATION_ERRORS]:
        path = "$" + "".join(f"[{p}]" if isinstance(p, int) else f".{p}" for p in error.path)
        messages.append(f"{path}: {error.message}")
    if len(errors) > MAX_VALIDATION_ERRORS:
        messages.append(f"validation stopped after {MAX_VALIDATION_ERRORS} errors")
    return messages


def resolve_artifact_path(raw_path: str, evaluation_dir: Path, root_dir: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    candidates = [evaluation_dir / path, root_dir / path]
    if raw_path.startswith("results/"):
        candidates.append(root_dir / raw_path)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def iter_json_files(evaluation_dir: Path) -> list[Path]:
    files = []
    for path in evaluation_dir.rglob("*.json"):
        if path.name == "machine_score.json":
            continue
        if "scoring" in path.relative_to(evaluation_dir).parts:
            continue
        files.append(path)
    return sorted(files)


def discover_outputs(evaluation_dir: Path, root_dir: Path) -> dict[str, Any]:
    task_results: list[dict[str, Any]] = []
    ontology_paths: set[Path] = set()
    evidence_paths: set[Path] = set()
    json_load_errors: list[dict[str, str]] = []

    loaded: dict[Path, Any] = {}
    for path in iter_json_files(evaluation_dir):
        try:
            data = load_json(path)
        except Exception as exc:
            json_load_errors.append({"path": str(path), "error": str(exc)})
            continue
        loaded[path] = data
        if isinstance(data, dict) and {"task_id", "output_artifacts"}.issubset(data):
            task_results.append({"path": path, "data": data})
            for artifact in data.get("output_artifacts", []):
                if not isinstance(artifact, dict):
                    continue
                artifact_path = artifact.get("path")
                if not artifact_path:
                    continue
                resolved = resolve_artifact_path(artifact_path, evaluation_dir, root_dir)
                if artifact.get("artifact_type") == "ontology":
                    ontology_paths.add(resolved)
                elif artifact.get("artifact_type") == "evidence":
                    evidence_paths.add(resolved)

    for path, data in loaded.items():
        if isinstance(data, dict) and "ontology_id" in data and "concepts" in data:
            ontology_paths.add(path)
        elif looks_like_evidence_output(data):
            evidence_paths.add(path)

    return {
        "task_results": task_results,
        "ontology_paths": sorted(ontology_paths),
        "evidence_paths": sorted(evidence_paths),
        "json_load_errors": json_load_errors,
    }


def looks_like_evidence_output(data: Any) -> bool:
    if isinstance(data, dict) and "evidence_id" in data:
        return True
    if isinstance(data, dict):
        for key in ("evidence", "evidences", "items"):
            if isinstance(data.get(key), list) and any(isinstance(x, dict) and "evidence_id" in x for x in data[key]):
                return True
    if isinstance(data, list) and any(isinstance(x, dict) and "evidence_id" in x for x in data):
        return True
    return False


def extract_evidence_items(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict) and "evidence_id" in data:
        return [data]
    if isinstance(data, dict):
        items: list[dict[str, Any]] = []
        for key in ("evidence", "evidences", "items"):
            if isinstance(data.get(key), list):
                items.extend(x for x in data[key] if isinstance(x, dict) and "evidence_id" in x)
        return items
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict) and "evidence_id" in x]
    return []


def build_gold_index(gold: dict[str, Any], aliases: dict[str, Any]) -> dict[str, Any]:
    concepts = {c["id"]: c for c in gold.get("concepts", []) if isinstance(c, dict) and c.get("id")}
    attributes: dict[str, dict[str, Any]] = {}
    attrs_by_concept_and_name: dict[tuple[str, str], str] = {}
    relations = {r["id"]: r for r in gold.get("relations", []) if isinstance(r, dict) and r.get("id")}

    alias_to_ids: dict[str, set[str]] = defaultdict(set)

    def add_alias(canonical_id: str, value: Any) -> None:
        key = norm(value)
        if key:
            alias_to_ids[key].add(canonical_id)

    for concept_id, concept in concepts.items():
        add_alias(concept_id, concept_id)
        add_alias(concept_id, concept.get("name"))
        for alias in concept.get("aliases", []):
            add_alias(concept_id, alias)
        for attr in concept.get("attributes", []):
            if not isinstance(attr, dict) or not attr.get("id"):
                continue
            attr = dict(attr)
            attr["concept_id"] = concept_id
            attributes[attr["id"]] = attr
            add_alias(attr["id"], attr["id"])
            add_alias(attr["id"], attr.get("name"))
            add_alias(attr["id"], f"{concept.get('name')} {attr.get('name')}")
            attrs_by_concept_and_name[(concept_id, norm(attr.get("name")))] = attr["id"]

    for relation_id, relation in relations.items():
        add_alias(relation_id, relation_id)
        add_alias(relation_id, relation.get("name"))
        add_alias(relation_id, relation.get("predicate"))
        add_alias(relation_id, relation_id.replace("rel:", ""))

    for item in aliases.get("aliases", []):
        if not isinstance(item, dict):
            continue
        canonical_id = item.get("canonical_id")
        if not canonical_id:
            continue
        add_alias(canonical_id, item.get("alias"))
        add_alias(canonical_id, item.get("canonical_name"))

    return {
        "concepts": concepts,
        "attributes": attributes,
        "relations": relations,
        "alias_to_ids": alias_to_ids,
        "attrs_by_concept_and_name": attrs_by_concept_and_name,
        "core_concepts": set(gold.get("core_required_concept_ids", [])),
    }


def unique_match(alias_to_ids: dict[str, set[str]], value: Any, prefix: str) -> str | None:
    ids = {item for item in alias_to_ids.get(norm(value), set()) if item.startswith(prefix)}
    return next(iter(ids)) if len(ids) == 1 else None


def all_matches(alias_to_ids: dict[str, set[str]], value: Any, prefix: str) -> set[str]:
    return {item for item in alias_to_ids.get(norm(value), set()) if item.startswith(prefix)}


def match_concept(concept: dict[str, Any], gold_index: dict[str, Any]) -> str | None:
    aliases = gold_index["alias_to_ids"]
    candidates: list[Any] = [concept.get("id"), concept.get("name")]
    for alias in as_list(concept.get("aliases")):
        if isinstance(alias, dict):
            candidates.extend([alias.get("alias"), alias.get("name")])
        else:
            candidates.append(alias)
    for value in candidates:
        matched = unique_match(aliases, value, "concept:")
        if matched:
            return matched
    return None


def extract_output_concepts(ontology: dict[str, Any]) -> list[dict[str, Any]]:
    return [c for c in ontology.get("concepts", []) if isinstance(c, dict)]


def extract_output_attributes(ontology: dict[str, Any], concept_matches: dict[str, str]) -> list[dict[str, Any]]:
    attributes = [dict(a) for a in ontology.get("attributes", []) if isinstance(a, dict)]
    for concept in extract_output_concepts(ontology):
        parent_id = concept.get("id") or concept.get("name")
        parent_canonical = concept_matches.get(str(parent_id)) if parent_id is not None else None
        for attr in concept.get("attributes", []):
            if isinstance(attr, dict):
                nested = dict(attr)
                nested.setdefault("concept_id", parent_id)
                nested["_parent_canonical_concept_id"] = parent_canonical
                attributes.append(nested)
            elif isinstance(attr, str):
                attributes.append({"id": f"nested:{parent_id}.{attr}", "name": attr, "concept_id": parent_id, "_parent_canonical_concept_id": parent_canonical})
        for attr_id in concept.get("attribute_ids", []):
            attributes.append({"id": attr_id, "name": str(attr_id).split(".")[-1], "concept_id": parent_id, "_parent_canonical_concept_id": parent_canonical})
    return attributes


def match_attribute(attribute: dict[str, Any], gold_index: dict[str, Any], concept_id_matches: dict[str, str]) -> str | None:
    aliases = gold_index["alias_to_ids"]
    candidates = [attribute.get("id"), attribute.get("name")]
    for value in candidates:
        matched = unique_match(aliases, value, "attr:")
        if matched:
            return matched

    parent = attribute.get("_parent_canonical_concept_id")
    raw_concept_id = attribute.get("concept_id")
    if not parent and raw_concept_id is not None:
        parent = concept_id_matches.get(str(raw_concept_id))
        if not parent:
            parent = unique_match(aliases, raw_concept_id, "concept:")
    if parent:
        attr_name = norm(attribute.get("name") or str(attribute.get("id", "")).split(".")[-1])
        matched = gold_index["attrs_by_concept_and_name"].get((parent, attr_name))
        if matched:
            return matched
    return None


def extract_output_relations(ontology: dict[str, Any], concept_matches: dict[str, str]) -> list[dict[str, Any]]:
    relations = [dict(r) for r in ontology.get("relations", []) if isinstance(r, dict)]
    for concept in extract_output_concepts(ontology):
        parent_id = concept.get("id") or concept.get("name")
        parent_canonical = concept_matches.get(str(parent_id)) if parent_id is not None else None
        for rel in concept.get("relations", []):
            if isinstance(rel, dict):
                nested = dict(rel)
                nested.setdefault("source_concept_id", parent_id)
                nested["_parent_canonical_concept_id"] = parent_canonical
                relations.append(nested)
    return relations


def relation_endpoints(relation: dict[str, Any], gold_index: dict[str, Any], concept_id_matches: dict[str, str]) -> tuple[str | None, str | None]:
    aliases = gold_index["alias_to_ids"]

    def concept_value(*keys: str) -> str | None:
        for key in keys:
            value = relation.get(key)
            if value is None:
                continue
            raw = str(value)
            if raw in concept_id_matches:
                return concept_id_matches[raw]
            matched = unique_match(aliases, raw, "concept:")
            if matched:
                return matched
        return None

    source = relation.get("_parent_canonical_concept_id") or concept_value("source_concept_id", "source_id", "source", "from")
    target = concept_value("target_concept_id", "target_id", "target", "to")
    return source, target


def match_relation(relation: dict[str, Any], gold_index: dict[str, Any], concept_id_matches: dict[str, str]) -> str | None:
    aliases = gold_index["alias_to_ids"]
    gold_relations = gold_index["relations"]
    source, target = relation_endpoints(relation, gold_index, concept_id_matches)
    values = [relation.get("id"), relation.get("predicate"), relation.get("name")]

    candidates: set[str] = set()
    for value in values:
        candidates.update(all_matches(aliases, value, "rel:"))
    if candidates:
        endpoint_matches = [rid for rid in candidates if relation_matches_endpoints(gold_relations[rid], source, target)]
        if len(endpoint_matches) == 1:
            return endpoint_matches[0]
        if len(candidates) == 1:
            return next(iter(candidates))

    endpoint_only = [rid for rid, rel in gold_relations.items() if relation_matches_endpoints(rel, source, target)]
    if len(endpoint_only) == 1:
        return endpoint_only[0]
    return None


def relation_matches_endpoints(gold_relation: dict[str, Any], source: str | None, target: str | None) -> bool:
    if source and gold_relation.get("source_concept_id") != source:
        return False
    if target and gold_relation.get("target_concept_id") != target:
        return False
    return bool(source or target)


def collect_element_evidence_refs(ontology: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(element_type: str, element_id: Any, item: dict[str, Any]) -> None:
        for ref in item.get("evidence_refs", []) or []:
            rows.append({"element_type": element_type, "element_id": str(element_id or "<unknown>"), "evidence_ref": str(ref)})

    add("ontology", ontology.get("ontology_id"), ontology)
    for key, element_type in (
        ("concepts", "concept"),
        ("attributes", "attribute"),
        ("relations", "relation"),
        ("events", "event"),
        ("rules", "rule"),
        ("actions", "action"),
        ("states", "state"),
        ("roles", "role"),
        ("permissions", "permission"),
        ("aliases", "alias"),
        ("mappings", "mapping"),
        ("conflicts", "conflict"),
        ("uncertainties", "uncertainty"),
    ):
        for item in ontology.get(key, []) or []:
            if isinstance(item, dict):
                add(element_type, item.get("id") or item.get("name"), item)
                for nested_key in ("attributes", "relations"):
                    for nested in item.get(nested_key, []) or []:
                        if isinstance(nested, dict):
                            add(nested_key[:-1], nested.get("id") or nested.get("name"), nested)
    return rows


def build_available_evidence_refs(evaluation_dir: Path, dataset_dir: Path, evidence_items: list[dict[str, Any]], task_results: list[dict[str, Any]]) -> set[str]:
    available: set[str] = set()
    for item in evidence_items:
        evidence_id = item.get("evidence_id")
        if evidence_id:
            available.add(str(evidence_id))
        for field in ("locator", "content_ref", "source_file", "source_location"):
            if item.get(field):
                available.add(str(item[field]))
    for task in task_results:
        for ref in task["data"].get("evidence_refs", []) or []:
            available.add(str(ref))

    manifest_path = dataset_dir / "metadata" / "dataset_manifest.json"
    if manifest_path.exists():
        try:
            manifest = load_json(manifest_path)
            for artifact in manifest.get("artifacts", []):
                if not isinstance(artifact, dict) or not artifact.get("path"):
                    continue
                path = str(artifact["path"])
                p = Path(path)
                available.update({path, p.name, p.stem})
                art_type = artifact.get("type")
                if art_type == "source_code":
                    available.add(f"code:{p.stem}")
                elif art_type == "sample_data_csv":
                    available.add(f"csv:{p.stem}")
                elif art_type == "business_document":
                    available.add(f"doc:{p.stem}")
        except Exception:
            pass

    ddl_path = dataset_dir / "database" / "ddl.sql"
    if ddl_path.exists():
        text = ddl_path.read_text(encoding="utf-8")
        for table in re.findall(r"create\s+table\s+([A-Za-z0-9_]+)", text, flags=re.IGNORECASE):
            available.add(f"ddl:{table}")
        for table, column in re.findall(r"\b(pc_[A-Za-z0-9_]+)\b[^;]*?\b([A-Za-z_][A-Za-z0-9_]*)\b", text, flags=re.IGNORECASE | re.DOTALL):
            available.add(f"ddl:{table}.{column}")

    for base in (evaluation_dir, dataset_dir):
        if base.exists():
            for path in base.rglob("*"):
                if path.is_file():
                    rel = str(path.relative_to(base))
                    available.update({rel, path.name, path.stem})
    return available


def evidence_ref_exists(ref: str, available: set[str], evaluation_dir: Path, dataset_dir: Path) -> bool:
    if ref in available or norm(ref) in {norm(x) for x in available}:
        return True
    raw_path = Path(ref)
    if raw_path.is_absolute() and raw_path.exists():
        return True
    return (evaluation_dir / raw_path).exists() or (dataset_dir / raw_path).exists()


def extract_screenshot_gold_items(data: Any | None) -> list[dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    return [item for item in data.get("evidence", []) if isinstance(item, dict) and item.get("evidence_id")]


def extract_web_gold_items(data: Any | None) -> list[dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    return [item for item in data.get("evidence", []) if isinstance(item, dict) and item.get("evidence_id")]


def build_screenshot_evidence_summary(screenshot_items: list[dict[str, Any]], evidence_rows: list[dict[str, str]], dataset_dir: Path) -> dict[str, Any]:
    screenshot_ids = {str(item.get("evidence_id")) for item in screenshot_items if item.get("evidence_id")}
    referenced = sorted({row["evidence_ref"] for row in evidence_rows if row["evidence_ref"].startswith("screen:")})
    missing_refs = [ref for ref in referenced if ref not in screenshot_ids]
    invalid_source_files = sorted({
        str(item.get("source_file"))
        for item in screenshot_items
        if item.get("source_file") and not (dataset_dir / str(item["source_file"])).exists()
    })
    return {
        "enabled": bool(screenshot_items),
        "gold_screenshot_evidence_count": len(screenshot_items),
        "referenced_screenshot_evidence_count": len(referenced),
        "matched_screenshot_evidence_count": len([ref for ref in referenced if ref in screenshot_ids]),
        "missing_screenshot_evidence_refs": missing_refs,
        "invalid_screenshot_source_files": invalid_source_files,
        "input_mode": "surrogate_only" if screenshot_items else None,
        "note": "Screenshot evidence checks are optional and do not change MVP gold ontology coverage.",
    }


def build_web_evidence_summary(web_items: list[dict[str, Any]], evidence_rows: list[dict[str, str]], dataset_dir: Path) -> dict[str, Any]:
    web_ids = {str(item.get("evidence_id")) for item in web_items if item.get("evidence_id")}
    referenced = sorted({row["evidence_ref"] for row in evidence_rows if row["evidence_ref"].startswith("web:")})
    missing_refs = [ref for ref in referenced if ref not in web_ids]

    invalid_paths: set[str] = set()
    page_map_files: set[str] = set()
    input_modes: set[str] = set()
    for item in web_items:
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        if metadata.get("input_mode"):
            input_modes.add(str(metadata["input_mode"]))
        content_ref = item.get("content_ref")
        if content_ref:
            content_ref_str = str(content_ref)
            if content_ref_str.startswith("web_map/"):
                page_map_files.add(content_ref_str)
            if not (dataset_dir / content_ref_str).exists():
                invalid_paths.add(content_ref_str)

    return {
        "enabled": bool(web_items),
        "gold_web_evidence_count": len(web_items),
        "referenced_web_evidence_count": len(referenced),
        "matched_web_evidence_count": len([ref for ref in referenced if ref in web_ids]),
        "missing_web_evidence_refs": missing_refs,
        "invalid_web_snapshot_paths": sorted(invalid_paths),
        "page_map_file_count": len(page_map_files),
        "input_mode": sorted(input_modes)[0] if input_modes else ("html_snapshot" if web_items else None),
        "note": "Web evidence checks are optional and do not change MVP gold ontology coverage.",
    }


def compare_ontology(ontology: dict[str, Any], gold_index: dict[str, Any]) -> dict[str, Any]:
    output_concepts = extract_output_concepts(ontology)
    concept_matches_by_raw_id: dict[str, str] = {}
    matched_concepts: dict[str, dict[str, Any]] = {}
    hallucinated_concepts: list[dict[str, str]] = []

    for concept in output_concepts:
        canonical = match_concept(concept, gold_index)
        raw_key = str(concept.get("id") or concept.get("name") or "<unknown>")
        if canonical:
            concept_matches_by_raw_id[raw_key] = canonical
            if concept.get("id"):
                concept_matches_by_raw_id[str(concept["id"])] = canonical
            if concept.get("name"):
                concept_matches_by_raw_id[str(concept["name"])] = canonical
            matched_concepts[canonical] = {"output_id": str(concept.get("id", "")), "output_name": str(concept.get("name", ""))}
        else:
            hallucinated_concepts.append({"id": str(concept.get("id", "")), "name": str(concept.get("name", ""))})

    attributes = extract_output_attributes(ontology, concept_matches_by_raw_id)
    matched_attributes: dict[str, dict[str, Any]] = {}
    hallucinated_attributes: list[dict[str, str]] = []
    for attribute in attributes:
        canonical = match_attribute(attribute, gold_index, concept_matches_by_raw_id)
        if canonical:
            matched_attributes[canonical] = {"output_id": str(attribute.get("id", "")), "output_name": str(attribute.get("name", ""))}
        else:
            hallucinated_attributes.append({"id": str(attribute.get("id", "")), "name": str(attribute.get("name", "")), "concept_id": str(attribute.get("concept_id", ""))})

    relations = extract_output_relations(ontology, concept_matches_by_raw_id)
    matched_relations: dict[str, dict[str, Any]] = {}
    hallucinated_relations: list[dict[str, str]] = []
    for relation in relations:
        canonical = match_relation(relation, gold_index, concept_matches_by_raw_id)
        if canonical:
            matched_relations[canonical] = {"output_id": str(relation.get("id", "")), "output_predicate": str(relation.get("predicate") or relation.get("name") or "")}
        else:
            hallucinated_relations.append({
                "id": str(relation.get("id", "")),
                "predicate": str(relation.get("predicate") or relation.get("name") or ""),
                "source_concept_id": str(relation.get("source_concept_id", "")),
                "target_concept_id": str(relation.get("target_concept_id", "")),
            })

    core_concepts = gold_index["core_concepts"] or set(gold_index["concepts"])
    required_attributes = {
        attr_id for attr_id, attr in gold_index["attributes"].items()
        if attr.get("required") is True and attr.get("concept_id") in core_concepts
    }
    key_relations = set(gold_index["relations"])

    return {
        "matched_concepts": matched_concepts,
        "matched_attributes": matched_attributes,
        "matched_relations": matched_relations,
        "missing_core_concepts": sorted(core_concepts - set(matched_concepts)),
        "missing_key_attributes": sorted(required_attributes - set(matched_attributes)),
        "missing_key_relations": sorted(key_relations - set(matched_relations)),
        "possible_hallucinations": {
            "concepts": hallucinated_concepts,
            "attributes": hallucinated_attributes,
            "relations": hallucinated_relations,
        },
        "counts": {
            "output_concepts": len(output_concepts),
            "output_attributes": len(attributes),
            "output_relations": len(relations),
            "matched_core_concepts": len(set(matched_concepts) & core_concepts),
            "total_core_concepts": len(core_concepts),
            "matched_key_attributes": len(set(matched_attributes) & required_attributes),
            "total_key_attributes": len(required_attributes),
            "matched_key_relations": len(set(matched_relations) & key_relations),
            "total_key_relations": len(key_relations),
        },
    }


def ratio(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def merge_comparisons(comparisons: list[dict[str, Any]], gold_index: dict[str, Any]) -> dict[str, Any]:
    matched_concepts: dict[str, Any] = {}
    matched_attributes: dict[str, Any] = {}
    matched_relations: dict[str, Any] = {}
    hallucinations = {"concepts": [], "attributes": [], "relations": []}
    output_counts = {"output_concepts": 0, "output_attributes": 0, "output_relations": 0}

    for comp in comparisons:
        matched_concepts.update(comp["matched_concepts"])
        matched_attributes.update(comp["matched_attributes"])
        matched_relations.update(comp["matched_relations"])
        for key in hallucinations:
            hallucinations[key].extend(comp["possible_hallucinations"][key])
        for key in output_counts:
            output_counts[key] += comp["counts"][key]

    core_concepts = gold_index["core_concepts"] or set(gold_index["concepts"])
    required_attributes = {
        attr_id for attr_id, attr in gold_index["attributes"].items()
        if attr.get("required") is True and attr.get("concept_id") in core_concepts
    }
    key_relations = set(gold_index["relations"])

    counts = {
        **output_counts,
        "matched_core_concepts": len(set(matched_concepts) & core_concepts),
        "total_core_concepts": len(core_concepts),
        "matched_key_attributes": len(set(matched_attributes) & required_attributes),
        "total_key_attributes": len(required_attributes),
        "matched_key_relations": len(set(matched_relations) & key_relations),
        "total_key_relations": len(key_relations),
    }
    return {
        "matched_concepts": matched_concepts,
        "matched_attributes": matched_attributes,
        "matched_relations": matched_relations,
        "missing_core_concepts": sorted(core_concepts - set(matched_concepts)),
        "missing_key_attributes": sorted(required_attributes - set(matched_attributes)),
        "missing_key_relations": sorted(key_relations - set(matched_relations)),
        "possible_hallucinations": hallucinations,
        "counts": counts,
        "coverage": {
            "core_concept_coverage": ratio(counts["matched_core_concepts"], counts["total_core_concepts"]),
            "key_attribute_coverage": ratio(counts["matched_key_attributes"], counts["total_key_attributes"]),
            "key_relation_coverage": ratio(counts["matched_key_relations"], counts["total_key_relations"]),
        },
    }


def build_markdown(result: dict[str, Any]) -> str:
    summary = result["summary"]
    coverage = result["gold_comparison"]["coverage"]
    missing = result["gold_comparison"]
    hallucinations = result["possible_hallucinations"]
    evidence = result["evidence_check"]

    lines = [
        "# Machine Score",
        "",
        "This report contains automatic, offline checks only. Human review is still required.",
        "",
        "## Summary",
        "",
        f"- Evaluation ID: `{result['evaluation_id']}`",
        f"- Generated at: `{result['generated_at']}`",
        f"- Ontology files checked: {summary['ontology_file_count']}",
        f"- Task result files checked: {summary['task_result_file_count']}",
        f"- Schema-valid ontology files: {summary['valid_ontology_file_count']} / {summary['ontology_file_count']}",
        "",
        "## Coverage",
        "",
        f"- Core concepts: {coverage['core_concept_coverage']:.2%}",
        f"- Key attributes: {coverage['key_attribute_coverage']:.2%}",
        f"- Key relations: {coverage['key_relation_coverage']:.2%}",
        "",
        "## Missing Items",
        "",
        format_list("Missing core concepts", missing["missing_core_concepts"]),
        format_list("Missing key attributes", missing["missing_key_attributes"]),
        format_list("Missing key relations", missing["missing_key_relations"]),
        "",
        "## Evidence References",
        "",
        f"- Evidence references checked: {evidence['referenced_evidence_count']}",
        f"- Missing evidence references: {len(evidence['missing_evidence_refs'])}",
        f"- Screenshot evidence enabled: {evidence.get('screenshot_evidence', {}).get('enabled', False)}",
        f"- Screenshot evidence refs checked: {evidence.get('screenshot_evidence', {}).get('referenced_screenshot_evidence_count', 0)}",
        f"- Missing screenshot evidence refs: {len(evidence.get('screenshot_evidence', {}).get('missing_screenshot_evidence_refs', []))}",
        f"- Web evidence enabled: {evidence.get('web_evidence', {}).get('enabled', False)}",
        f"- Web evidence refs checked: {evidence.get('web_evidence', {}).get('referenced_web_evidence_count', 0)}",
        f"- Missing Web evidence refs: {len(evidence.get('web_evidence', {}).get('missing_web_evidence_refs', []))}",
        f"- Invalid Web snapshot paths: {len(evidence.get('web_evidence', {}).get('invalid_web_snapshot_paths', []))}",
        format_records("Missing evidence reference details", evidence["missing_evidence_refs"], ["element_id", "evidence_ref"]),
        "",
        "## Possible Hallucinations",
        "",
        format_records("Concepts", hallucinations["concepts"], ["id", "name"]),
        format_records("Attributes", hallucinations["attributes"], ["id", "name", "concept_id"]),
        format_records("Relations", hallucinations["relations"], ["id", "predicate", "source_concept_id", "target_concept_id"]),
        "",
        "## Schema Validation",
        "",
    ]
    for item in result["schema_validation"]:
        status = "valid" if item["is_valid"] else "invalid"
        lines.append(f"- `{item['path']}`: {status} ({len(item['errors'])} errors)")
    lines.extend([
        "",
        "## Human Review Fields",
        "",
        "- Human review status: pending",
        "- Human score: not set",
        "- Reviewer notes: not set",
        "",
    ])
    return "\n".join(lines)


def format_list(title: str, items: list[str], limit: int = 25) -> str:
    if not items:
        return f"### {title}\n\nNone.\n"
    lines = [f"### {title}", ""]
    for item in items[:limit]:
        lines.append(f"- `{item}`")
    if len(items) > limit:
        lines.append(f"- ... {len(items) - limit} more")
    return "\n".join(lines) + "\n"


def format_records(title: str, rows: list[dict[str, Any]], fields: list[str], limit: int = 25) -> str:
    if not rows:
        return f"### {title}\n\nNone.\n"
    lines = [f"### {title}", ""]
    for row in rows[:limit]:
        parts = [f"{field}=`{row.get(field, '')}`" for field in fields]
        lines.append("- " + ", ".join(parts))
    if len(rows) > limit:
        lines.append(f"- ... {len(rows) - limit} more")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run offline machine checks for ontology evaluation results.")
    parser.add_argument("evaluation_id", help="Evaluation id under results/ or a direct evaluation directory path.")
    parser.add_argument("--results-dir", default=None, help="Results directory. Defaults to <toolkit>/results.")
    parser.add_argument("--dataset", default="generic_procurement_contract_mvp", help="Dataset id under datasets/.")
    parser.add_argument("--output-dir", default=None, help="Output directory. Defaults to <evaluation>/scoring.")
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parents[1]
    results_dir = Path(args.results_dir).resolve() if args.results_dir else root_dir / "results"
    evaluation_arg = Path(args.evaluation_id)
    evaluation_dir = evaluation_arg.resolve() if evaluation_arg.exists() else results_dir / args.evaluation_id
    dataset_dir = root_dir / "datasets" / args.dataset
    output_dir = Path(args.output_dir).resolve() if args.output_dir else evaluation_dir / "scoring"

    if not evaluation_dir.exists():
        raise SystemExit(f"Evaluation directory not found: {evaluation_dir}")

    schemas_dir = root_dir / "schemas"
    ontology_schema = load_json(schemas_dir / "ontology.schema.json")
    task_result_schema = load_json(schemas_dir / "task_result.schema.json")
    evidence_schema = load_json(schemas_dir / "evidence.schema.json")
    gold = load_json(dataset_dir / "gold" / "gold_ontology.json")
    aliases = load_json(dataset_dir / "gold" / "acceptable_aliases.json")
    screenshot_gold_path = dataset_dir / "gold" / "gold_evidence_map.screenshot.json"
    screenshot_gold = load_optional_json(screenshot_gold_path)
    screenshot_evidence_items = extract_screenshot_gold_items(screenshot_gold)
    web_gold_path = dataset_dir / "gold" / "gold_evidence_map.web.json"
    web_gold = load_optional_json(web_gold_path)
    web_evidence_items = extract_web_gold_items(web_gold)
    gold_index = build_gold_index(gold, aliases)

    discovered = discover_outputs(evaluation_dir, root_dir)
    schema_validation: list[dict[str, Any]] = []

    for task in discovered["task_results"]:
        errors = validate_json(task["data"], task_result_schema)
        schema_validation.append({"path": str(Path(task["path"]).relative_to(evaluation_dir)), "schema": "task_result.schema.json", "is_valid": not errors, "errors": errors})

    ontology_docs: list[dict[str, Any]] = []
    comparisons: list[dict[str, Any]] = []
    evidence_rows: list[dict[str, str]] = []
    for path in discovered["ontology_paths"]:
        try:
            data = load_json(path)
        except Exception as exc:
            schema_validation.append({"path": str(path), "schema": "ontology.schema.json", "is_valid": False, "errors": [str(exc)]})
            continue
        errors = validate_json(data, ontology_schema)
        display_path = str(path.relative_to(evaluation_dir)) if path.is_relative_to(evaluation_dir) else str(path)
        schema_validation.append({"path": display_path, "schema": "ontology.schema.json", "is_valid": not errors, "errors": errors})
        if isinstance(data, dict):
            ontology_docs.append(data)
            comparisons.append(compare_ontology(data, gold_index))
            evidence_rows.extend(collect_element_evidence_refs(data))

    evidence_items: list[dict[str, Any]] = []
    for path in discovered["evidence_paths"]:
        try:
            data = load_json(path)
        except Exception as exc:
            schema_validation.append({"path": str(path), "schema": "evidence.schema.json", "is_valid": False, "errors": [str(exc)]})
            continue
        items = extract_evidence_items(data)
        evidence_items.extend(items)
        if isinstance(data, dict) and "evidence_id" in data:
            errors = validate_json(data, evidence_schema)
            schema_name = "evidence.schema.json"
        else:
            errors = []
            schema_name = "evidence_map"
            for index, item in enumerate(items):
                errors.extend(f"items[{index}]: {err}" for err in validate_json(item, evidence_schema))
        display_path = str(path.relative_to(evaluation_dir)) if path.is_relative_to(evaluation_dir) else str(path)
        schema_validation.append({"path": display_path, "schema": schema_name, "is_valid": not errors, "errors": errors})

    comparison = merge_comparisons(comparisons, gold_index)
    available_refs = build_available_evidence_refs(evaluation_dir, dataset_dir, evidence_items + screenshot_evidence_items + web_evidence_items, discovered["task_results"])
    missing_evidence_refs = [row for row in evidence_rows if not evidence_ref_exists(row["evidence_ref"], available_refs, evaluation_dir, dataset_dir)]
    screenshot_evidence_summary = build_screenshot_evidence_summary(screenshot_evidence_items, evidence_rows, dataset_dir)
    web_evidence_summary = build_web_evidence_summary(web_evidence_items, evidence_rows, dataset_dir)

    valid_ontology_count = sum(1 for row in schema_validation if row["schema"] == "ontology.schema.json" and row["is_valid"])
    result = {
        "schema_version": "1.0.0",
        "evaluation_id": evaluation_dir.name,
        "generated_at": utc_now(),
        "inputs": {
            "evaluation_dir": str(evaluation_dir),
            "dataset_dir": str(dataset_dir),
            "gold_ontology": "gold/gold_ontology.json",
            "acceptable_aliases": "gold/acceptable_aliases.json",
            "gold_screenshot_evidence": "gold/gold_evidence_map.screenshot.json" if screenshot_gold_path.exists() else None,
            "gold_web_evidence": "gold/gold_evidence_map.web.json" if web_gold_path.exists() else None,
        },
        "summary": {
            "task_result_file_count": len(discovered["task_results"]),
            "ontology_file_count": len(discovered["ontology_paths"]),
            "valid_ontology_file_count": valid_ontology_count,
            "evidence_file_count": len(discovered["evidence_paths"]),
            "json_load_error_count": len(discovered["json_load_errors"]),
        },
        "schema_validation": schema_validation,
        "gold_comparison": comparison,
        "evidence_check": {
            "referenced_evidence_count": len(evidence_rows),
            "available_evidence_ref_count": len(available_refs),
            "missing_evidence_refs": missing_evidence_refs,
            "screenshot_evidence": screenshot_evidence_summary,
            "web_evidence": web_evidence_summary,
        },
        "possible_hallucinations": comparison["possible_hallucinations"],
        "machine_metrics": {
            **comparison["coverage"],
            "schema_validity_rate": ratio(valid_ontology_count, len(discovered["ontology_paths"])),
            "missing_evidence_ref_count": len(missing_evidence_refs),
            "missing_screenshot_evidence_ref_count": len(screenshot_evidence_summary["missing_screenshot_evidence_refs"]),
            "referenced_screenshot_evidence_count": screenshot_evidence_summary["referenced_screenshot_evidence_count"],
            "web_evidence_enabled": web_evidence_summary["enabled"],
            "referenced_web_evidence_count": web_evidence_summary["referenced_web_evidence_count"],
            "matched_web_evidence_count": web_evidence_summary["matched_web_evidence_count"],
            "missing_web_evidence_ref_count": len(web_evidence_summary["missing_web_evidence_refs"]),
            "invalid_web_snapshot_path_count": len(web_evidence_summary["invalid_web_snapshot_paths"]),
            "possible_hallucinated_concept_count": len(comparison["possible_hallucinations"]["concepts"]),
            "possible_hallucinated_attribute_count": len(comparison["possible_hallucinations"]["attributes"]),
            "possible_hallucinated_relation_count": len(comparison["possible_hallucinations"]["relations"]),
        },
        "json_load_errors": discovered["json_load_errors"],
        "human_review": {
            "status": "pending",
            "reviewer": None,
            "manual_score": None,
            "manual_decision": None,
            "notes": None,
            "overrides": [],
        },
        "notes": [
            "Machine checks are conservative and alias-based; they do not replace human ontology quality review.",
            "Possible hallucinations are unmatched items, not final false-positive judgments.",
            "Gold/reference paths in inputs are evaluator-side relative identifiers and must not be provided to AI tools under evaluation.",
        ],
    }

    write_json(output_dir / "machine_score.json", result)
    write_text(output_dir / "machine_score.md", build_markdown(result))
    print(f"Wrote {output_dir / 'machine_score.json'}")
    print(f"Wrote {output_dir / 'machine_score.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
