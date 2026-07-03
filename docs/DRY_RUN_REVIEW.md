# A4 Dry Run Review

状态：Open  
范围：基于 A4 read-only dry-run 结果，模拟低经验操作员从 README 到最终报告的 8 步流程。本文只记录问题与改进建议，不声明任何修复已完成。

## 结论

整体流程只能部分跑通。熟悉仓库结构的操作员可以手动找到 MVP 数据集、复制任务 Prompt、保存输出并运行 `score_auto.py`；但低经验操作员无法稳定完成端到端 smoke test，因为任务范围、输入切片、输出包装、结果目录、人工复核与最终报告生成之间仍有多处需要自行判断。

最主要风险集中在：

- 缺少可执行的低经验操作员 smoke-test playbook。
- Prompt 输出文件名、结果目录和 `score_auto.py` 发现规则不统一。
- `/gold` 与 demo baseline 位于同一仓库内，容易被误作为输入泄漏给被评估 AI。
- `machine_score.md` 可读但不是最终评分，人工复核与最终报告模板不足。
- `final_eval_report.md` 这个目标产物与当前 Task 07 JSON/report schema 之间没有清晰映射。

## 8 步流程模拟

### 1. 阅读 README

状态：Open / 可部分执行。

操作员可从 `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/README.md` 找到总体流程：读设计与能力文档、填写客户画像、执行 operator guide、保存输出、评分、报告。

问题：README 当前状态存在陈旧描述，例如仍提示 MVP 不创建 JSON Schema 或实际测试数据文件，但仓库中已经存在 schemas、dataset、scoring 与 demo baseline。这会削弱操作员对后续说明的信任。

### 2. 选择数据集

状态：Open / 可部分执行。

操作员可识别 MVP 数据集为：

`/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/datasets/generic_procurement_contract_mvp`

Smoke subset 大致应包含：

- `database/ddl.sql`
- `documents/business_overview.md`
- `documents/procurement_process.md`
- `source_code/.../PurchaseRequestService.java`
- `source_code/.../ApprovalService.java`
- core CSV 的 3-5 行样本

问题：数据集 README 提到 3-5 行 core CSV，但未明确哪些 CSV 是 core、是否包含表头、是否保留行号、如何选择代表性/异常样本。`/gold` 文件实际存在，但文档又说 gold 不包含，低经验操作员可能误把 gold 作为输入。

### 3. 执行 Prompts

状态：Open / 可部分执行。

Task 00-07 的 Prompt 文件都存在，且大多有“给 AI 工具复制使用的完整 prompt”区域。模拟顺序应为：

1. Task 00：环境检查。
2. Task 01-04：分别处理代码、DDL、样本数据、文档。
3. Task 05：融合前序输出。
4. Task 06：仅在 JSON/schema 修复需要时运行。
5. Task 07：在前序输出、修复记录、评分和人工复核都存在后生成最终报告。

问题：Prompt copy boundary 没有机械化的 `COPY FROM HERE / END COPY` 标记；Task 05 中直接列出若干预期冲突，可能提示过强；Task 00 要求模型/环境/网络/JSON 稳定性等信息，低经验操作员未必知道如何获得；Task 03 要求行数和 profiling，但 smoke subset 只给 3-5 行时无法获得全量行数。

### 4. 保存输出

状态：Open / 高风险。

推荐结果结构应统一为：

```text
results/<evaluation_id>/raw_outputs/
results/<evaluation_id>/normalized_outputs/
results/<evaluation_id>/scoring/
results/<evaluation_id>/report/
```

问题：当前约定不统一。Prompt 文件使用 flat path，例如 `results/task_01_code_to_ontology.json`；`results/README.md` 推荐 `results/{date}-{customer_code}-{tool_stack}/raw_outputs/`；`scoring/README.md` 又使用 `results/<evaluation_id>/normalized_outputs/`；demo baseline 的文件名包含 `*_raw.md` 和 `*_result.json`。低经验操作员很可能覆盖 demo、混合不同 run，或保存成带 Markdown fence 的 `.md` 导致 JSON 解析失败。

### 5. 运行评分

状态：Open / demo baseline 可跑通。

针对 demo baseline，以下命令可运行：

```bash
python3 scoring/score_auto.py demo_baseline --dataset generic_procurement_contract_mvp
```

在 read-only dry run 中，应使用临时输出目录避免改写仓库内评分文件：

```bash
python3 scoring/score_auto.py demo_baseline --dataset generic_procurement_contract_mvp --output-dir /tmp/a4_demo_baseline_scoring_dry_run
```

模拟结果显示 scoring 可生成 `machine_score.json` 与 `machine_score.md`，并得到与现有 demo 一致的信号：5 个 task result、1 个 ontology、1 个 evidence、0 个 JSON load error、ontology schema valid、core concept coverage 83.33%、key attribute coverage 83.78%、key relation coverage 27.91%、61 个 missing evidence refs。

问题：默认命令会写入 `results/<evaluation_id>/scoring`，dry-run-safe 的 `--output-dir` 选项不够显眼；`score_auto.py` 没有真正的 `--dry-run`/`--no-write`；固定 Prompt 不直接产出 `task_result` wrapper，score_auto 需要的 discoverable artifact 需要额外手动包装。

### 6. 查看 machine_score.md

状态：Open / 可读但易误解。

`machine_score.md` 能帮助操作员看到 schema validation、coverage、missing items、missing evidence refs、possible hallucinations 与 human review fields。

问题：Markdown 报告只显示百分比和截断列表，不显示所有 denominator；完整细节必须查看 `machine_score.json`。自动分数不是最终业务评分，但百分比标题容易被误读为最终成绩。Possible hallucinations 实际是 unmatched items，需要人工判定，不能直接标记为确认幻觉。

### 7. 填写人工复核

状态：Open / 缺模板。

当前 `machine_score.md` 有 human review placeholders，但缺少人工复核表单、schema、字段说明和 sign-off 流程。低经验操作员不知道如何记录：人工分数、证据引用处置、hallucination adjudication、relation coverage 是否可接受、是否允许 constrained ready。

问题：`scoring/README.md` 提醒自动评分不是最终业务评分，但没有把 human review fields 映射到最终报告 schema。

### 8. 生成 final_eval_report.md

状态：Open / 不能可靠完成。

当前仓库更偏向 Task 07 生成 JSON：`results/task_07_final_report_generation.json`。同时存在 `schemas/evaluation_report.schema.json` 与 example JSON，但没有实际 `final_eval_report.md` 模板，`report_templates/README.md` 仍是 placeholder。

问题：用户目标产物 `final_eval_report.md` 与当前 Task 07 JSON/report schema 不一致；Task 07 skeleton 包含 schema 不允许的字段、nullable numeric、以及容易被照抄的 enum 示例。仅凭 `machine_score.md` 不能生成可信最终报告，因为缺 raw outputs、execution log、failure records、human review、customer/tool profiles 的完整输入。

## 分级问题清单

### Blocker - Open

- 缺少可执行的低经验操作员 playbook：`operator_guide/README.md` 仍是未来内容，无法支撑从 README 到报告的端到端 smoke test。
- 客户画像模板缺失：流程要求先填写 customer profile，但 `customer_profiles/README.md` 仅描述未来模板/示例。
- Smoke subset 未精确定义：未列明 core CSV、表头/行号/抽样规则，低经验操作员无法稳定复制输入。
- Prompt 输出与 scoring 输入不兼容：Prompt 要求保存直接 JSON，scoring 需要 task_result wrapper、output_artifacts 与 normalized artifact path。
- `/gold` 实际存在但文档说未包含：低经验操作员可能把 gold ontology/evidence/aliases/conflicts 提供给被评估 AI。
- `final_eval_report.md` 缺模板与生成规则：现有 Task 07 是 JSON 任务，report_templates 为空，无法可靠产出 Markdown final report。
- Task 07 输出 skeleton 与 `evaluation_report.schema.json` 不一致，直接复制会导致 schema invalid。

### Major - Open

- 结果目录约定冲突：flat `results/task_XX.json`、run folder、`raw_outputs/normalized_outputs/`、demo baseline 命名并存。
- Task 00、Task 06 的输出形态不易被 `score_auto.py` 发现，也不清楚应评分、归档还是仅作为 metadata。
- Task 06 决策规则不清：何时运行、对每个 invalid output 运行还是最后统一运行、修复输出是否替换原文件、no-op artifact 如何保存。
- `machine_score.md` 没有覆盖率 numerator/denominator，长列表被截断，低经验操作员需要打开 JSON 才能完整理解。
- 自动评分含义容易被误解：coverage 和 possible hallucinations 是机器信号，不是最终业务结论。
- 人工复核缺模板和 schema：human score、review notes、evidence disposition、hallucination adjudication 无固定位置。
- gold/evidence 引用风格不统一：task evidence refs、gold evidence map、scoring 可识别 ref 之间存在命名差异，missing refs 可能是命名问题而非真实无证据。
- Task 03 sample data profile 与 ontology/evidence schema 的关系不清，容易造成 schema validation 预期错误。
- 路径包含空格和中文字符，命令示例未充分展示 quote/escape，shell、Windows、VDI 或远程环境容易失败。

### Minor - Open

- Task ID 命名混用：`TASK-00`、`task_00_environment_check.json`、`task_01_code_to_ontology_result.json` 并存，缺映射表。
- 数据集 ID 与人类可读名称并存，低经验操作员可能不知道评分命令应使用 `generic_procurement_contract_mvp`。
- `machine_score.md` 使用英文标题，而 scoring docs 为中文，中文操作员需要 section mapping。
- demo baseline 标注 simulated，但仍可能被误复制为真实 run 输入。
- Task 07 中 `final_report_generation` 文件名与 `report/` 目录中的最终报告概念容易混淆。
- Prompt 要求 legal JSON，但未统一提示不要 Markdown fence、不要前后解释，以及原始输出如何保存。

### Suggestion - Open

- 在每个 Prompt 中增加明确 `COPY FROM HERE` / `END COPY` 标记。
- 在每个 task input section 增加硬警告：不要把 `datasets/generic_procurement_contract_mvp/gold/` 提供给 AI。
- 在 scoring README 增加 read-only dry-run 示例，使用 `--output-dir /tmp/...`。
- 在 `machine_score.md` 增加解释 banner：schema valid、coverage incomplete、evidence refs high-risk、hallucination candidates require human review、human review pending。
- 增加 GUI/no-shell 操作说明，适配只能复制粘贴文件片段的低经验用户。

## 重点风险

### 路径风险 - Open

- 仓库绝对路径包含空格与中文字符：`/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit`。所有 shell 示例都应使用引号。
- 数据集 README 用相对路径说明 `source_code/`、`database/ddl.sql`，但 AI 工具或终端 cwd 不同时容易找错路径。
- 默认 scoring 输出会写回仓库结果目录；read-only dry run 需要显式 `--output-dir`。
- Gold/reference 文件与输入文件同处 dataset 下，必须明确排除。

### 非复制友好 Prompt - Open

- Copy boundary 不够机械化，容易把操作员说明、失败条件或输出文件名说明一起复制给被测 AI。
- Prompt 没有内嵌标准输入清单，Standard Test 文件列表需要操作员自行推断。
- Task 05 强提示若干冲突，可能让 AI 更接近 gold-like answer。
- Task 07 的 skeleton 与 schema 不一致，复制后会产生无效 JSON。

### 命名统一 - Open

需要统一并文档化以下概念：

- `evaluation_id` / run id
- raw output / normalized output / task result wrapper
- ontology JSON / sample data profile JSON / evidence map
- failure record / repair log / repaired output
- machine score / human review / final report
- `task_XX` 文件名与 `TASK-XX` JSON ID
- Markdown `final_eval_report.md` 与 JSON `evaluation_report`

### score_auto 清晰度 - Open

`score_auto.py` 对 demo baseline 可运行，但对新 run 的前提不够清晰：必须先有可发现的 task_result wrapper、ontology/evidence artifacts、相对 artifact path。固定 Prompt 不直接产出这些包装，导致低经验操作员需要自行设计 normalized step。

### Gold/Evidence 充分性 - Open

Gold 文件可用于评分，但必须与生成输入隔离。当前 evidence ref 风格差异导致 61 个 missing evidence refs；这些缺失可能包含真实证据不足，也可能是 ref 命名/归一化不一致。最终报告必须把这类问题标为人工复核项，而不是自动得出 hallucination 结论。

### 低经验操作员卡点 - Open

- 不知道 smoke test 到底包含 Task 00-05、00-07，还是只跑部分任务。
- 不知道哪些 CSV 是 core，也不知道怎么抽 3-5 行。
- 不知道如何保存 raw vs repaired vs normalized 输出。
- 不知道如何把模型 JSON 包成 `task_result.schema.json`。
- 可能误把 `/gold` 或 `results/demo_baseline` 作为输入。
- 可能把 coverage 百分比当成最终评分。
- 可能在 human review 未完成时生成最终结论。

## 优先修复清单

### P0 - Open

1. 增加一页 A4 smoke-test run sheet，明确 Task 00、Task 01-04、Task 05、条件 Task 06、scoring、human review、Task 07/final report 的顺序、输入、输出、停止条件。
2. 增加 smoke input file/path matrix，列出 exact files、CSV slices、是否含 header/row number，并明确排除 `/gold` 与 `/results/demo_baseline`。
3. 统一结果目录规范为 `results/<evaluation_id>/raw_outputs/`、`normalized_outputs/`、`scoring/`、`report/`，并更新所有 Prompt 输出文件说明。
4. 提供每个任务的最小 `task_result` wrapper 模板，以及 raw model JSON 到 `output_artifacts` 的映射示例。
5. 增加真实 `final_eval_report.md` 模板，或统一改名为 schema-valid JSON report，并在 docs 中保持一致。

### P1 - Open

1. 增加 customer_profile/tool_profile 模板和 Task 00 环境检查 worksheet，允许安全填写 unknown。
2. 修正 Task 07 与 `evaluation_report.schema.json` 的字段不一致：移除不允许字段，避免 null numeric，明确 enum。
3. 增加人工复核模板/schema：review status、reviewer、human score/grade、notes、evidence disposition、hallucination adjudication、sign-off。
4. 明确 Task 06 规则：何时运行、每次允许几次 repair、no-op artifact、repair log、repaired output 保存位置。
5. 为 Task 03 增加 `sample_data_profile.schema.json`，或明确其只作为 profile/raw artifact 后续再 normalized。
6. 更新 README 和 dataset README，反映 schemas、dataset、gold、scoring scripts、demo baseline 已存在，并标注 input/reference/demo 边界。

### P2 - Open

1. 在 scoring README 增加 read-only dry-run 命令示例，并说明 `--output-dir` 是当前 dry-run 机制。
2. 给 `machine_score.md` 增加 numerator/denominator，例如 core concepts 10/12、key attributes 62/74、key relations 12/43。
3. 在每个 Prompt 增加 `COPY FROM HERE / END COPY` 标记。
4. 增加带引号的 macOS 绝对路径命令示例，并提供 no-shell 复制粘贴替代流程。
5. 文档化 intentional conflicts：50000 threshold、invoice tolerance 等应保留为冲突/不确定性，不应在抽取阶段手工修正。
6. 在 demo baseline README 中明确当前 demo 会产生 61 个 missing evidence refs，避免操作员以为只有一个明显 broken ref。

## Dry Run 状态

- 8 步主流程：Partially runnable，状态 Open。
- Prompt 执行：Mostly copyable，但低经验执行不顺畅，状态 Open。
- Scoring demo baseline：Runnable with caveat，状态 Open。
- Human review 与 final report：Partially runnable / not reliable，状态 Open。

本次评审为 dry run synthesis，仅记录开放问题和优先级，不表示上述问题已修复。

## A5 修复状态更新

A5 针对 A4 的 Blocker/Major 做了最小可控修复，主要集中在 runbook、路径、模板、prompt 输出说明、人工复核和最终报告契约；未修改 dataset/gold/scoring 核心逻辑。

### Blocker 状态

| A4 Blocker | A5 状态 | 修复说明 |
| --- | --- | --- |
| 缺少可执行低经验 playbook | Fixed | `operator_guide/README.md` 已改为 Smoke Test run sheet，包含任务顺序、输入、输出、停止条件、评分和 report gate。 |
| 客户画像模板缺失 | Fixed | 新增 `customer_profiles/customer_profile.template.json`，并更新 `customer_profiles/README.md`。 |
| Smoke subset 未精确定义 | Fixed | `operator_guide/README.md` 和 dataset README 已列出 DDL、文档、代码和 CSV header + first 5 rows 规则。 |
| Prompt 输出与 scoring 输入不兼容 | Fixed | Task 01-06 已补充 raw output、normalized artifact、task_result wrapper 的保存规则。 |
| `/gold` 实际存在但文档说未包含 | Fixed | README、dataset README 和 operator guide 已明确 input/reference/demo 边界，并禁止把 `/gold` 提供给被评估 AI。 |
| `final_eval_report.md` 缺模板与生成规则 | Fixed | 新增 `report_templates/final_eval_report.template.md`，并明确 `evaluation_report.json` 是 canonical 结构化报告、Markdown 是展示层。 |
| Task 07 skeleton 与 schema 不一致 | Fixed | Task 07 已改为 schema-compatible skeleton，不再输出未定义顶层字段、null numeric 或 ambiguous enum placeholder。 |

### Major 状态

| A4 Major | A5 状态 | 修复说明 |
| --- | --- | --- |
| 结果目录约定冲突 | Fixed | `results/README.md`、operator guide 和 prompts 已统一到 `results/<evaluation_id>/raw_outputs/`、`normalized_outputs/`、`scoring/`、`report/`。 |
| Task 00/06 输出不易被 scoring 发现 | Fixed | Task 00 明确为 metadata；Task 06 明确 repair wrapper 与 repaired artifact 保存和 wrapper 引用规则。 |
| Task 06 决策规则不清 | Fixed | `operator_guide/README.md` 和 Task 06 已说明何时运行、最多 1 次 repair、保存位置和发现方式。 |
| `machine_score.md` 缺 numerator/denominator | Deferred | 需要修改 `score_auto.py` 输出格式，属于 scoring 行为变更；A5 暂不改核心评分逻辑。 |
| 自动评分含义容易误解 | Fixed | `scoring/README.md` 增加 A5 收口补充，强调机器信号、人工复核、possible hallucination 和 missing evidence refs 的解释边界。 |
| 人工复核缺模板/schema | Fixed | 新增 `report_templates/manual_review.template.md`，并在 report templates/operator guide/scoring README 中要求人工复核 gate。 |
| evidence ref 命名风格不统一 | Mitigated | A5 未改 gold/scoring 语义，但在 `scoring/README.md` 中增加 missing evidence refs 的人工处置分类。 |
| Task 03 与 ontology/evidence schema 关系不清 | Fixed | Task 03 已说明它是 sample data profile，不是完整 ontology；需在 Task 05 融合后转化为 ontology/evidence artifact 参与评分。 |
| 路径包含空格和中文字符 | Fixed | `operator_guide/README.md` 和 `scoring/README.md` 已加入带引号命令示例和 `--output-dir` dry-run 示例。 |

### A5 后剩余 Blocker / Major

- Blocker：0。
- Major：1 个 Deferred（`machine_score.md` numerator/denominator，需要后续 scoring 输出增强）。
- Major：1 个 Mitigated（evidence ref 命名风格，需要后续 gold/scoring 语义决策才能彻底关闭）。

