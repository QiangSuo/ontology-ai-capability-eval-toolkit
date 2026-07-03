# MVP 闭环总结（A6）

## 结论

- **Internal Pilot readiness Status：Conditional Go**。
- 本次闭环可作为“内部 MVP / 工具包基线闭环候选”使用，适合在受控条件下做离线 smoke test 和内部试点评估。
- 不应表述为“无条件客户现场 Go”或“完全客户可交付”。原因是 A5 已补齐低经验操作者运行 smoke test 所需的运行手册、输入边界、结果目录约定、`task_result` 包装、dry-run scoring、人工复核门禁和最终报告约定；但 A3 仍有语义 / gold 口径问题待业务或数据负责人确认，demo baseline 也仍处于人工复核 pending 状态。

## 已完成功能清单

- 离线 MVP 数据集：`datasets/generic_procurement_contract_mvp/` 提供虚构采购 / 合同领域材料，包括 `source_code/`、`database/ddl.sql`、`database/sample_data/`、`documents/` 以及隔离给评估方使用的 `gold/` / reference 材料。
- 固定任务提示词：`prompts/tasks/` 提供 Task 00-07，覆盖环境登记、代码抽取、DDL 抽取、样例数据画像、文档抽取、多源融合、Schema 修复、最终报告生成。
- 结构化 Schema：`schemas/` 提供 ontology、evidence、task_result、tool_profile、customer_profile、evaluation_report 等 JSON Schema。
- 自动评分脚本：`scoring/score_auto.py` 支持离线发现任务结果、验证 JSON / Schema、对比 gold、检查 evidence ref、标记 possible hallucination，并输出机器评分结果。
- 操作手册：`operator_guide/README.md` 已提供可执行 smoke-test run sheet、输入矩阵、CSV 切片规则、结果目录约定、Task 00 / 06 处理方式、评分命令、人工复核门禁和失败记录要求。
- 评分说明：`scoring/README.md` 已补充 dry-run 安全输出、wrapper 要求、evidence-ref 解读和最低人工复核要求，并明确 `human_review.status = pending` 阻断无约束 ready 结论。
- 报告模板：`report_templates/` 提供人工复核和最终评估报告模板，支持把机器评分信号、人工判断、风险和结论映射到规范报告。
- Demo baseline：`results/demo_baseline/` 提供可运行示例，用于验证目录结构、包装文件、自动评分和报告流程；该 baseline 是故意不完美样例，不是客户现场 ready 证据。
- 一致性和 dry-run 复盘记录：`docs/MVP_CONSISTENCY_CHECK.md` 与 `docs/DRY_RUN_REVIEW.md` 记录 A3 / A4 / A5 问题状态，其中 A5 修复 A4 blockers，但保留需人工或业务决策的 deferred / mitigated items。

## 当前可评估能力

- 环境接入与日志记录：文件访问、命令执行、网络 / 浏览器 / 数据库 / 图像能力、JSON 稳定性、权限与限制记录。
- 代码理解：从 Java 源码抽取业务概念、属性、关系、事件、规则、动作、状态、角色、权限、别名、映射和 evidence。
- 数据库元数据理解：从 DDL 抽取表、字段、实体、关系、状态、枚举和约束信息。
- 样例数据画像：从 CSV 样例识别状态值、枚举观察、缺失、异常和候选规则，并明确 sample data 不是完整事实来源。
- 文档理解：从中文业务 / 流程 / 政策 Markdown 文档抽取角色、权限、规则、流程和 evidence。
- 多源融合：合并代码、DDL、CSV、文档输出，处理别名、去重、映射、冲突、不确定性、置信度和来源链路。
- 结构化输出与 Schema 修复：检查 JSON 可解析性、Schema 兼容性、必填字段、修复日志和原始业务内容保留。
- Evidence traceability：检查 `source_ref` 是否存在、识别 missing evidence refs、gold / alias unmatched 项和 possible hallucination 候选。
- 操作者流程能力：评估低经验操作者是否能保留 raw / normalized outputs、执行 prompt retry、记录 repair count、保存日志并完成人工复核。
- 最终报告能力：从 task results、machine score 和 human review 生成结构化 `evaluation_report.json`，并可选生成展示型 Markdown 报告。

## 不支持或不能宣称已就绪的能力

- 不支持真实 UI 截图 / 图像理解评估；当前 MVP 没有 screenshot 输入、OCR 约定或 screenshot evidence scoring。
- 不支持 live UI screenshot / OCR 自动评分。
- 不支持递归 live Web crawling、浏览器自动化或网页图算法评分。
- 不支持 dashboard 或交互式报告。
- 不支持行业扩展数据集的广域验证；当前仅覆盖一个虚构采购 / 合同 MVP 数据集。
- 不支持完全自动化最终业务评分、最终 POC 准入或客户现场 Go 决策。
- 不支持自动语义判定所有业务规则、冲突和抽象选择；A3 M-01 至 M-05 仍需业务 / 数据 / gold 口径确认。
- 不覆盖大型企业代码库、生产数据库连接、生产权限流、客户敏感数据处理验证或现场系统集成。

## 标准工作流

1. 阅读 `DESIGN_PRINCIPLES.md`、`CAPABILITY_MODEL.md`、`operator_guide/README.md` 和 `scoring/README.md`，明确 MVP 范围与限制。
2. 使用 Task 00 记录工具、模型、客户环境、权限、输入访问能力和已知限制。
3. 新建 `results/<evaluation_id>/`，不得复用或覆盖 `results/demo_baseline/`。
4. 仅向被评估 AI 提供允许的 MVP 输入：`datasets/generic_procurement_contract_mvp/source_code/`、`database/ddl.sql`、`database/sample_data/`、`documents/` 和必要的数据集说明。
5. 严禁向被评估 AI 提供 `gold/`、acceptable aliases、known conflicts、`results/demo_baseline/`、scoring 输出、A3 / A4 复盘文档或 machine score。
6. 按顺序运行 Task 01-04：代码、DDL、样例数据、文档单源抽取。
7. 运行 Task 05 做多源融合，生成 ontology 和 evidence map。
8. 仅在 JSON / Schema 不合格时运行 Task 06；每个无效输出最多一次修复，修复结果需单独保存并由 wrapper 引用。
9. 保存 raw outputs、normalized JSON artifacts 和 `task_result` wrappers，确保 `score_auto.py` 可发现文件。
10. 从工具包根目录运行自动评分：`python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp`。
11. 若只是练习或不想改写正式目录，使用 `--output-dir /tmp/<evaluation_id>_scoring_dry_run` 做 dry run。
12. 完成人工复核后，再运行 Task 07 / 报告模板生成 `report/evaluation_report.json` 和可选 `report/final_eval_report.md`。

## 输入 / 输出闭环

- 输入边界：被评估 AI 只能看到 source code、DDL、sample CSV、documents 和必要任务提示；gold、reference、demo、scoring、known conflicts 和复盘文档必须留在评估方侧。
- 原始输出：每个任务的模型原始回答保存到 `results/<evaluation_id>/raw_outputs/`。
- 规范化输出：可评分的 ontology、evidence、profile 等 JSON 保存到 `results/<evaluation_id>/normalized_outputs/`。
- Wrapper：每个任务保存 `task_result` wrapper，引用 raw / normalized artifacts，使自动评分能可靠发现输出。
- 自动评分输出：默认写入 `results/<evaluation_id>/scoring/`，或通过 `--output-dir` 写到临时目录。
- 人工复核输出：人工判断、证据缺口处置、possible hallucination 处置、score cap 和 sign-off 保存到 `results/<evaluation_id>/report/` 或 `manual_review/` 约定位置。
- 最终报告：`evaluation_report.json` 是规范结构化报告；`final_eval_report.md` 只是展示层，不应包含 Schema 不支持的自创字段。
- Task 03 只作为样例数据画像，不直接代表完整 ontology；Task 05 才负责把前序输出融合为可评分 ontology / evidence artifacts。
- Task 07 / reporting 必须同时消费 machine score 与 human review，不能只依据机器分数下结论。

## 目录结构

```text
ontology-ai-capability-eval-toolkit/
├── CAPABILITY_MODEL.md
├── DESIGN_PRINCIPLES.md
├── README.md
├── customer_profiles/
├── datasets/
│   └── generic_procurement_contract_mvp/
│       ├── source_code/
│       ├── database/
│       │   ├── ddl.sql
│       │   └── sample_data/
│       ├── documents/
│       └── gold/
├── docs/
│   ├── DRY_RUN_REVIEW.md
│   ├── MVP_CLOSURE_SUMMARY.md
│   ├── MVP_CONSISTENCY_CHECK.md
│   └── PHASED_IMPLEMENTATION_PLAN.md
├── operator_guide/
├── prompts/
│   └── tasks/
├── report_templates/
├── results/
│   └── demo_baseline/
├── schemas/
└── scoring/
    ├── README.md
    └── score_auto.py
```

推荐每次正式评估创建以下运行目录：

```text
results/<evaluation_id>/
├── raw_outputs/
├── normalized_outputs/
├── scoring/
├── report/
└── logs/
```

## 自动评分

- `score_auto.py` 可离线运行，不要求 live network；如安装 `jsonschema` 则使用完整 Schema 校验，否则使用简化 fallback 校验。
- 当前评分能发现 `task_result` wrappers、ontology artifacts 和 evidence artifacts。
- 当前评分覆盖 JSON load errors、Schema validation、alias-aware gold comparison、core concept coverage、key attribute coverage、key relation coverage、evidence-ref checks、possible hallucination candidates 和 human-review placeholders。
- Demo baseline scoring 已验证结构上可运行，能检查 5 个 task result 文件、1 个 ontology 文件和 1 个 evidence map，并产生 `machine_score.json` / `machine_score.md`。
- 自动评分是结构信号、覆盖信号和 red-flag 信号，不是最终业务评分。
- Possible hallucination 表示“机器未匹配 gold / alias 的候选项”，不是已确认幻觉。
- Missing evidence refs 表示 evidence-chain 风险，可能是真缺证据、命名不一致、路径不一致或 gold / scoring 维护问题，需要人工处置。
- `machine_score.md` 的 numerator / denominator 展示增强仍是 deferred；低经验复核者可能需要查看 `machine_score.json` 获得完整细节。
- 当前 Web / screenshot evidence scoring 未实现；未来 B / C 阶段扩展必须保持 MVP baseline 和 `results/demo_baseline/` 兼容。

## 人工复核边界

- 人工复核是外部 readiness claim 的强制门禁；机器评分不能单独支撑客户现场 ready。
- 人工必须判断业务语义正确性、抽象质量、冲突处理质量、证据链充分性、possible hallucination 是否成立、score caps、红线、最终等级和 sign-off。
- `human_review.status = pending` 时，不得输出无约束 `ready` 或客户现场 Go 结论。
- Demo baseline 的 `machine_score.md` 明确显示 human review pending，因此只能作为结构和流程样例，不能作为已通过业务复核的 ready 证据。
- A3 M-01 至 M-05 是业务 / 数据 / gold 语义决策问题，不应由技术文档静默修复或隐藏。
- 对客户现场使用，复核者必须区分真实缺证据、evidence-ref shorthand / naming mismatch、可接受 post-review evidence、以及 gold / scoring 维护缺陷。

## 已知限制

- A3 M-01 至 M-05 仍为 deferred major：CSV 外键遗留引用、`50000` 审批阈值冲突、`1.5%` vs `2%` 发票容差冲突、gold evidence-ref shorthand mismatch、acceptable-alias one-to-many 语义问题。
- A4 / A5 仍保留 `machine_score.md` numerator / denominator 展示增强为 deferred。
- Evidence-ref 命名风格已通过文档缓解，但 gold / scoring 语义尚未完全对齐，missing-evidence 高计数可能包含命名不一致。
- Demo baseline 是故意不完美样例，当前体现包括 61 个 missing evidence references、relation coverage 约 27.91%、一个类似幻觉的预算预留概念、human review pending。
- Gold/reference 文件与输入数据集同仓库共存，若不严格遵守 operator guide，存在泄漏给被评估 AI 的风险。
- 路径包含空格和中文字符，shell 命令需要正确引用；Windows / VDI / 受限客户环境需额外验证。
- `score_auto.py` 没有真正 no-write 模式；dry run 需要用 `--output-dir` 写入临时目录。
- 当前工具包只评估本地 / 离线抽取与报告流程，不验证生产级安全、权限、数据脱敏和现场系统集成。

## Internal Pilot readiness

**Status：Conditional Go**

- Go 范围：内部 MVP closure candidate、受控 internal pilot、离线 smoke test、评估流程演练、报告模板演练。
- Conditional Go 条件：必须使用新 `evaluation_id` 完成一次 clean smoke rehearsal；必须隔离 gold / demo / scoring artifacts；必须完成 manual review；必须在报告中显式列出 A3 deferred issues、A4 / A5 residual issues 和不支持能力。
- No-Go 范围：无人工复核的客户现场交付、无约束 customer-site Go、宣称 screenshot / Web / dashboard / 自动最终业务评分已就绪、把 demo baseline 当作业务通过证据。
- 结论措辞建议：可写“内部试点 Conditional Go”；不可写“fully customer-ready”或“unconstrained ready”。

## 客户现场前置条件

- 将版本标注为 `MVP closure candidate / internal pilot ready with constraints`，不要标注为 fully customer-ready。
- 先用新的非 demo `evaluation_id` 做一次端到端 clean smoke test，并保留 raw outputs、normalized outputs、task_result wrappers、execution log、tool / customer profiles、scoring outputs、manual review 和 final report。
- 准备人工复核者，使用 `report_templates/manual_review.template.md` 完成证据缺口、possible hallucination、score caps、红线和最终结论处置。
- 准备 gold/reference 隔离流程，确保被评估 AI 不会看到 `gold/`、acceptable aliases、known conflicts、demo baseline、machine score 或 A3 / A4 复盘文档。
- 明确客户目标 POC 是否依赖 screenshot、Web、live database、large repo、browser automation 或生产权限；若依赖，必须标记 N/A / Blocked / cap，而不是声称 MVP 已覆盖。
- 验证客户环境能读取允许输入、保存日志和输出、运行 Python / scoring，或准备 no-shell / manual-copy fallback。
- 决定 A3 M-01 至 M-05 的对外口径：作为已知 conflict fixtures 接受，或在外部 rollout 前安排 gold / dataset maintenance。
- 对含空格和中文路径的命令进行现场预演；必要时复制到无空格 ASCII 路径下执行。
- 不上传客户敏感数据、gold/reference artifacts 或评分材料到外部服务，除非客户安全流程明确批准。

## 截图能力前置条件

- 当前 MVP 不需要截图输入；截图评估明确在 MVP 范围外。
- 若未来评估 screenshot / UI 能力，应先创建 `docs/SCREENSHOT_EXTENSION_PLAN.md`，并确保不破坏 MVP baseline。
- 需要新增 screenshot surrogate 或真实图片输入、manifest、可见文本 / OCR 支持、region / text / path evidence 约定和 source_type 规范。
- 需要新增或调整截图任务编号，避免与现有 Task 06 schema repair 和 Task 07 final report 发生冲突。
- 若工具不能看图，只能使用 surrogate / OCR 文本，则 UI 能力应按测试模式标记 N/A / Blocked 或 cap，不能声称真实视觉理解已通过。
- 如果工具只收到 surrogate text 却声称直接看到了视觉证据，应作为红线风险处理。

## Web 能力前置条件

- 当前 MVP 不需要 live Web 或递归 crawling；工具包设计为离线 / 本地执行。
- 若未来评估 Web recursive analysis，应先创建 `docs/WEB_EXTENSION_PLAN.md`，并遵守 `docs/PHASED_IMPLEMENTATION_PLAN.md` 中 MVP、screenshot、Web 分阶段稳定的顺序。
- 需要新增 offline HTML snapshots、sitemap / page manifest、title / URL mapping、DOM / source refs、page-link / process expectations 和 source_ref 约定。
- C 阶段 scoring 应保持最小化：可做 evidence/ref coverage 和 summary，不应声称实现真实 crawler scoring 或图算法评分。
- 若客户工具不能访问 live Web，应使用 offline snapshots / page_map；若也不能处理，则 Web 能力应标为 N/A / Blocked 或按 capability model cap。
- 必须避免 Web 扩展让 `results/demo_baseline/` 或 screenshot baseline 依赖 Web 文件。
