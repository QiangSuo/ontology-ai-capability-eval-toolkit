# Operator Guide

`operator_guide/` 面向低经验操作员，目标是让操作员在客户现场按固定步骤完成 MVP Smoke Test，保存可复盘结果，并避免把 gold/reference/demo 内容泄漏给被评估 AI 工具。

## 1. 执行边界

本指南只覆盖 MVP Smoke Test：代码、DDL、CSV 样例数据、业务文档和多源融合。不包含截图、Web、真实数据库连接或客户生产数据。

严禁把以下内容作为输入提供给被评估 AI：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `docs/MVP_CONSISTENCY_CHECK.md`
- `docs/DRY_RUN_REVIEW.md`
- `scoring/score_auto.py`
- `scoring/SCORING_RUBRIC.md`
- 任何人工评分答案、gold answer、known conflicts 或 machine_score 输出

这些文件只供操作员评分、复核和学习目录结构使用，不属于被测输入。

## 2. Smoke Test 一页运行表

| 顺序 | 任务 | 输入 | 输出 | 停止条件 |
| --- | --- | --- | --- | --- |
| 0 | 建立结果目录 | evaluation_id | `results/<evaluation_id>/` | 无法创建目录时停止 |
| 1 | Task 00 环境检查 | 工具/模型/权限信息 | `tool_profile.json`、可选 `customer_profile.json` | 工具能力未知也可继续，但必须记录 unknown/unverified |
| 2 | Task 01 代码抽取 | Smoke 代码文件 | raw 输出、normalized ontology、task_result wrapper | AI 无法读取/接收代码时记录 blocked |
| 3 | Task 02 DDL 抽取 | `database/ddl.sql` | raw 输出、normalized ontology、task_result wrapper | DDL 缺失或输出不可修复时记录 failed |
| 4 | Task 03 CSV 画像 | core CSV 切片 | raw 输出、sample profile、task_result wrapper | CSV 切片不完整时记录 `sample_is_partial` |
| 5 | Task 04 文档抽取 | Smoke 文档 | raw 输出、normalized ontology、task_result wrapper | 文档缺失或输出不可修复时记录 failed |
| 6 | Task 05 多源融合 | Task 01-04 normalized 输出 | fused ontology、evidence map、task_result wrapper | 前置任务少于 2 个 completed 时记录 insufficient data |
| 7 | Task 06 schema repair | invalid JSON/schema errors | repair wrapper、repaired artifact、repair task_result | 每个问题最多 1 次 repair，仍失败则记录 failed |
| 8 | 自动评分 | evaluation_id | `scoring/machine_score.json`、`scoring/machine_score.md` | `ontology_file_count = 0` 或 JSON load error 需先排查 |
| 9 | 人工复核 | machine score、raw outputs、execution log | `manual_review/manual_review.md` | human review 未完成不得给最终 Go 结论 |
| 10 | Task 07 / final report | task results、machine score、human review | `report/evaluation_report.json` 和/或 `report/final_eval_report.md` | 缺 human review 时只能给 insufficient_data 或 ready_with_constraints |

## 3. Smoke 输入文件矩阵

所有路径均相对于 `datasets/generic_procurement_contract_mvp/`。

### 3.1 必选输入

| 类型 | 文件 | 提供方式 |
| --- | --- | --- |
| DDL | `database/ddl.sql` | 提供完整文件 |
| 文档 | `documents/business_overview.md` | 提供完整文件 |
| 文档 | `documents/procurement_process.md` | 提供完整文件 |
| 代码 | `source_code/src/main/java/com/example/procurement/service/PurchaseRequestService.java` | 提供完整文件 |
| 代码 | `source_code/src/main/java/com/example/procurement/service/ApprovalService.java` | 提供完整文件 |

### 3.2 CSV Smoke 切片

默认 smoke 切片使用表头 + 前 5 行。若工具支持文件读取，可直接提供整个 CSV；若只能复制粘贴，按下表复制表头和前 5 行，并在 Task 03 中设置 `sample_is_partial = true`。

| CSV | 选择规则 | 用途 |
| --- | --- | --- |
| `database/sample_data/pc_purchase_request.csv` | header + rows 1-5 | 采购申请状态、金额、申请人、部门 |
| `database/sample_data/pc_purchase_request_line.csv` | header + rows 1-5 | 申请行、物料/服务、数量、金额 |
| `database/sample_data/pc_approval_record.csv` | header + rows 1-5 | 审批对象、审批状态、审批人 |
| `database/sample_data/pc_contract.csv` | header + rows 1-5 | 合同状态、供应商、申请引用 |
| `database/sample_data/pc_invoice.csv` | header + rows 1-5 | 发票状态、匹配与付款线索 |
| `database/sample_data/pc_payment_request.csv` | header + rows 1-5 | 付款申请与付款状态 |

如果操作员使用其他行，必须在 `execution_log.md` 中记录文件名、是否含表头、行号范围和选择理由。

## 4. 结果目录规范

每次评估必须新建独立目录：

```text
results/<evaluation_id>/
  customer_profile.json
  tool_profile.json
  execution_log.md
  raw_outputs/
  normalized_outputs/
  scoring/
  manual_review/
  report/
  artifacts/
```

推荐命名：

```text
<YYYYMMDD>-<customer_code>-<tool_stack>-smoke
```

示例：

```text
20260703-demo-claude-smoke
```

不要直接写入 `results/demo_baseline/`，它是示例结果。

## 5. Raw / Normalized / Task Result 的区别

| 类型 | 保存位置 | 说明 |
| --- | --- | --- |
| raw output | `raw_outputs/task_XX_*.md` | AI 原始回答，允许包含 Markdown fence 和解释文字 |
| normalized artifact | `normalized_outputs/*.json` | 操作员整理后的合法 JSON，例如 ontology/evidence/profile |
| task_result wrapper | `task_XX_*_result.json` | 符合 `schemas/task_result.schema.json`，用于让 `score_auto.py` 发现 artifact |
| machine score | `scoring/` | `score_auto.py` 生成 |
| manual review | `manual_review/` | 人工复核表和签字意见 |
| final report | `report/` | `evaluation_report.json` 和/或 `final_eval_report.md` |

固定 prompt 让被测 AI 输出业务 JSON；操作员随后把它保存为 raw output，并在 normalized 目录中整理成 schema-friendly artifact。不要把人工补写内容伪装成 AI 原始输出。

## 6. 最小 task_result wrapper 模板

Task 01-05 的 wrapper 至少应包含：

```json
{
  "task_id": "task_01_code_to_ontology",
  "task_name": "Code to Ontology",
  "mode": "fixed_prompt",
  "level": "smoke",
  "status": "completed",
  "tool_profile_ref": "tool:<evaluation_id>",
  "started_at": "2026-07-03T00:00:00Z",
  "completed_at": "2026-07-03T00:10:00Z",
  "output_artifacts": [
    {
      "artifact_id": "artifact:task_01.ontology",
      "artifact_type": "ontology",
      "path": "normalized_outputs/task_01_code_to_ontology.json",
      "schema_ref": "schemas/ontology.schema.json"
    },
    {
      "artifact_id": "artifact:task_01.raw",
      "artifact_type": "raw_output",
      "path": "raw_outputs/task_01_code_to_ontology_raw.md"
    }
  ],
  "human_interventions": [],
  "limitations": [],
  "notes": "Raw output was normalized into an ontology artifact."
}
```

路径应相对于 `results/<evaluation_id>/`。不要使用绝对路径，除非客户环境要求且已记录原因。

## 7. Task 00 处理规则

Task 00 是环境和工具能力登记，不是 ontology 质量评分任务。推荐输出：

- `tool_profile.json`：尽量兼容 `schemas/tool_profile.schema.json`。
- `customer_profile.json`：尽量兼容 `schemas/customer_profile.schema.json`。
- `raw_outputs/task_00_environment_check_raw.md`：保存原始回答。

如果某个能力未知，不要猜测。对于 schema 中必须是 boolean 的字段，采用保守值 `false`，并在 `known_limitations`、`metadata.unverified_capabilities` 或 notes 中记录 unknown/unverified。

## 8. Task 06 repair 处理规则

仅在 JSON 不合法或 schema 明显不兼容时运行 Task 06。每个待修复输出最多允许 1 次 repair。

保存规则：

```text
raw_outputs/task_06_schema_repair_raw.md
normalized_outputs/task_06_schema_repair_wrapper.json
normalized_outputs/<original_task>_repaired.json
task_06_schema_repair_result.json
```

`repaired_output` 不会被 `score_auto.py` 自动发现。操作员必须把修复后的实际 ontology/evidence 另存为 `normalized_outputs/<original_task>_repaired.json`，并在 task_result wrapper 的 `output_artifacts` 中引用它。

## 9. 自动评分命令

在工具包根目录运行：

```bash
python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp
```

如果只是 dry run，不想覆盖仓库内评分文件，使用：

```bash
python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp --output-dir /tmp/<evaluation_id>_scoring_dry_run
```

仓库路径含空格和中文字符时，直接路径必须加引号：

```bash
cd "/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit"
python3 scoring/score_auto.py demo_baseline --dataset generic_procurement_contract_mvp --output-dir /tmp/demo_baseline_scoring_dry_run
```

## 10. 人工复核 Gate

自动评分完成后，必须人工复核：

- schema validation 是否通过。
- core concept / key attribute / key relation 覆盖是否可接受。
- missing evidence refs 是真实缺证据，还是 ref 命名不一致。
- possible hallucinations 是否是真幻觉、合理抽象或 gold/alias 缺口。
- 工具限制是否触发评分上限。
- 是否允许进入 Internal Pilot 或仅允许 constrained pilot。

人工复核未完成时，不得给出最终 Go 结论。

## 11. Final Report Gate

当前 canonical 机器可校验报告是：

```text
results/<evaluation_id>/report/evaluation_report.json
```

如果需要给管理层阅读，可从 JSON 和人工复核表渲染：

```text
results/<evaluation_id>/report/final_eval_report.md
```

`final_eval_report.md` 是展示文档；`evaluation_report.json` 是 schema-valid 结构化报告。二者内容必须一致。

## 12. 失败记录规范

每次失败至少记录：

```json
{
  "task_id": "task_XX",
  "status": "failed",
  "failure_type": "invalid_json | missing_input | tool_limit | timeout | hallucination | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_XX_raw.md"
}
```

任何失败、超时、工具限制、人工介入都必须写入 `execution_log.md`。不得为了评分好看而删除失败记录。
