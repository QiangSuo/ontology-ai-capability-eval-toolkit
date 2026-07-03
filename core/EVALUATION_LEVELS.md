# Evaluation Levels

## 1. 目标

本文件定义工具包的三层评估级别：Smoke Test、Standard Test、Deep Agentic Test。不同级别对应不同评估深度、耗时、输入材料、输出要求和准入判断用途。

## 2. 总览

| 级别 | 建议耗时 | 目标 | 适用场景 | 输出结论 |
|---|---:|---|---|---|
| Smoke Test | 1-2 小时 | 快速判断基本可用性。 | 客户现场初筛、工具组合快速准入。 | 是否值得进入 Standard Test。 |
| Standard Test | 0.5-1 天 | 判断是否能承担真实 POC 的部分工作。 | POC 前准入评估。 | 是否可进入真实 POC，以及适用范围。 |
| Deep Agentic Test | 1-3 天 | 判断是否接近 Claude Code/Codex 自动化流水线能力。 | 关键客户、长期平台选型、复杂项目。 | 是否可作为主力自动化交付工具。 |

## 3. Smoke Test

### 3.1 目标

Smoke Test 用于快速回答：这套客户内网 AI 工具组合是否具备本体项目评估的最低可用性。

### 3.2 输入范围

MVP Smoke Test 输入包括：

- customer profile。
- 小型 DDL。
- 一份中文业务说明文档。
- 少量样例数据。
- 小型多源融合材料。
- 幻觉红线测试材料。

### 3.3 标准任务

| 任务编号 | 任务名称 | 核心目标 | 主要输出 |
|---|---|---|---|
| ST-00 | 环境能力登记 | 判断工具权限和降级路径。 | environment capability 记录。 |
| ST-01 | DDL 到本体草案 | 测数据库结构理解和结构化输出。 | ontology_from_ddl。 |
| ST-02 | 文档到规则和流程 | 测中文文档理解。 | ontology_from_doc。 |
| ST-03 | 多源小融合 | 测基本融合和证据引用。 | merged_ontology_smoke。 |
| ST-04 | 幻觉红线测试 | 测缺失信息和冲突下的幻觉控制。 | hallucination_check。 |

### 3.4 输出要求

Smoke Test 必须输出：

- customer profile 初版。
- 每个任务的 raw output。
- 每个任务的 normalized output 或失败记录。
- execution log。
- 初步能力矩阵。
- 红线失败记录。
- 是否进入 Standard Test 的建议。

### 3.5 通过标准

建议同时满足：

- 没有 Critical 红线。
- 结构化输出能力不低于 C+。
- 数据库 Metadata 理解能力不低于 B-。
- 文档理解能力不低于 B-。
- 幻觉控制能力不低于 B-。
- 操作员能保存完整日志和原始输出。

### 3.6 失败处理

若 Smoke Test 失败，应判断原因：

- 工具能力不足：建议不进入 Standard Test。
- 权限不足：要求客户补充文件、DDL、文档或导出权限后重测。
- 操作流程不清：修订 operator playbook 后重测。
- 数据输入方式受限：进入降级路径并设置评分上限。

## 4. Standard Test

### 4.1 目标

Standard Test 用于判断客户工具组合是否可以承担真实 POC 中的一部分本体建设工作。

### 4.2 输入范围

MVP Standard Test 输入包括：

- 源代码。
- DDL。
- metadata JSON。
- 样例数据 CSV。
- 业务说明文档。
- API 文档。
- Gold answer 和 aliases 仅用于评分，不提供给被测工具。

### 4.3 标准任务

| 任务编号 | 任务名称 | 核心目标 | 主要输出 |
|---|---|---|---|
| STD-01 | 代码模块理解 | 从代码识别业务对象、接口、流程、规则。 | code_ontology。 |
| STD-02 | DB metadata 理解 | 从 DDL/metadata 识别实体、字段、关系。 | db_ontology。 |
| STD-03 | 样例数据语义分析 | 识别枚举、状态、异常和规则候选。 | sample_insights。 |
| STD-04 | 文档规则抽取 | 抽取规则、角色、状态、权限。 | doc_ontology。 |
| STD-05 | 多源融合 | 合并多源本体草案。 | merged_ontology。 |
| STD-06 | 冲突识别 | 识别多源不一致和缺口。 | conflicts。 |
| STD-07 | Evidence map 生成 | 为本体元素补充证据链。 | evidence_map。 |
| STD-08 | JSON 修复与稳定性 | 检查结构化输出稳定性。 | validated_ontology。 |
| STD-09 | 操作员复现测试 | 验证低经验人员可执行性。 | execution_log 和复现记录。 |

### 4.4 输出要求

Standard Test 必须输出：

- 完整 customer profile。
- 所有任务 raw outputs。
- normalized outputs。
- 自动评分结果。
- 人工评分表。
- human effort metrics。
- capability matrix。
- redline report。
- POC 准入建议。

### 4.5 通过标准

进入真实 POC 的建议门槛详见 `ENTRY_CRITERIA.md`。Standard Test 通常应满足：

- 综合等级不低于 B-。
- Critical 红线为 0。
- 数据库 Metadata 理解能力不低于 B。
- 结构化输出能力不低于 B。
- 证据链能力不低于 B-。
- 人机协同成本 HEI 不高于 2。

### 4.6 失败处理

若 Standard Test 失败，应输出明确策略：

- 可作为辅助工具。
- 只能局部使用。
- 需要 FDE 核心团队看护。
- 需要客户补充权限或更强模型。
- 不建议进入真实 POC。

## 5. Deep Agentic Test

### 5.1 目标

Deep Agentic Test 用于判断工具组合是否具备接近 Claude Code/Codex 的自动化交付流水线能力。

### 5.2 输入范围

V2 Deep Agentic Test 输入包括：

- Level 3/4 混乱数据集。
- 多目录代码。
- 大量文档。
- 截图和 Web 快照。
- 旧 ontology 与变更材料。
- 冲突和缺失材料。

### 5.3 标准任务

| 任务编号 | 任务名称 | 核心目标 | 主要输出 |
|---|---|---|---|
| DAT-01 | 端到端本体生成流水线 | 从完整测试包生成本体、证据和冲突记录。 | final_ontology。 |
| DAT-02 | 多源冲突与修订 | 识别复杂冲突并提出修订策略。 | conflict_resolution_plan。 |
| DAT-03 | 长上下文/分片能力 | 分片处理大材料并保持全局一致。 | chunk_summaries 和 global_ontology。 |
| DAT-04 | 变更影响分析 | 基于新材料更新旧本体。 | ontology_delta。 |
| DAT-05 | 人机协同交付模拟 | 记录真实交付成本和可复现性。 | delivery_simulation_report。 |

### 5.4 输出要求

- 分阶段计划。
- 中间产物。
- 最终本体。
- evidence map。
- conflict list。
- change impact。
- 自检和修复记录。
- 人机协同成本报告。

### 5.5 通过标准

若工具要被认定为可作为主力自动化交付工具，建议满足：

- Deep Agentic Test 综合不低于 B+。
- Agentic 交付能力不低于 B+。
- 多源融合能力不低于 B+。
- 证据链能力不低于 B。
- Critical 红线为 0。
- HEI 不高于 2。

## 6. 固定模式与自由模式

每个级别可分为：

- 固定提示词模式：用于横向比较。
- 自由发挥模式：用于评估真实交付上限。

记录要求：

- 两种模式分别保存 raw output。
- 两种模式分别评分。
- 报告中展示分数差异和额外人工成本。
- 自由模式不能覆盖固定模式红线。

## 7. 级别升级规则

| 当前结果 | 下一步 |
|---|---|
| Smoke Test B- 以上且无 Critical 红线 | 可进入 Standard Test。 |
| Smoke Test C 或以下 | 先补权限、换工具或缩小范围后重测。 |
| Standard Test B- 以上且满足准入门槛 | 可进入有限范围真实 POC。 |
| Standard Test B+ 以上且 HEI <= 2 | 可作为 POC 辅助主力。 |
| Standard Test C 或以下 | 不建议进入真实 POC 主流程。 |
| Deep Agentic Test B+ 以上 | 可评估作为主力自动化流水线。 |

## 8. 阶段性裁剪规则

MVP 阶段：

- 必测 Smoke Test。
- 必测 Standard Test。
- 暂不要求 Deep Agentic Test。
- UI/Web 可标 N/A，但报告必须说明风险。

V1 阶段：

- 增加 UI/Web。
- 增加 Level 3/4 数据。
- 增加行业包。

V2 阶段：

- 增加 Deep Agentic Test。
- 增加变更影响分析。
- 增加跨客户对比和操作员认证。
