# Web Extension 后续实施计划（Manifest / C5 / C6 / C7）

## 1. 背景与当前状态

当前 Web extension 已完成并提交 C2-C4：

- C2：`datasets/generic_procurement_contract_mvp/web_snapshots/` 已包含 8 个离线 HTML snapshot。
- C3：`datasets/generic_procurement_contract_mvp/web_map/page_map.json` 和 `page_map.md` 已创建。
- C4：`prompts/tasks/task_12_web_snapshot_to_ontology.md`、`task_13_page_map_to_business_flow.md`、`task_14_extended_multi_source_fusion.md` 已创建。

这些产物已可用于手工运行 Web snapshot / page map 评估，但还不是完整的可发现、可评分、可演示闭环。下一步目标是完成：

1. Web 输入在 README / manifest 中登记，便于操作员和自动发现流程使用。
2. C5：新增 evaluator-only Web reference / conflict 文件。
3. C6：扩展 scoring，使 Web evidence 成为可选、附加、向后兼容的评分信号。
4. C7：创建 `results/demo_web/`，演示 Task 12/13/14 与 Web scoring 的闭环。

## 2. 总体原则

- 不改变 MVP baseline 的核心评分口径。
- 不让 Web evidence 默认并入 MVP core concept / key attribute / key relation coverage。
- 不破坏 `results/demo_baseline/` 和 `results/demo_screenshot/` 的可评分性。
- Web 输入、Web gold/reference、Web scoring/demo 的边界必须清楚。
- `gold/*`、`known_conflicts*`、`results/demo_*`、`machine_score*` 永远不得提供给被测 AI。
- HTML snapshot 只能代表 `html_snapshot` 输入模式，不得被描述成 `live_crawl`。
- page map 只能作为输入侧页面清单和导航说明，不是 gold answer。

## 3. 推荐实施顺序

建议分 4 个小阶段推进，每阶段单独验证，必要时可单独提交。

| 阶段 | 目标 | 主要输出 | 风险 |
| --- | --- | --- | --- |
| P0 | Web 输入登记 | README / manifest 更新 | 低 |
| C5 | Web reference / known conflicts | `gold_evidence_map.web.*`、`known_conflicts.web.*` | 中 |
| C6 | Web scoring 最小扩展 | `score_auto.py`、scoring README、测试结果 | 中高 |
| C7 | Demo Web 闭环 | `results/demo_web/` | 中 |

## 4. P0：Web 输入登记

### 4.1 目标

让 Web snapshot bundle 成为明确的可选输入扩展，避免操作员只看 manifest 时误以为 Web 仍被排除。

### 4.2 文件范围

需要修改：

- `datasets/generic_procurement_contract_mvp/README.md`
- `datasets/generic_procurement_contract_mvp/metadata/dataset_manifest.json`

不应修改：

- `datasets/generic_procurement_contract_mvp/gold/`
- `scoring/`
- `results/`

### 4.3 具体修改

#### README

在 `Inputs That May Be Provided To The AI Tool` 后新增可选 Web extension 说明，结构可参考 screenshot extension：

- `web_snapshots/*.html`
- `web_map/page_map.json`
- `web_map/page_map.md`

需要明确：

- 只有评估负责人启用 Web extension 时才提供。
- 输入模式是 `html_snapshot` 或 `page_map_only`。
- 这些文件不代表 live Web、登录态、JS 执行或真实浏览器爬取。
- `gold/gold_evidence_map.web.*`、`known_conflicts.web.*` 不提供给被测 AI。

#### dataset_manifest.json

建议调整：

- 从 `excluded_artifacts` 中移除或重新解释 `web_pages`，避免和已存在的 Web snapshot 冲突。
- 在 `optional_extensions` 中新增：

```json
{
  "extension_id": "C_web_snapshots",
  "input_mode": "html_snapshot",
  "manifest_path": "web_map/page_map.json",
  "artifact_root": "web_snapshots/",
  "baseline_included": false,
  "description": "Optional offline HTML snapshot and page map inputs for Web semantic extraction and page-flow analysis; not live Web crawling."
}
```

- 在 `artifacts` 中登记：
  - 8 个 HTML snapshot，type 可用 `web_snapshot`。
  - `web_map/page_map.json`，type 可用 `web_page_map`。
  - `web_map/page_map.md`，type 可用 `web_page_map_documentation`。

### 4.4 验收标准

- README 明确区分 MVP baseline、screenshot surrogate、Web snapshot。
- manifest 中可发现 Web optional extension。
- manifest JSON 合法。
- 不修改 gold/scoring/results。
- 不把 Web gold 或 known conflicts 列为 AI 输入。

### 4.5 验证命令

```bash
python3 -m json.tool datasets/generic_procurement_contract_mvp/metadata/dataset_manifest.json >/dev/null
rg -n "C_web_snapshots|web_snapshots|page_map" datasets/generic_procurement_contract_mvp/README.md datasets/generic_procurement_contract_mvp/metadata/dataset_manifest.json
```

## 5. C5：新增 Web evaluator-only reference / conflicts

### 5.1 目标

新增 Web 专用的 evaluator-only reference，使人工评审和 C6 scoring 能判断 Web evidence 是否被正确引用，同时不泄漏给被测 AI。

### 5.2 文件范围

新增：

- `datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.json`
- `datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.md`
- `datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.json`
- `datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.md`

不应修改：

- `gold/gold_ontology.json`
- `gold/gold_evidence_map.json`
- `gold/known_conflicts.json`
- `scoring/`

### 5.3 `gold_evidence_map.web.json` 建议结构

建议沿用 existing evidence schema 的最小字段，并专门使用 `web:*` evidence id。

```json
{
  "schema_version": "1.0.0",
  "dataset_id": "generic_procurement_contract_mvp",
  "input_mode": "html_snapshot",
  "description": "Evaluator-only Web evidence reference for offline HTML snapshots and page map.",
  "evidence": [
    {
      "evidence_id": "web:purchase_requests.table.pr_no",
      "evidence_type": "web_page",
      "source": {
        "type": "file",
        "path": "web_snapshots/purchase_requests.html"
      },
      "content_ref": "web_snapshots/purchase_requests.html",
      "locator": "table header: PR No",
      "web_page": {
        "url": "web_snapshots/purchase_requests.html",
        "title": "Purchase Requests",
        "dom_path": "table thead th",
        "text_snippet": "PR No"
      },
      "metadata": {
        "input_mode": "html_snapshot",
        "page_id": "web:purchase_requests"
      }
    }
  ]
}
```

### 5.4 Web evidence coverage 建议

不要穷举所有 DOM 文本；建议覆盖能测试能力边界的代表性 evidence：

#### 页面级 evidence

- `web:home.page`
- `web:purchase_requests.page`
- `web:purchase_request_detail.page`
- `web:approval_tasks.page`
- `web:contracts.page`
- `web:contract_detail.page`
- `web:invoices.page`
- `web:payments.page`

#### 字段 / 表格 evidence

- PR No / Requester / Department / Supplier / Amount / Status。
- Preferred Vendor。
- Approval Task 的 Target Type / Target No。
- Contract No / Vendor / Source PR / Source PO / Legal Approved At / Activated At。
- Invoice No / Supplier Invoice No / PO No / GRN No / Difference %。
- Payment Application No / Payment Request No / Hold Reason / Payment Status。

#### action evidence

- New Purchase Request。
- Submit / Cancel PR。
- Create Contract。
- Approve / Reject / Return。
- Submit Legal Review / Activate Contract / Terminate Contract。
- Match Invoice / Create Payment Request。
- Submit Payment Approval / Approve Payment / Mark Paid / Release Hold。

#### flow / link evidence

- Home -> Purchase Requests。
- Purchase Requests -> PR Detail。
- PR Detail -> Contract Detail。
- Contract Detail -> Invoices。
- Invoices -> Payments。
- Payments -> Approval Tasks。

### 5.5 `known_conflicts.web.*` 建议内容

至少包含 C1 中定义的 6 类：

- `web_vs_document_flow_mismatch`
- `page_action_without_backend_evidence`
- `ui_vs_database_naming_mismatch`
- `role_permission_web_vs_doc_mismatch`
- `missing_page_or_broken_link`
- `web_only_business_term`

每条 conflict 建议包含：

- `conflict_id`
- `conflict_type`
- `title`
- `description`
- `web_evidence_refs`
- `related_non_web_sources`（如只描述类别即可，避免过度写答案）
- `expected_handling`
- `severity`
- `review_notes`

### 5.6 验收标准

- JSON 合法。
- 所有 `web:*` evidence id 唯一。
- 所有 `content_ref` / `source.path` 指向真实 `web_snapshots/` 或 `web_map/` 文件。
- 不修改 baseline gold。
- README / prompt 明确这些文件不得给被测 AI。

### 5.7 验证命令

```bash
python3 -m json.tool datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.json >/dev/null
python3 -m json.tool datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.json >/dev/null
python3 - <<'PY'
from pathlib import Path
import json
root = Path('datasets/generic_procurement_contract_mvp')
data = json.loads((root / 'gold/gold_evidence_map.web.json').read_text())
ids = []
for item in data.get('evidence', []):
    ids.append(item['evidence_id'])
    for key in ('content_ref',):
        if item.get(key) and not (root / item[key]).exists():
            raise SystemExit(f"missing {key}: {item[key]}")
    source = item.get('source') or {}
    if source.get('path') and not (root / source['path']).exists():
        raise SystemExit(f"missing source.path: {source['path']}")
if len(ids) != len(set(ids)):
    raise SystemExit('duplicate web evidence_id')
print('web gold evidence refs ok')
PY
```

## 6. C6：最小扩展 scoring 支持 optional Web evidence

### 6.1 目标

让 `score_auto.py` 可选读取 Web gold evidence，并在 `machine_score.json` / `machine_score.md` 中报告 Web evidence 覆盖情况，同时保持 baseline 和 screenshot demo 向后兼容。

### 6.2 文件范围

需要修改：

- `scoring/score_auto.py`
- `scoring/README.md`

可能需要新增或更新测试/验证说明：

- `docs/WEB_EXTENSION_NEXT_IMPLEMENTATION_PLAN.md`（本文件，可更新结果）
- `results/demo_web/`（C7 时做）

不应修改：

- MVP gold ontology coverage 逻辑。
- baseline gold 文件。

### 6.3 现有 scoring 入口

`score_auto.py` 当前已有 screenshot optional evidence 的模式：

- `extract_screenshot_gold_items(...)`
- `build_screenshot_evidence_summary(...)`
- `gold/gold_evidence_map.screenshot.json` 可选读取。
- `machine_score.json` 的 `evidence_check.screenshot_evidence` 输出摘要。
- `machine_score.md` 输出 screenshot evidence 摘要。

Web scoring 建议复用同样模式。

### 6.4 具体实现建议

#### 新增 helper

新增：

- `extract_web_gold_items(data)`
- `build_web_evidence_summary(web_items, evidence_rows, dataset_dir)`

建议指标：

```json
{
  "enabled": true,
  "gold_web_evidence_count": 0,
  "referenced_web_evidence_count": 0,
  "matched_web_evidence_count": 0,
  "missing_web_evidence_refs": [],
  "invalid_web_snapshot_paths": [],
  "page_map_file_count": 0,
  "input_mode": "html_snapshot",
  "note": "Web evidence checks are optional and do not change MVP gold ontology coverage."
}
```

#### main 中加载 Web gold

新增：

```python
web_gold_path = dataset_dir / "gold" / "gold_evidence_map.web.json"
web_gold = load_optional_json(web_gold_path)
web_evidence_items = extract_web_gold_items(web_gold)
```

并将 `web_evidence_items` 加入 available refs：

```python
available_refs = build_available_evidence_refs(
    evaluation_dir,
    dataset_dir,
    evidence_items + screenshot_evidence_items + web_evidence_items,
    discovered["task_results"],
)
```

#### evidence_check 输出

新增：

```python
"web_evidence": web_evidence_summary
```

#### machine_metrics 输出

新增：

- `missing_web_evidence_ref_count`
- `referenced_web_evidence_count`
- `matched_web_evidence_count`
- `invalid_web_snapshot_path_count`
- `web_evidence_enabled`

#### markdown 输出

在 `## Evidence References` 下新增：

- Web evidence enabled。
- Web evidence refs checked。
- Missing Web evidence refs。
- Invalid Web snapshot paths。

### 6.5 兼容性要求

必须验证：

- 没有 `gold_evidence_map.web.json` 时，脚本不报错，`web_evidence.enabled = false`。
- `results/demo_baseline/` 可评分。
- `results/demo_screenshot/` 可评分。
- Web evidence 不改变 core concept / key attribute / key relation coverage。
- Web missing refs 只影响 Web evidence 摘要，不直接判定整体验证失败。

### 6.6 验收标准

- `python3 scoring/score_auto.py demo_baseline` 成功。
- `python3 scoring/score_auto.py demo_screenshot` 成功。
- 有 Web gold 时，`machine_score.json` 包含 `evidence_check.web_evidence`。
- `machine_score.md` 包含 Web evidence summary。
- MVP coverage 数值在同一输入下不因启用 Web gold 而变化。

### 6.7 验证命令

```bash
python3 scoring/score_auto.py demo_baseline
python3 scoring/score_auto.py demo_screenshot
python3 - <<'PY'
import json
from pathlib import Path
for run in ['demo_baseline', 'demo_screenshot']:
    p = Path('results') / run / 'scoring/machine_score.json'
    data = json.loads(p.read_text())
    assert 'web_evidence' in data['evidence_check']
    print(run, data['evidence_check']['web_evidence']['enabled'])
PY
```

## 7. C7：创建 `results/demo_web/` 演示闭环

### 7.1 目标

提供一套可审阅的 Web extension demo，展示：

- Task 12 能从 HTML snapshot / page map 输出 Web-derived ontology supplement。
- Task 13 能从 page map 输出业务流程 / 页面路径分析。
- Task 14 能把 MVP baseline 与 Web 输出融合。
- C6 scoring 能识别 Web evidence 摘要，同时不破坏 MVP coverage。

### 7.2 文件范围

新增目录：

```text
results/demo_web/
```

建议包含：

```text
results/demo_web/README.md
results/demo_web/execution_log.md
results/demo_web/tool_profile.json
results/demo_web/human_effort_log.json
results/demo_web/raw_outputs/task_12_web_snapshot_to_ontology_raw.md
results/demo_web/raw_outputs/task_13_page_map_to_business_flow_raw.md
results/demo_web/raw_outputs/task_14_extended_multi_source_fusion_raw.md
results/demo_web/normalized_outputs/task_12_web_snapshot_to_ontology.json
results/demo_web/normalized_outputs/task_13_page_map_to_business_flow.json
results/demo_web/normalized_outputs/task_14_extended_multi_source_fusion.json
results/demo_web/task_12_web_snapshot_to_ontology_result.json
results/demo_web/task_13_page_map_to_business_flow_result.json
results/demo_web/task_14_extended_multi_source_fusion_result.json
results/demo_web/scoring/machine_score.json
results/demo_web/scoring/machine_score.md
results/demo_web/report/evaluation_report.json
results/demo_web/report/final_eval_report.md
```

可选：如果不想一次性补 report，可先只做 raw / normalized / task_result / scoring，report 放后续阶段。

### 7.3 Demo 输出内容建议

#### Task 12 normalized output

需要包含：

- `input_mode = html_snapshot`
- `source_system = web_snapshot`
- `pages` 数组，覆盖 8 个页面。
- `concepts`、`attributes`、`relations`、`actions`、`states`、`roles`。
- `aliases`：Vendor/Supplier、PR/Purchase Request、GRN/Goods Receipt、Payment Application/Payment Request。
- `mappings`：UI label -> candidate ontology element。
- `conflicts` / `uncertainties`：UI-only actions、缺页、静态 snapshot 限制。
- `evidence_refs`：必须包含 `web:*`。

#### Task 13 normalized output

需要包含：

- `input_mode = html_snapshot_with_page_map` 或 `page_map_only`，按实际输入说明。
- `module_paths`。
- `business_flows`。
- `role_paths`。
- `navigation_graph.nodes` / `navigation_graph.edges`。
- `recursive_analysis_points`。
- `missing_pages`。
- `uncertainties`。

#### Task 14 normalized output

需要包含：

- `input_mode = mvp_plus_web_snapshot` 或 `mvp_plus_screenshot_plus_web`。
- `source_coverage`。
- 融合后的 concepts / aliases / mappings / page_flows / fusion_decisions。
- 清楚保留 Web-only / UI-only 不确定性。
- 不把 UI button 直接提升为后端事实。

### 7.4 Task result wrapper 要求

每个 task result wrapper 需要：

- `task_id`
- `status`
- `input_artifacts`
- `output_artifacts`
- `evidence_refs`
- `started_at` / `completed_at` 或同类时间字段（按 schema 实际要求）
- 指向 raw 和 normalized 文件。

### 7.5 验收标准

- `results/demo_web/` 下 JSON 都合法。
- `score_auto.py demo_web` 成功生成 machine score。
- `machine_score.json` 包含 Web evidence summary。
- `machine_score.md` 可读地展示 Web evidence 摘要。
- Web demo 不依赖 live Web、外部网络或后端服务。
- Demo 中不泄漏 gold Web reference 给被测 AI 的 prompt 输入。

### 7.6 验证命令

```bash
python3 scoring/score_auto.py demo_web
python3 -m json.tool results/demo_web/normalized_outputs/task_12_web_snapshot_to_ontology.json >/dev/null
python3 -m json.tool results/demo_web/normalized_outputs/task_13_page_map_to_business_flow.json >/dev/null
python3 -m json.tool results/demo_web/normalized_outputs/task_14_extended_multi_source_fusion.json >/dev/null
python3 -m json.tool results/demo_web/scoring/machine_score.json >/dev/null
rg -n "Web evidence|web_evidence|TASK-12|TASK-13|TASK-14" results/demo_web
```

## 8. 回归测试矩阵

| 测试项 | 命令 / 检查 | 通过条件 |
| --- | --- | --- |
| manifest JSON | `python3 -m json.tool .../dataset_manifest.json` | JSON 合法 |
| Web page map JSON | `python3 -m json.tool .../page_map.json` | JSON 合法 |
| Web gold JSON | `python3 -m json.tool .../gold_evidence_map.web.json` | JSON 合法 |
| Web conflicts JSON | `python3 -m json.tool .../known_conflicts.web.json` | JSON 合法 |
| HTML snapshot 存在 | 检查 8 个文件 | 全部存在 |
| page map evidence refs | 自定义脚本 | 全部指向真实文件 |
| baseline scoring | `python3 scoring/score_auto.py demo_baseline` | 成功，无异常 |
| screenshot scoring | `python3 scoring/score_auto.py demo_screenshot` | 成功，无异常 |
| web demo scoring | `python3 scoring/score_auto.py demo_web` | 成功生成 Web evidence summary |
| 禁止泄漏 | `rg -n "gold_evidence_map.web|known_conflicts.web" prompts datasets/.../web_snapshots datasets/.../web_map` | prompts 只能出现禁止读取说明；HTML/page map 不包含 evaluator-only gold 内容 |

## 9. 建议提交拆分

### Commit 1：登记 Web optional input

```text
docs: register web snapshot optional input
```

包含：README + dataset_manifest 更新。

### Commit 2：新增 Web evaluator reference

```text
gold: add web evidence references and conflicts
```

包含：`gold_evidence_map.web.*`、`known_conflicts.web.*`。

### Commit 3：扩展 Web scoring

```text
scoring: add optional web evidence checks
```

包含：`score_auto.py`、`scoring/README.md`、必要验证说明。

### Commit 4：新增 demo_web

```text
results: add web extension demo run
```

包含：`results/demo_web/`。

如果希望减少 commit 数，也可合并为两个 commit：

1. `docs: register web optional inputs and references`
2. `scoring: add web evidence checks and demo`

## 10. 风险与控制

### 10.1 Web snapshot 被误解为 live Web

控制：

- README、prompt、demo 输出和 scoring report 都必须显示 `input_mode = html_snapshot`。
- 报告中明确“不代表登录、JS、API、真实浏览器或 live crawl”。

### 10.2 page map 泄漏过多标准答案

控制：

- page map 只列页面清单、可见字段、链接和 crawl notes。
- 不写 expected ontology resolution。
- 不写 scoring 结论。

### 10.3 UI action 被当作后端事实

控制：

- Web known conflicts 中记录 `page_action_without_backend_evidence`。
- Task 12/14 prompt 要求 UI button 仅作为 candidate action。
- Demo 输出中保留 uncertainty。

### 10.4 Web evidence 破坏历史可比性

控制：

- Web evidence 只进入 `evidence_check.web_evidence` 和 optional metrics。
- 不改变 `gold_comparison.coverage` 的核心计算。
- baseline / screenshot demo 必须回归通过。

### 10.5 Gold/reference 泄漏

控制：

- `gold/*web*` 只在 evaluator / scorer 使用。
- README 和 prompt 明确禁止提供。
- Demo execution log 记录实际提供给 AI 的输入清单。

## 11. 完成定义

完成 P0-C7 后，应满足：

- 操作员可以从 README / manifest 发现 Web optional extension。
- 被测 AI 可以使用 Task 12/13/14 处理 Web snapshot / page map。
- Evaluator 有 Web evidence reference 和 Web known conflicts 用于复核。
- `score_auto.py` 可以报告 Web evidence 覆盖情况。
- `results/demo_web/` 展示 Web 任务输出、融合输出和评分摘要。
- MVP baseline 和 screenshot demo 仍可独立运行、独立评分。

## 12. 下一步执行建议

建议下一轮先做 P0，因为它风险最低、能立刻提升可用性，并为 C5/C6/C7 提供统一的文件发现入口。

P0 完成后再做 C5；C5 完成并验证 evidence refs 后，再做 C6 scoring；最后用 C7 demo_web 验证完整闭环。
