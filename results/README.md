# results

## 用途

`results/` 存放每次评估的原始输出、标准化结果、评分结果、人工复核和最终报告。每次评估必须使用独立 evaluation_id，避免覆盖 demo 或其他客户结果。

## 标准目录结构

推荐结构：

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
<YYYYMMDD>-<customer_code>-<tool_stack>-<level>
```

示例：

```text
20260703-demo-claude-smoke
```

`results/demo_baseline/` 是模拟示例结果，只用于学习目录结构和评分输出，不要作为真实评估输入或覆盖目标。

## 各目录说明

| 路径 | 内容 | 说明 |
| --- | --- | --- |
| `customer_profile.json` | 客户环境画像 | 尽量兼容 `schemas/customer_profile.schema.json`。 |
| `tool_profile.json` | 工具画像 | 尽量兼容 `schemas/tool_profile.schema.json`。 |
| `execution_log.md` | 执行日志 | 记录时间、任务、输入、失败、重试、人工介入。 |
| `raw_outputs/` | AI 原始输出 | 不要修改；可保存 Markdown、文本或原始 JSON。 |
| `normalized_outputs/` | 标准化 artifact | 保存整理后的 ontology、evidence、profile、repair 输出。 |
| `scoring/` | 自动评分输出 | `score_auto.py` 默认写入 `machine_score.json` 和 `machine_score.md`。 |
| `manual_review/` | 人工复核 | 保存人工评分、证据处置、幻觉判定和 sign-off。 |
| `report/` | 最终报告 | 保存 `evaluation_report.json` 和可选 `final_eval_report.md`。 |
| `artifacts/` | 附件 | 保存额外截图、日志、导出文件等。 |

## Raw / Normalized / Task Result

不要混淆三类文件：

1. `raw_outputs/*.md`：AI 工具原始回答，保留原样。
2. `normalized_outputs/*.json`：操作员整理后的合法 JSON artifact，例如 ontology 或 evidence map。
3. `task_XX_*_result.json`：任务执行结果 wrapper，符合 `schemas/task_result.schema.json`，通过 `output_artifacts` 指向 normalized/raw 文件。

`score_auto.py` 可以发现包含 `task_id` 和 `output_artifacts` 的 task result wrapper，也可以发现包含 `ontology_id` 和 `concepts` 的 standalone ontology JSON。为了可复盘，真实评估应同时保存 wrapper 和 normalized artifact。

## Task Result Wrapper 示例

```json
{
  "task_id": "task_05_multi_source_fusion",
  "task_name": "Multi Source Fusion",
  "mode": "fixed_prompt",
  "level": "smoke",
  "status": "completed",
  "started_at": "2026-07-03T00:00:00Z",
  "completed_at": "2026-07-03T00:20:00Z",
  "output_artifacts": [
    {
      "artifact_id": "artifact:task_05.ontology",
      "artifact_type": "ontology",
      "path": "normalized_outputs/task_05_multi_source_fusion.json",
      "schema_ref": "schemas/ontology.schema.json"
    },
    {
      "artifact_id": "artifact:task_05.raw",
      "artifact_type": "raw_output",
      "path": "raw_outputs/task_05_multi_source_fusion_raw.md"
    }
  ],
  "human_interventions": [],
  "limitations": [],
  "notes": "Raw output was normalized into an ontology artifact."
}
```

Artifact path 应使用相对于 `results/<evaluation_id>/` 的路径。

## 最终报告约定

Canonical 结构化报告：

```text
results/<evaluation_id>/report/evaluation_report.json
```

可选 Markdown 展示报告：

```text
results/<evaluation_id>/report/final_eval_report.md
```

`evaluation_report.json` 应尽量兼容 `schemas/evaluation_report.schema.json`。`final_eval_report.md` 是展示层，应由 JSON、machine score、人工复核表和执行日志整理而来，不得包含 JSON 中没有依据的结论。

## 使用规范

- 原始输出必须保存，不得只保存整理后的答案。
- 追问记录、失败记录和人工修复必须保存。
- 不得把人工补写结果伪装为模型输出。
- 不得把 `datasets/*/gold/` 或 `results/demo_baseline/` 提供给被评估 AI 工具。
- 自动评分不是最终评分，最终结论必须包含人工复核。
- 客户敏感材料不能未经授权带出客户环境。
- 可沉淀的历史结果应先脱敏再进入 `benchmark_history/`。
