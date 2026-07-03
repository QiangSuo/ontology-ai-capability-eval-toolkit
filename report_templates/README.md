# report_templates

## 用途

`report_templates/` 存放标准评估报告、能力矩阵、人工复核和管理层摘要模板。MVP 阶段的报告目标是把机器检查结果、人工复核结论、工具限制和风险建议合并成可审计的评估结论。

## 输入

- `customer_profile.json`
- `tool_profile.json`
- `task_XX_*_result.json`
- `raw_outputs/`
- `normalized_outputs/`
- `scoring/machine_score.json`
- `scoring/machine_score.md`
- `manual_review/`
- `execution_log.md`

## 输出

Canonical 结构化报告：

```text
results/<evaluation_id>/report/evaluation_report.json
```

可选 Markdown 展示报告：

```text
results/<evaluation_id>/report/final_eval_report.md
```

`evaluation_report.json` 应兼容 `schemas/evaluation_report.schema.json`。`final_eval_report.md` 是展示层，必须与 JSON 报告、人工作业记录和 machine score 一致。

## 最小人工复核模板

建议保存为：

```text
results/<evaluation_id>/manual_review/manual_review.md
```

模板：

```markdown
# Manual Review

Evaluation ID:
Reviewer:
Review date:
Review status: pending | completed | blocked

## Machine Score Disposition

- Schema validation accepted: yes | no | needs_fix
- Concept coverage accepted: yes | no | needs_fix
- Attribute coverage accepted: yes | no | needs_fix
- Relation coverage accepted: yes | no | needs_fix
- Missing evidence refs disposition:
- Possible hallucinations disposition:

## Human Score

- Human score: not set
- Human grade: N/A
- Decision: ready | ready_with_constraints | not_ready | insufficient_data

## Notes

## Required Fixes Before Customer Site

## Sign-off
```

人工复核未完成时，最终报告不得给出无约束 ready 结论。

## evaluation_report.json 模板

以下模板只使用 `evaluation_report.schema.json` 允许的字段。不要把 `machine_score.json` 字段原样塞入未定义字段；应通过 `key_findings`、`risks`、`redline_results`、`score_caps`、`capability_results` 和 `recommendations` 表达。

```json
{
  "report_id": "report:<evaluation_id>",
  "title": "Procurement Contract MVP Evaluation Report",
  "customer_profile_ref": "customer:<evaluation_id>",
  "tool_profile_ref": "tool:<evaluation_id>",
  "evaluation_period": {
    "start_date": "2026-07-03",
    "end_date": "2026-07-03"
  },
  "executive_summary": "MVP evaluation summary. Automatic checks are machine signals only; human review is required for final decision.",
  "overall_grade": "N/A",
  "capability_results": [
    {
      "capability_id": "cap:structured_output",
      "capability_name": "Structured Output",
      "grade": "N/A",
      "task_result_refs": [
        "task_01_code_to_ontology",
        "task_02_ddl_to_ontology",
        "task_03_sample_data_profile",
        "task_04_document_to_ontology",
        "task_05_multi_source_fusion"
      ],
      "notes": "Use machine_score schema_validation and JSON load errors as inputs; final grade requires human review."
    }
  ],
  "task_result_refs": [
    "task_01_code_to_ontology",
    "task_02_ddl_to_ontology",
    "task_03_sample_data_profile",
    "task_04_document_to_ontology",
    "task_05_multi_source_fusion"
  ],
  "redline_results": [
    {
      "rule_id": "redline:no_unreviewed_hallucination",
      "status": "not_tested",
      "description": "Possible hallucinations require manual adjudication before final decision."
    }
  ],
  "score_caps": [
    {
      "reason": "Human review is pending.",
      "max_grade": "B-",
      "affected_capabilities": [
        "cap:ontology_quality",
        "cap:evidence_traceability"
      ]
    }
  ],
  "key_findings": [
    "Machine score is not a final grade.",
    "Schema validity, coverage, missing evidence refs and possible hallucinations must be reviewed together."
  ],
  "risks": [
    "Human review not completed.",
    "Evidence references may include naming mismatches and require adjudication."
  ],
  "recommendations": [
    {
      "priority": "high",
      "description": "Complete manual review before issuing customer-site readiness conclusion."
    }
  ],
  "conclusion": {
    "decision": "insufficient_data",
    "rationale": "Final decision requires completed human review and sign-off.",
    "next_steps": [
      "Review machine_score.md and machine_score.json.",
      "Complete manual_review/manual_review.md.",
      "Update report conclusion after human sign-off."
    ]
  },
  "generated_at": "2026-07-03T00:00:00Z",
  "provenance": {
    "created_by": "operator_or_ai_tool",
    "created_at": "2026-07-03T00:00:00Z",
    "method": "hybrid",
    "source_system": "evaluation_outputs"
  }
}
```

## machine_score 到报告字段映射

| machine_score 字段 | 报告位置 | 说明 |
| --- | --- | --- |
| `summary` | `key_findings`、`capability_results.notes` | 说明发现的 task/ontology/evidence 文件数量。 |
| `schema_validation` | `capability_results`、`redline_results` | 结构化输出能力和红线风险。 |
| `gold_comparison.coverage` | `capability_results`、`key_findings` | 概念/属性/关系覆盖信号。 |
| `evidence_check.missing_evidence_refs` | `risks`、`redline_results` | 证据链风险；需人工判定。 |
| `possible_hallucinations` | `risks`、`redline_results` | 疑似幻觉候选；不是确认幻觉。 |
| `human_review.status` | `score_caps`、`conclusion` | pending 时不得给 ready 结论。 |

## Markdown final_eval_report.md 建议结构

```markdown
# Final Evaluation Report

## Executive Summary
## Scope And Inputs
## Tool And Environment Profile
## Task Results
## Machine Score Summary
## Human Review Summary
## Evidence And Hallucination Disposition
## Risks And Score Caps
## Recommendation
## Conclusion
## Appendix: File List
```

## 使用规范

- 报告必须区分已测能力和未测能力。
- 报告必须列出权限限制和评分上限原因。
- 报告必须明确推荐使用场景和不推荐使用场景。
- POC 准入结论必须保留人工确认环节。
- `possible_hallucinations` 是未匹配候选，不是自动确认的幻觉。
- `missing_evidence_refs` 是证据链风险，可能是命名不一致、路径错误或真实无证据。
- 不得在人工复核 pending 时输出无约束 `ready`。
