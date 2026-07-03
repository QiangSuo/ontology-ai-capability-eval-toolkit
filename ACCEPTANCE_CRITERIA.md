# Acceptance Criteria

## 1. 项目骨架验收标准

当前阶段完成后，应满足：

- 已创建 `ontology-ai-capability-eval-toolkit/` 项目根目录。
- 已创建核心目录：`core/`、`datasets/`、`adapters/`、`prompts/`、`schemas/`、`scoring/`、`operator_guide/`、`report_templates/`、`customer_profiles/`、`results/`、`benchmark_history/`、`tools/`、`docs/`。
- 每个核心目录都有 `README.md`。
- 根目录包含核心文档：`README.md`、`IMPLEMENTATION_PLAN.md`、`TASK_BREAKDOWN.md`、`CAPABILITY_MODEL.md`、`DESIGN_PRINCIPLES.md`、`ACCEPTANCE_CRITERIA.md`、`ROADMAP.md`。
- 文档均使用中文。
- 当前阶段不包含评分脚本、测试数据、JSON Schema 或过多空文件。

## 2. MVP 验收标准

MVP 完成后，应满足：

- 能让低经验操作员在 1-2 小时内完成 Smoke Test。
- 能让操作员在 0.5-1 天内完成 Standard Test。
- 能覆盖源代码、DDL、样例数据、文档四类输入。
- 能输出标准化本体草案和证据链结构。
- 能完成基础 schema 合规检查、gold 对比、evidence 检查和幻觉检查。
- 能生成能力矩阵和标准评估报告。
- 能给出是否适合进入真实 POC 的明确建议。
- 能完整保存原始输出、操作日志、评分结果和报告。

## 3. Smoke Test 验收标准

Smoke Test 应满足：

- 总耗时控制在 1-2 小时。
- 至少覆盖环境能力、DDL 理解、文档理解、多源小融合和幻觉红线测试。
- 输出文件命名统一。
- 有明确通过标准和红线失败条件。
- 能快速判断工具组合是否具备基础可用性。

## 4. Standard Test 验收标准

Standard Test 应满足：

- 总耗时控制在 0.5-1 天。
- 覆盖代码理解、数据库 metadata、样例数据、文档、多源融合、冲突识别、证据链、结构化输出和操作员复现。
- 每个任务有独立评分结果。
- 结果可汇总为能力矩阵。

## 5. 准入门槛

进入真实客户 POC 前，建议满足：

- Smoke Test 不低于 B-。
- Standard Test 综合不低于 B-。
- 数据库 Metadata 理解能力不低于 B。
- 代码理解能力不低于 B-。
- 结构化输出能力不低于 B。
- 证据链与可追溯能力不低于 B-。
- 严重幻觉红线测试为 0。
- 低经验操作员可以完成标准流程。
- 人工干预成本不高于 2。

## 6. 红线一票否决项

出现以下情况，不得作为主力工具进入真实 POC：

- 严重编造不存在的表、字段、代码、规则。
- 引用不存在来源作为证据。
- 多轮后仍无法输出可解析结构化结果。
- 无法保存原始输出和日志，评估不可复盘。
- 操作员无法按手册完成基础任务。
- 对明确冲突强行给出无证据结论。
- 工具输出存在无法控制的敏感数据外泄风险。
