# scoring 使用说明

`scoring/` 存放自动评分脚本、评分规则和人工复核说明。本目录当前提供 `score_auto.py`，用于对一次评估结果做离线机器检查，帮助操作员快速发现结构化输出、gold 覆盖、evidence 引用和疑似幻觉问题。

> 注意：自动评分不是最终业务评分。`score_auto.py` 只能给出机器可检查的信号，最终结论仍需要人工结合原始输出、执行日志和业务语义复核。

## 1. score_auto.py 的用途

`score_auto.py` 会读取一次评估结果目录，并执行以下检查：

1. 发现任务结果 JSON、ontology JSON 和 evidence JSON。
2. 校验任务结果、ontology、evidence 是否符合 `schemas/` 下的 JSON Schema。
3. 将输出 ontology 与数据集 gold ontology 做 alias-aware 对比。
4. 统计核心概念、关键属性、关键关系的覆盖率。
5. 检查 ontology 中引用的 evidence ref 是否能在数据集或评估结果中找到。
6. 如果数据集提供可选 `gold_evidence_map.screenshot.json`，额外汇总 screenshot surrogate evidence 覆盖信号。
7. 如果数据集提供可选 `gold_evidence_map.web.json`，额外汇总 Web snapshot evidence 覆盖信号。
8. 标记无法匹配 gold 或 alias 的 concept / attribute / relation，作为 possible hallucinations。
9. 输出机器可读的 `machine_score.json` 和操作员可读的 `machine_score.md`。

它适合用于 MVP 阶段的自动检查，尤其是判断输出是否能被后续评分和报告流程消费。

## 2. 输入目录结构要求

推荐每次评估在 `results/` 下建立一个独立目录，例如：

```text
results/<evaluation_id>/
  customer_profile.json
  execution_log.md
  raw_outputs/
  normalized_outputs/
  scoring/
  manual_review/
  report/
  artifacts/
```

最低要求不是所有目录都必须存在，但为了便于复核，建议保留完整结构。

### 2.1 必备或推荐文件

| 路径 | 是否必需 | 用途 |
| --- | --- | --- |
| `customer_profile.json` | 推荐 | 记录客户环境、工具、模型、权限和网络限制。 |
| `execution_log.md` | 推荐 | 记录执行过程、prompt 调整、重试和人工介入。 |
| `raw_outputs/` | 推荐 | 保存 AI 工具原始输出，供人工复核。 |
| `normalized_outputs/` | 推荐 | 保存整理后的 task result、ontology、evidence JSON。 |
| `scoring/` | 自动生成 | 默认输出 `machine_score.json` 和 `machine_score.md`。 |
| `manual_review/` | 推荐 | 保存人工评分表和复核意见。 |
| `report/` | 推荐 | 保存最终评估报告。 |
| `artifacts/` | 可选 | 保存补充材料。 |

### 2.2 score_auto.py 会发现哪些 JSON

`score_auto.py` 会递归扫描评估目录下的 JSON 文件，并按结构识别：

1. **Task result JSON**：包含 `task_id` 和 `output_artifacts` 的文件。
2. **Ontology JSON**：task result 的 `output_artifacts` 中 `artifact_type = ontology` 指向的文件，或包含 `ontology_id` 和 `concepts` 的 standalone JSON。
3. **Evidence JSON / evidence map**：task result 的 `output_artifacts` 中 `artifact_type = evidence` 指向的文件，或包含 `evidence_id`、`evidence`、`evidences`、`items` 等 evidence 结构的 JSON。

如果数据集目录中存在 `gold/gold_evidence_map.screenshot.json`，脚本会把其中的 `screen:*` evidence handle 加入可用证据集合，并在 `evidence_check.screenshot_evidence` 中输出可选截图 evidence 覆盖摘要。该逻辑是 additive，不会改变 MVP 核心概念、属性、关系覆盖率。

如果数据集目录中存在 `gold/gold_evidence_map.web.json`，脚本会把其中的 `web:*` evidence handle 加入可用证据集合，并在 `evidence_check.web_evidence` 中输出可选 Web evidence 覆盖摘要。该逻辑同样是 additive，不会改变 MVP 核心概念、属性、关系覆盖率，也不代表 live Web crawling 能力。

建议操作员把标准化结果放在 `normalized_outputs/`，并在 task result 的 `output_artifacts` 中引用这些文件。

## 3. results/<evaluation_id>/ 应包含哪些文件

MVP 推荐至少包含：

```text
results/<evaluation_id>/
  raw_outputs/
    task_01_code_to_ontology_raw.md
    task_02_ddl_to_ontology_raw.md
    task_03_sample_data_profile_raw.md
    task_04_document_to_ontology_raw.md
    task_05_multi_source_fusion_raw.md
  normalized_outputs/
    task_01_code_to_ontology_result.json
    task_02_ddl_to_ontology_result.json
    task_03_sample_data_profile_result.json
    task_04_document_to_ontology_result.json
    task_05_multi_source_fusion_result.json
    ontology.json
    evidence_map.json
  tool_profile.json
  human_effort_log.json
  scoring/
    machine_score.json
    machine_score.md
```

实际文件名可以不同，但要满足：

- task result JSON 能被识别为包含 `task_id` 和 `output_artifacts`。
- ontology artifact 路径能指向真实存在的 ontology JSON。
- evidence artifact 路径能指向真实存在的 evidence JSON 或 evidence map。
- 路径尽量使用评估目录内的相对路径，例如 `normalized_outputs/ontology.json`。

## 4. 如何运行 score_auto.py

请在工具包根目录运行：

```bash
python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp
```

其中 `<evaluation_id>` 可以是：

1. `results/` 下的目录名，例如 `demo_baseline`。
2. 一个真实存在的评估目录路径，例如 `/path/to/evaluation_result`。

脚本默认会把输出写入：

```text
results/<evaluation_id>/scoring/
```

如果传入的是直接路径，则默认写入：

```text
<evaluation_dir>/scoring/
```

## 5. 命令示例

### 5.1 使用默认 results 目录

```bash
python3 scoring/score_auto.py demo_baseline --dataset generic_procurement_contract_mvp
```

### 5.2 指定 results 根目录

```bash
python3 scoring/score_auto.py demo_baseline \
  --results-dir results \
  --dataset generic_procurement_contract_mvp
```

### 5.3 直接传入评估目录路径

```bash
python3 scoring/score_auto.py /path/to/results/demo_baseline \
  --dataset generic_procurement_contract_mvp
```

### 5.4 指定输出目录

```bash
python3 scoring/score_auto.py demo_baseline \
  --dataset generic_procurement_contract_mvp \
  --output-dir /tmp/demo_baseline_scoring
```

## 6. 参数说明

| 参数 | 是否必需 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `evaluation_id` | 必需 | 无 | `results/` 下的评估 ID，或一个真实存在的评估目录路径。 |
| `--results-dir` | 可选 | `<toolkit>/results` | 评估结果根目录。 |
| `--dataset` | 可选 | `generic_procurement_contract_mvp` | 使用哪个 `datasets/` 下的数据集作为 gold answer。 |
| `--output-dir` | 可选 | `<evaluation>/scoring` | 机器评分输出目录。 |

## 7. machine_score.json 字段解释

`machine_score.json` 用于后续程序读取或汇总。主要字段如下：

| 字段 | 含义 |
| --- | --- |
| `schema_version` | 机器评分结果格式版本。 |
| `evaluation_id` | 被评分的评估结果目录名。 |
| `generated_at` | 评分生成时间。 |
| `inputs` | 本次评分使用的 evaluation directory、dataset directory、gold ontology、aliases、可选 screenshot evidence 路径和可选 Web evidence 路径。 |
| `summary` | 文件发现摘要，包括 task result、ontology、evidence 文件数量和 JSON 加载错误数量。 |
| `schema_validation` | 每个被检查 JSON 的 schema 校验结果。 |
| `gold_comparison` | 输出 ontology 与 gold ontology 的匹配、缺失和覆盖情况。 |
| `evidence_check` | evidence 引用检查结果，包括引用数量、可用引用数量、缺失引用，以及可选 `screenshot_evidence` / `web_evidence` 摘要。 |
| `possible_hallucinations` | 无法通过 gold ontology 或 aliases 匹配的 concept / attribute / relation。 |
| `machine_metrics` | 自动评分核心指标。 |
| `json_load_errors` | 无法解析的 JSON 文件及错误信息。 |
| `human_review` | 人工复核占位字段，默认 `status = pending`。 |
| `notes` | 自动评分解释说明。 |

### 7.1 machine_metrics 指标

| 指标 | 含义 | 如何理解 |
| --- | --- | --- |
| `core_concept_coverage` | 核心概念覆盖率 | 输出命中的核心 concept 数 / gold 核心 concept 数。 |
| `key_attribute_coverage` | 关键属性覆盖率 | 输出命中的关键 required attribute 数 / gold 关键 required attribute 数。 |
| `key_relation_coverage` | 关键关系覆盖率 | 输出命中的 relation 数 / gold relation 数。 |
| `schema_validity_rate` | ontology schema 通过率 | schema 合法 ontology 文件数 / 发现的 ontology 文件数。 |
| `missing_evidence_ref_count` | 缺失 evidence 引用数 | ontology 中引用但无法找到来源的 evidence ref 数量。 |
| `referenced_screenshot_evidence_count` | 已引用截图 evidence 数 | ontology 中引用的 `screen:*` evidence ref 数量；只有可选 screenshot evidence 文件存在时有意义。 |
| `missing_screenshot_evidence_ref_count` | 缺失截图 evidence 引用数 | 引用了 `screen:*` 但未在 screenshot evidence map 中找到的数量。 |
| `web_evidence_enabled` | Web evidence 是否启用 | 数据集中存在 `gold_evidence_map.web.json` 时为 true。 |
| `referenced_web_evidence_count` | 已引用 Web evidence 数 | ontology 中引用的 `web:*` evidence ref 数量；只有可选 Web evidence 文件存在时有意义。 |
| `matched_web_evidence_count` | 命中的 Web evidence 数 | 引用的 `web:*` ref 中能在 Web evidence map 找到的数量。 |
| `missing_web_evidence_ref_count` | 缺失 Web evidence 引用数 | 引用了 `web:*` 但未在 Web evidence map 中找到的数量。 |
| `invalid_web_snapshot_path_count` | 无效 Web snapshot 路径数 | Web evidence map 中 `content_ref` 指向不存在文件的数量。 |
| `possible_hallucinated_concept_count` | 疑似幻觉 concept 数 | 输出中无法匹配 gold/alias 的 concept 数量。 |
| `possible_hallucinated_attribute_count` | 疑似幻觉 attribute 数 | 输出中无法匹配 gold/alias 的 attribute 数量。 |
| `possible_hallucinated_relation_count` | 疑似幻觉 relation 数 | 输出中无法匹配 gold/alias 的 relation 数量。 |

注意：possible hallucinations 只是“未匹配项”，不是最终确认的幻觉。某些合理抽象、命名差异或 gold 缺口也可能被标记，需要人工判断。

## 8. machine_score.md 字段解释

`machine_score.md` 面向操作员阅读。主要部分包括：

| 章节 | 用途 |
| --- | --- |
| `Summary` | 显示 evaluation id、生成时间、发现的 ontology/task result 数量和 schema-valid ontology 数量。 |
| `Coverage` | 展示核心概念、关键属性、关键关系覆盖率。 |
| `Missing Items` | 列出缺失的核心概念、关键属性和关键关系。 |
| `Evidence References` | 展示 evidence 引用检查结果、可选 screenshot evidence 摘要和缺失 evidence ref 明细。 |
| `Possible Hallucinations` | 列出疑似幻觉的 concept、attribute、relation。 |
| `Schema Validation` | 展示每个被检查文件的 schema 校验结果。 |
| `Human Review Fields` | 提醒人工复核仍未完成。 |

建议阅读顺序：

1. 先看 `Summary`，确认脚本确实发现了 ontology 和 task result 文件。
2. 再看 `Schema Validation`，先处理 invalid JSON 或 schema 错误。
3. 再看 `Coverage` 和 `Missing Items`，判断 gold 覆盖是否足够。
4. 再看 `Evidence References`，确认引用是否可追溯。
5. 最后看 `Possible Hallucinations`，人工判断是否是真幻觉。

## 9. 常见错误和排查方法

### 9.1 Evaluation directory not found

现象：脚本提示找不到评估目录。

处理：

1. 确认当前目录是工具包根目录。
2. 确认 `results/<evaluation_id>/` 是否存在。
3. 如果结果目录不在默认 `results/` 下，使用 `--results-dir` 或直接传入目录路径。

### 9.2 JSON 解析失败

现象：`json_load_errors` 不为 0，或 `machine_score.md` 显示 JSON load errors。

处理：

1. 打开对应 JSON 文件。
2. 检查是否有 Markdown 包裹、尾随逗号、注释、未转义换行或中文标点。
3. 先修复 JSON 格式，再重新运行评分。

### 9.3 没有发现 ontology 文件

现象：`ontology_file_count = 0`。

处理：

1. 检查 task result JSON 是否包含 `task_id` 和 `output_artifacts`。
2. 检查 `output_artifacts` 中是否有 `artifact_type = ontology`。
3. 检查 artifact path 是否指向真实存在的 JSON 文件。
4. 如果使用 standalone ontology JSON，确认文件包含 `ontology_id` 和 `concepts`。

### 9.4 schema validation errors 很多

现象：`schema_validation` 中大量 invalid。

处理：

1. 先修复最顶层结构，例如缺少必填字段、字段类型错误。
2. 再修复数组元素内部字段。
3. 不要急着解释 coverage，schema 错误太多时覆盖率可能没有意义。

### 9.5 coverage 很低

现象：`core_concept_coverage`、`key_attribute_coverage` 或 `key_relation_coverage` 明显偏低。

处理：

1. 检查输出 ontology 是否确实缺少这些业务对象。
2. 检查命名是否和 gold/aliases 差异过大。
3. 检查是否选错了 `--dataset`。
4. 记录为人工复核重点，不要直接判定工具失败。

### 9.6 missing evidence refs 很多

现象：`missing_evidence_ref_count` 很高。

处理：

1. 检查 evidence ref 拼写是否和 evidence map、文件路径、表名、字段名一致。
2. 检查输出是否引用了不存在的文件、章节、表或字段。
3. 检查 artifact path 是否使用了评估目录内的相对路径。
4. 记录为证据链问题，优先修复。

### 9.7 possible hallucinations 很多

现象：possible hallucinated concept / attribute / relation 数量很高。

处理：

1. 先确认是否选错 dataset。
2. 检查是否只是命名差异或合理抽象。
3. 对照 `acceptable_aliases.json` 判断是否需要补充 alias。
4. 人工确认后再判定是否为真实幻觉。

### 9.8 缺少 jsonschema 依赖

`score_auto.py` 可以在没有第三方 `jsonschema` 包的情况下运行。若环境安装了 `jsonschema`，脚本会使用它；否则会使用内置的简化校验逻辑。

离线环境通常不需要临时安装依赖。如果确实要安装，请先确认客户环境允许安装 Python 包。

## 10. 离线环境运行注意事项

1. `score_auto.py` 不需要访问外网。
2. 默认只读取本地 `results/`、`datasets/` 和 `schemas/`。
3. 不要把客户敏感数据上传到外部服务。
4. 如果客户环境不能安装依赖，优先使用脚本内置校验逻辑。
5. 如果需要拷贝评估结果到另一台机器，请保持 `results/<evaluation_id>/` 内部相对路径不变。
6. 建议保存原始输出、标准化输出、评分输出和人工复核记录，便于后续审计。

## 11. 低经验操作员检查清单

运行前：

```text
[ ] 我在工具包根目录。
[ ] results/<evaluation_id>/ 存在。
[ ] 我知道本次使用的数据集 id，MVP 默认为 generic_procurement_contract_mvp。
[ ] task result JSON、ontology JSON、evidence JSON 已保存到评估目录。
[ ] task result JSON 中的 output_artifacts 路径指向真实文件。
```

运行命令：

```bash
python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp
```

运行后：

```text
[ ] scoring/machine_score.json 已生成。
[ ] scoring/machine_score.md 已生成。
[ ] machine_score.md 中 ontology_file_count 不是 0。
[ ] schema validation 没有明显大面积错误。
[ ] 已查看 missing core concepts / key attributes / key relations。
[ ] 已查看 missing evidence refs。
[ ] 已查看 possible hallucinations，并标记需要人工确认的条目。
[ ] 已把 machine_score.md、原始输出和 execution_log.md 交给人工复核。
```

## 12. 评分解释边界

自动评分结果应作为“红旗提示”和“结构化检查结果”，不能替代人工业务判断：

- coverage 低，可能表示工具输出缺失，也可能是命名映射或 gold/alias 问题。
- possible hallucinations 是 alias 匹配失败，不等于确认幻觉。
- missing evidence refs 是证据链风险，需要优先排查。
- schema invalid 会影响后续报告和自动处理，应优先修复。
- 人工复核必须结合 raw output、execution log、prompt、工具限制和客户环境。

## 13. A5 收口补充：dry run、安全输出和人工复核

### 13.1 Read-only dry run 命令

`score_auto.py` 当前没有 `--dry-run` 或 `--no-write` 参数。若只想练习或验证，不希望覆盖 `results/<evaluation_id>/scoring/`，请使用 `--output-dir` 写到临时目录：

```bash
python3 scoring/score_auto.py demo_baseline \
  --dataset generic_procurement_contract_mvp \
  --output-dir /tmp/demo_baseline_scoring_dry_run
```

仓库路径含空格或中文字符时，先用引号进入工具包根目录：

```bash
cd "/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit"
python3 scoring/score_auto.py demo_baseline --dataset generic_procurement_contract_mvp --output-dir /tmp/demo_baseline_scoring_dry_run
```

### 13.2 Task result wrapper 要求

固定 Prompt 产生的通常是业务 JSON，例如 ontology 或 profile。为了让 `score_auto.py` 稳定发现结果，建议每个参与评分的任务都额外保存一个 task result wrapper：

```json
{
  "task_id": "task_05_multi_source_fusion",
  "task_name": "Multi Source Fusion",
  "mode": "fixed_prompt",
  "level": "smoke",
  "status": "completed",
  "started_at": "2026-07-03T00:00:00Z",
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
  ]
}
```

`path` 建议使用相对于 `results/<evaluation_id>/` 的路径。不要把 `datasets/*/gold/` 或 `results/demo_baseline/` 放入 task input artifacts。

### 13.3 Evidence ref 命名解释

`missing_evidence_refs` 可能来自三类原因：

1. 输出真的引用了不存在的证据。
2. evidence ref 命名风格与 evidence map 或文件路径不一致。
3. 输出使用了合理但尚未登记到 acceptable aliases / evidence map 的来源名称。

因此，missing evidence ref 是证据链风险，不是自动失败结论。人工复核需要逐条处置：

- `confirmed_missing`：确认没有证据。
- `naming_mismatch`：证据存在但命名不一致。
- `acceptable_after_review`：证据足够，允许通过。
- `needs_fix`：需要修正输出或补充 reference mapping。

### 13.4 Human review 最小要求

自动评分完成后，至少填写：

```text
manual_review/manual_review.md
```

推荐使用：

```text
report_templates/manual_review.template.md
```

人工复核必须给出：

- schema validation 是否接受。
- coverage 是否接受。
- missing evidence refs 处置。
- possible hallucinations 处置。
- human score / grade / decision。
- reviewer notes 和 sign-off。

`human_review.status = pending` 时，最终报告不得给出无约束 `ready` 结论。

