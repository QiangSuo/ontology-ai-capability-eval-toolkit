# MVP 一致性检查（A3 只读审计汇总）

## 范围

本报告汇总 A3 只读一致性审计结果，覆盖数据集 DDL、样例 CSV、Java 源码、业务文档、README、gold 文件、任务提示词、schemas、自动评分脚本、demo baseline 与报告模板占位说明。主要路径包括：

- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/datasets/generic_procurement_contract_mvp/`
- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/prompts/tasks/`
- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/schemas/`
- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/scoring/score_auto.py`
- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/results/demo_baseline/`
- `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/report_templates/README.md`

## 方法

- 对 DDL、样例 CSV、Java 源码、业务文档、README 与 gold 文件进行互相一致性检查。
- 对 `gold_ontology.json` 与 `gold_evidence_map.json` 做覆盖性、引用完整性、源文件存在性与锚点可定位性检查。
- 对 `acceptable_aliases.json` 与 `known_conflicts.json` 做 canonical id、重复 alias、枚举值、置信度、冲突类型、计数与源文件存在性检查。
- 对任务提示词、schema、自动评分脚本、demo baseline 与报告模板占位说明做接口契约一致性检查。
- 本报告只保留审计结果中有明确证据支持的发现；未添加推测性问题。

## 严重级别定义

- **Blocker**：阻止 MVP 数据集、评分或报告主流程使用，且没有合理绕过方式的问题。
- **Major**：会导致数据加载失败、业务规则冲突、评分/报告链路不可见或关键引用无法解析的问题。
- **Minor**：不会立即阻断主流程，但会造成理解偏差、自动化定位困难、词表/文档不完整或验证歧义的问题。
- **Suggestion**：当前不构成直接缺陷，但可提升稳定性、可维护性或未来自动化程度的改进建议。

## 审计状态说明

- 所有发现的初始状态均为 **Open**。
- 本次汇总只写入本报告文件；A3 审计中被检查的源文件、数据文件、gold 文件、schema、提示词、评分脚本、demo baseline 与模板文件均未被修改。

## Blocker

未发现有证据支持的 Blocker 级问题。

## Major

### M-01 Sample CSV 违反 DDL 中 legacy request 引用的外键约束

- **状态**：Open
- **证据**：DDL 要求 `pc_contract.request_id` 与 `pc_purchase_order.request_id` 引用 `pc_purchase_request.request_id`，位置为 `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/datasets/generic_procurement_contract_mvp/database/ddl.sql:86` 和 `/Users/suoqiang/Desktop/本体项目 AI 工具能力评估工具包/ontology-ai-capability-eval-toolkit/datasets/generic_procurement_contract_mvp/database/ddl.sql:106`。CSV 行在 `pc_contract.csv:7`、`pc_contract.csv:8`、`pc_purchase_order.csv:7`、`pc_purchase_order.csv:8` 引用了 `request_id` 2990 和 2988，但 `pc_purchase_request.csv` 没有对应值。
- **影响**：样例数据无法在不禁用或绕过外键约束的情况下加载到声明 schema 中；本体抽取工具可能推断出断裂的合同/采购订单到采购申请关系，或把有效历史行视为孤儿数据。
- **建议修复**：补充 2988 和 2990 的历史采购申请行；或把这些样例行改为现有 `request_id`；或明确说明这些行是故意不可加载的 legacy 记录，并相应调整 DDL/样例数据范围。

### M-02 财务审批阈值边界在代码与文档/DDL 中不一致

- **状态**：Open
- **证据**：文档说明大于等于 50000 CNY 的申请需要财务审批，位置为 `documents/procurement_process.md:21` 和 `documents/business_rules.md:14`。DDL 注释也说明 PR 金额 `>= 50000` 需要财务经理审批，位置为 `database/ddl.sql:54`。代码使用 `compareTo(50000) > 0`，因此恰好 50000 时返回 `DEPARTMENT_MANAGER`，位置为 `source_code/src/main/java/com/example/procurement/service/ApprovalService.java:10`。
- **影响**：金额恰好为 50000 CNY 的采购申请存在相互矛盾的审批要求。这是行为不一致，而不只是术语差异，会因来源优先级不同产生不同本体规则。
- **建议修复**：确定 canonical 边界。若文档/DDL 正确，将代码条件改为 `>= 50000`；若代码正确，将文档与 DDL 注释改为大于 50000。

### M-03 发票匹配容差在政策与代码中不一致

- **状态**：Open
- **证据**：业务规则与付款政策允许发票差异最高 2%，位置为 `documents/business_rules.md:37` 和 `documents/receipt_invoice_payment_policy.md:35`。代码将 `CODE_MATCH_TOLERANCE_RATE` 定义为 `0.015` 并用于发票匹配，位置为 `source_code/src/main/java/com/example/procurement/service/ReceiptInvoiceMatchingService.java:11` 和 `source_code/src/main/java/com/example/procurement/service/ReceiptInvoiceMatchingService.java:24`。
- **影响**：差异在 1.5% 到 2% 之间的发票会被政策接受但被代码拒绝。多源抽取会得到冲突的业务规则，除非这是作为已知冲突有意保留。
- **建议修复**：统一代码与政策容差；或仅在该数据集有意测试冲突处理时保留两个值，并确保冲突继续记录在 gold/known-conflicts 文件中。

### M-04 gold_ontology 的 evidence_refs 使用无法直接解析到 evidence_map evidence_id 的简写 ID

- **状态**：Open
- **证据**：`gold/gold_ontology.json` 包含 `ddl:pc_purchase_request`、`code:PurchaseRequest`、`doc:procurement_process`、`csv:pc_department`、`documents/*.md`、`database/ddl.sql` 等引用，而 `gold/gold_evidence_map.json` 使用 `db.table.pc_purchase_request`、`code.PurchaseRequest.domain`、`doc.procurement_process.status_flow`、`csv.pc_department.rows` 等具体 `evidence_id`。
- **影响**：如果消费者把 `evidence_refs` 视为指向 evidence map 的外键，很多本体级和概念级引用会解析失败，即使 evidence map 中存在支持证据。
- **建议修复**：将 `evidence_refs` 规范化为 `gold_evidence_map.json` 中的精确 `evidence_id`；或为 `ddl:`、`code:`、`doc:`、`csv:` 前缀明确记录并实现 alias/shorthand 解析层。

### M-05 acceptable_aliases 的 alias 并非一对一，违反文件使用说明

- **状态**：Open
- **证据**：`gold/acceptable_aliases.json` 中有 15 个归一化 alias 字符串映射到多个 canonical id。例如：`requester` 映射到 `concept:employee` 和 `attr:purchase_request.requester_user_id`；`approver` 映射到 `concept:employee` 和 `attr:approval_task.approver_user_id`；`item_description` 映射到 `concept:material` 和 `attr:purchase_request_item.item_description`；`category_code` 映射到 `concept:material` 和 `attr:purchase_request_item.category_code`；`创建采购申请` 映射到 `event:purchase_request_created` 和 `action:create_purchase_request`。
- **影响**：这与文件中 alias 映射到 exactly one canonical_id 的使用说明矛盾。假设一对一解析的评分器或匹配器可能把结果计入错误本体元素，或在概念/属性、事件/动作之间产生非确定行为。
- **建议修复**：让 alias 字符串全局唯一；或显式建模为带上下文/歧义消解规则的 alias，并修改使用说明。事件/动作重复标签可考虑使用时态区分。

### M-06 Task 00 提示词要求的输出形状无法通过引用的 tool profile schema

- **状态**：Open
- **证据**：`prompts/tasks/task_00_environment_check.md:12` 引用 `tool_profile.schema.json` 和 `customer_profile.schema.json`，但 `prompts/tasks/task_00_environment_check.md:46` 开始的 required output block 未要求 `tool_profile.schema.json` 所需的顶层字段：`tool_profile_id`、`tool_name`、`model_name`、`customer_environment`、`capabilities`、`recommended_use_cases`、`not_recommended_use_cases`。demo baseline 将 `tool_profile.json` 单独存储，而不是作为 Task 00 输出。`score_auto.py` 只在 `scoring/score_auto.py:221` 发现包含 `task_id` 和 `output_artifacts` 的 dict 作为 task_result。
- **影响**：按 Task 00 执行的操作者可能产出看似合法的 environment check JSON，但不能按 `tool_profile.schema.json` 或 `customer_profile.schema.json` 校验；同时 `score_auto.py` 也不会把它当成 task_result。
- **建议修复**：将 Task 00 改为明确输出兼容 `tool_profile.schema.json` 的对象，并可选输出 customer_profile；或新增专用 environment_check schema，并让下游评分/报告明确消费该 schema。

### M-07 Schema repair 提示词输出的 wrapper 没有 schema，且对 scoring discovery 不可见

- **状态**：Open
- **证据**：`prompts/tasks/task_06_schema_repair.md:39` 要求顶层对象包含 `repaired_output` 和 `repair_log`，而 `schemas/task_result.schema.json` 要求 `task_id`、`task_name`、`mode`、`status`、`started_at`、`output_artifacts`，`schemas/ontology.schema.json` 要求 `ontology_id`、`title`、`concepts`。`score_auto.py` 只在 `scoring/score_auto.py:221` 通过 `task_id + output_artifacts` 发现 task result，并在 `scoring/score_auto.py:236` 通过 `ontology_id + concepts` 发现 ontology。
- **影响**：合法的 Task 06 输出可能被 `score_auto.py` 忽略，因此修复后的 ontology/evidence artifact 除非被人工抽取到 normalized_outputs 并由单独 task_result 文件引用，否则可能不会被校验或评分。
- **建议修复**：为 repair wrapper 输出增加 schema，并更新 `score_auto.py` discovery 以跟随 `repaired_output`；或要求 Task 06 产出 task_result 记录，其 `output_artifacts` 指向修复后的 ontology/evidence JSON 文件。

### M-08 Final report 提示词与 evaluation_report schema 未对齐 machine_score 输出字段

- **状态**：Open
- **证据**：`prompts/tasks/task_07_final_report_generation.md:17` 引用 `evaluation_report.schema.json`，`prompts/tasks/task_07_final_report_generation.md:45` 开始要求输出结构。该 schema 要求 `customer_profile_ref`、`tool_profile_ref`、`evaluation_period`、`executive_summary`、`capability_results`、`conclusion`。用于报告输入的 `machine_score.json` 则提供 `inputs`、`summary`、`schema_validation`、`gold_comparison`、`evidence_check`、`possible_hallucinations`、`machine_metrics`、`json_load_errors`、`human_review`、`notes`。
- **影响**：报告生成器可能通过 `evaluation_report.schema.json` 校验但遗漏或宽松映射实际 `machine_score` 段落；也可能准确总结 `machine_score` 但因缺少 schema 必填报告字段而校验失败。
- **建议修复**：在 Task 07 和/或 report_templates 中明确记录 `machine_score.json` 字段到 `evaluation_report.schema.json` 字段的映射。

## Minor

### m-01 Dataset README 称不包含 gold/conflict 文件，但实际存在

- **状态**：Open
- **证据**：dataset README 在 `datasets/generic_procurement_contract_mvp/README.md:31` 表示 MVP input bundle 故意不包含 Gold ontology、Gold evidence map、Acceptable aliases file、Known conflicts file 或 Scoring scripts。仓库实际包含 `gold/gold_ontology.json`、`gold/gold_evidence_map.json`、`gold/acceptable_aliases.json`、`gold/known_conflicts.md`。
- **影响**：操作者可能误解哪些文件属于输入、哪些属于 reference/gold artifact。如果 gold 文件被意外包含为源输入，可能污染抽取运行。
- **建议修复**：修改 README，区分 input-only 子集与同目录 reference/gold artifact；或将 gold artifact 移出 dataset input bundle。

### m-02 付款审批角色在文档与代码中不同

- **状态**：Open
- **证据**：付款政策在 `documents/receipt_invoice_payment_policy.md:53` 说明付款审批由 Finance Manager 执行。代码在 `source_code/src/main/java/com/example/procurement/service/PaymentService.java:16` 允许 `FINANCE_MANAGER` 和 `PROCUREMENT_ADMIN`。
- **影响**：角色/权限本体可能遗漏 Procurement Admin 的 override 能力，或相对业务政策夸大该权限。
- **建议修复**：在政策中明确 Procurement Admin 是 override 角色；或如果只有 Finance Manager 应审批付款，则删除代码中的该允许项。

### m-03 合同签署要求只存在于文档，schema/code 字段不支持

- **状态**：Open
- **证据**：业务规则在 `documents/business_rules.md:26` 说明 Contract 不应在双方签署前 active。DDL 合同字段在 `database/ddl.sql:83` 包含法务审批和激活时间，但没有签署状态/日期字段。激活代码在 `source_code/src/main/java/com/example/procurement/service/ContractService.java:23` 只检查法务审批和期限日期。
- **影响**：该规则无法从可用结构化来源验证或执行。除非明确该缺口，本体输出可能 hallucinate 未支持的签署属性。
- **建议修复**：如果这是可执行规则，增加签署字段和激活检查；否则在 dataset/gold evidence 中标注为 document-only business expectation。

### m-04 部分 source_location 是聚合描述而非可直接定位锚点

- **状态**：Open
- **证据**：`gold/gold_evidence_map.json` 中，`code.Supplier.domain` 使用 `class Supplier / isEligibleForAward()`；`doc.business_rules.supplier_contract_po` 使用 `## Supplier Rules; ## Contract Rules; ## Purchase Order Rules`；`doc.glossary.terms` 使用 `Preferred Term table rows`。底层锚点存在于 `source_code/src/main/java/com/example/procurement/domain/Supplier.java` 和相关文档中，但组合字符串不是 literal anchor。
- **影响**：人工可以推断目标章节，但自动校验器或跳转 UI 可能无法精确定位这些 `source_location`。
- **建议修复**：将多锚点 evidence 拆成单独 evidence entry；或增加结构化位置，例如 heading 名称加行号/表格行标识。

### m-05 canonical id 引用内部有效

- **状态**：Open
- **证据**：`gold/acceptable_aliases.json` 中全部 417 个 `canonical_id` 都能解析到 `gold/gold_ontology.json` 中存在的递归 id，覆盖 concept、attr、rel、event、state、rule、action、role、permission。
- **影响**：未发现缺失或过期 canonical id，因此 alias entry 不会因 gold ontology target 缺失而失败。
- **建议修复**：canonical id 存在性无需修改。建议将该检查保留在 CI 或轻量验证脚本中，防止回归。

### m-06 known_conflicts 指向现有源文件且声明计数匹配

- **状态**：Open
- **证据**：`gold/known_conflicts.json` 中所有引用源文件均存在。声明的 `severity_counts`：low=8、medium=4、high=0、critical=0，与 12 个 conflict entry 匹配；所有 `conflict_type` 值均列在 `conflict_types` 中。
- **影响**：冲突文件与数据集源文件结构一致，未发现缺失文件引用或计数漂移。
- **建议修复**：结构上无需修复。若需要更严格验证，可增加自动化 snippet/line anchoring，而不是只依赖 `source_location` 文本。

### m-07 Sample-data 提示词要求非 ontology profile，但引用的 ontology/evidence schema 不匹配该形状

- **状态**：Open
- **证据**：`prompts/tasks/task_03_sample_data_profile.md:36` 要求 `table_profile`、`column_profile`、`candidate_*` 风格输出，`prompts/tasks/task_03_sample_data_profile.md:95` 说明这不是完整 ontology。该提示词在 `prompts/tasks/task_03_sample_data_profile.md:10` 引用的 `evidence.schema.json` 和 `ontology.schema.json` 都未定义 table-profile wrapper。
- **影响**：Task 03 输出预期结构不同于两个引用 schema，使自动 schema validation 语义不清。
- **建议修复**：新增 `sample_data_profile.schema.json`；或说明 Task 03 raw output 不直接做 schema 校验，必须先规范化为 ontology/evidence artifact 再评分。

### m-08 提示词输出文件名与 demo baseline task result 命名不匹配

- **状态**：Open
- **证据**：例如 `prompts/tasks/task_01_code_to_ontology.md:80` 指定 `results/task_01_code_to_ontology.json`，而 demo baseline 使用 `results/demo_baseline/task_01_code_to_ontology_result.json` 作为 task_result wrapper，并使用 `results/demo_baseline/normalized_outputs/ontology_fused_demo.json` 存放 ontology 内容。`score_auto.py` 能发现直接 ontology 文件和 task_result wrapper，但提示词命名未解释 wrapper/normalized split。
- **影响**：操作者可能把模型 ontology JSON 保存到评分框架期望 task_result wrapper 的路径，或遗漏 `output_artifacts`。
- **建议修复**：在每个任务提示词中明确命名输出是 raw model JSON、normalized ontology/evidence JSON，还是 task_result wrapper JSON；使示例与 demo_baseline 约定一致。

## Suggestion

### S-01 状态常量遗漏部分 DDL/文档状态

- **状态**：Open
- **证据**：DDL 在 `database/ddl.sql:112`、`database/ddl.sql:140`、`database/ddl.sql:154` 允许 PO CANCELLED、INVOICE CANCELLED、PAYMENT CANCELLED。收货/付款文档在 `documents/receipt_invoice_payment_policy.md:27` 和 `documents/receipt_invoice_payment_policy.md:47` 包含取消流程。`ProcurementStatus.java` 在 `source_code/src/main/java/com/example/procurement/common/ProcurementStatus.java:18` 未定义 `PO_CANCELLED`、`INVOICE_CANCELLED`、`PAYMENT_CANCELLED` 常量。
- **影响**：这不是直接运行时失败，因为 Java 不一定需要所有枚举式值；但相比 DDL 和文档，代码来源中的状态词表不完整。
- **建议修复**：补充遗漏状态常量；或说明 `ProcurementStatus.java` 只包含 service logic 实际引用的状态。

### S-02 CSV 行 source_location 是真实文件位置，但不是稳定语义引用

- **状态**：Open
- **证据**：`gold/gold_evidence_map.json` 中 CSV evidence entry 对 `database/sample_data/` 下文件使用 `rows 1-6`、`rows 1-10` 等位置。
- **影响**：这些引用指向真实文件，对样例数据可接受；但如果 fixture 被编辑，行范围会漂移，且无法标识支持具体本体项的记录或列。
- **建议修复**：优先使用稳定 key 或记录标识作为 `source_location`，例如 `request_no`、`contract_no`、`payment_no`；或在 evidence 支持属性时增加 columns 字段。

### S-03 report_templates 只是占位说明，未约束 machine_score 消费方式

- **状态**：Open
- **证据**：`report_templates/README.md:9` 说明模板是 future content；`report_templates/README.md:17` 仅列出 scoring results 作为输入，但未命名 `machine_score.json` 字段。生成的 score 文件包含具体段落：`summary`、`schema_validation`、`gold_comparison`、`evidence_check`、`possible_hallucinations`、`machine_metrics`、`human_review`、`notes`。
- **影响**：目前没有硬失败，因为还没有实际模板；但报告生成缺少 key machine-score sections 的标准位置，随着模板增加，评分与最终报告容易漂移。
- **建议修复**：新增模板时，为 `machine_score` 段落设置必需占位符，并定义 score caps、schema validation failures、evidence gaps、hallucination candidates 的最小契约。

## 已知限制

- 未对每条 gold ontology/evidence-map 断言与所有输入源做完整自然语言语义证明；审计重点是覆盖性、引用完整性、锚点存在性与多源一致性。
- 对 `gold/known_conflicts.md` 或 `known_conflicts.json` 中已记录的冲突：当它们构成源间不一致时仍保留为发现；但除非造成加载性或文档清晰度问题，否则不额外判定为意外缺陷。
- 未执行 `score_auto.py`；审计基于文件检查、显式 discovery/validation 逻辑，以及现有 `results/demo_baseline/scoring/machine_score.json` 的输出形状。
- 未使用 JSON Schema validator 对每个 JSON 实例做全量校验；发现基于文件审阅和审计结果提供的证据。
- 仓库不是 git repo，无法通过 git 历史判断审计 artifact 是否近期变更。

## A5 修复状态更新

A5 只处理 Blocker 和 Major，并遵守“不做大规模重构、不扩展截图/Web、不引入新数据集、不重写 gold answer 或评分逻辑”的边界。

### Major 状态

| ID | A5 状态 | 处理说明 |
| --- | --- | --- |
| M-01 | Deferred | CSV 外键与 legacy request 引用涉及样例数据语义和是否保留历史孤儿记录，需要业务/数据集负责人确认；A5 不静默改数据。 |
| M-02 | Deferred | 50000 审批阈值是有意设计的多源冲突候选；A5 不改代码、DDL 或文档语义。 |
| M-03 | Deferred | 1.5% vs 2% 发票容差是有意设计的多源冲突候选；A5 不改代码或政策语义。 |
| M-04 | Deferred | gold ontology evidence_refs 与 evidence_map evidence_id 的简写/精确 ID 问题会影响 gold 语义和评分可比性；A5 不改 gold 文件，改为在 `scoring/README.md` 和 operator guide 中说明 missing evidence refs 需人工处置。 |
| M-05 | Deferred | acceptable_aliases 一对多涉及 alias 语义和匹配策略；A5 不改 gold/aliases，保留为后续 gold-maintenance 任务。 |
| M-06 | Fixed | Task 00 已明确为环境/工具 metadata，不是 ontology 评分任务；`customer_profiles/customer_profile.template.json` 和 `customer_profiles/README.md` 已补充可执行模板与 unknown/unverified 规则。 |
| M-07 | Fixed | Task 06 已补充 repair 保存规则，说明 `repaired_output` wrapper 不会被 `score_auto.py` 自动当作 ontology 发现，必须另存 repaired artifact 并由 task_result wrapper 引用。 |
| M-08 | Fixed | Task 07 已重写为兼容 `evaluation_report.schema.json` 的输出结构，移除 schema 不允许字段、nullable numeric 示例和 ambiguous enum placeholder；`report_templates/README.md` 已补充 machine_score 到报告字段映射。 |

### A5 修改过的相关文件

- `operator_guide/README.md`
- `customer_profiles/README.md`
- `customer_profiles/customer_profile.template.json`
- `datasets/generic_procurement_contract_mvp/README.md`
- `results/README.md`
- `report_templates/README.md`
- `report_templates/manual_review.template.md`
- `report_templates/final_eval_report.template.md`
- `prompts/tasks/task_00_environment_check.md`
- `prompts/tasks/task_01_code_to_ontology.md`
- `prompts/tasks/task_02_ddl_to_ontology.md`
- `prompts/tasks/task_03_sample_data_profile.md`
- `prompts/tasks/task_04_document_to_ontology.md`
- `prompts/tasks/task_05_multi_source_fusion.md`
- `prompts/tasks/task_06_schema_repair.md`
- `prompts/tasks/task_07_final_report_generation.md`
- `scoring/README.md`
- `README.md`
- `results/demo_baseline/report/evaluation_report.json`
- `results/demo_baseline/report/final_eval_report.md`

### A5 后剩余 Major

仍有 5 个 Major 处于 Deferred 状态，原因均为需要业务/数据集/gold 语义决策，不能在 A5 静默修复：M-01 至 M-05。

