# Task Breakdown

## 1. 工作流划分

项目拆成 6 条工作流：

- A. 项目骨架与方法论文档
- B. Schema 与标准数据结构
- C. 测试数据集与 Gold Answer
- D. 测试任务与 Prompt
- E. 评分体系与报告体系
- F. 操作员手册、客户 Profile、Benchmark 沉淀

## 2. 推荐任务总表

| Task ID | 阶段 | 任务名称 | 目标 | 主要输出 |
|---|---|---|---|---|
| T00 | MVP | 固化项目边界与术语 | 防止项目变成单客户 POC 或模型评测 | README、术语表 |
| T01 | MVP | 定义总体目录结构 | 明确工具包工程结构 | 目录结构说明 |
| T02 | MVP | 编写能力模型 | 定义 15 个能力域和等级 | CAPABILITY_MODEL |
| T03 | MVP | 编写评分总则 | 定义权重、红线、上限规则 | SCORING_RUBRIC |
| T04 | MVP | 设计 customer profile schema | 标准化客户环境和权限记录 | customer profile schema |
| T05 | MVP | 设计 tool profile schema | 标准化工具组合画像 | tool profile schema |
| T06 | MVP | 设计 ontology schema | 固化本体输出结构 | ontology schema |
| T07 | MVP | 设计 evidence map schema | 固化证据链结构 | evidence map schema |
| T08 | MVP | 设计 task result schema | 标准化任务执行结果 | task result schema |
| T09 | MVP | 设计 scoring result schema | 标准化评分输出 | scoring result schema |
| T10 | MVP | 设计通用采购业务域 | 定义 MVP 数据集业务范围 | 业务蓝图 |
| T11 | MVP | 构造 Level 1 数据集 | 简单清晰数据，用于初筛 | Level 1 测试包 |
| T12 | MVP | 构造 Level 2 数据集 | 多模块、多表关联，用于标准测试 | Level 2 测试包 |
| T13 | MVP | 编写 Gold Ontology | 为数据集提供参考答案 | gold ontology |
| T14 | MVP | 编写 Gold Evidence Map | 为评分提供证据基准 | gold evidence map |
| T15 | MVP | 编写 aliases 与 known conflicts | 支持宽松评分和冲突测试 | aliases、known conflicts |
| T16 | MVP | 设计 Smoke Test 任务 | 支持 1-2 小时快速评估 | ST 任务定义 |
| T17 | MVP | 设计 Standard Test 任务 | 支持 0.5-1 天标准评估 | STD 任务定义 |
| T18 | MVP | 编写固定提示词 | 保证横向比较一致性 | fixed prompts |
| T19 | MVP | 编写自由模式指南 | 评估真实交付上限 | free mode protocol |
| T20 | MVP | 设计自动评分规则 | 明确脚本应如何评分 | scoring spec |
| T21 | MVP | 实现 schema validation 评分 | 检查 JSON 合规性 | validation script |
| T22 | MVP | 实现 gold 对比评分 | 计算召回和匹配 | recall scoring scripts |
| T23 | MVP | 实现 evidence 检查 | 检查 source_ref 合法性 | evidence scoring script |
| T24 | MVP | 实现 hallucination 检查 | 识别编造字段和来源 | hallucination script |
| T25 | MVP | 设计人工评分表 | 支持业务质量人工复核 | manual review form |
| T26 | MVP | 设计能力矩阵模板 | 汇总各能力域评分 | capability matrix template |
| T27 | MVP | 设计最终报告模板 | 标准化客户现场评估报告 | report template |
| T28 | MVP | 编写 Operator Playbook | 让低经验人员能执行 | OPERATOR_PLAYBOOK |
| T29 | MVP | 编写 Customer Profile Template | 让现场登记工具和权限 | profile template |
| T30 | MVP | 做 MVP 试运行 | 用 1-2 个工具组合验证流程 | pilot result package |
| T31 | MVP | 校准评分标准 | 根据试运行修正权重和阈值 | calibrated rubric |
| T32 | V1 | 增加截图数据集 | 测 UI / 截图理解能力 | screenshot dataset |
| T33 | V1 | 增加 Web 快照数据集 | 测页面递归分析能力 | web snapshot dataset |
| T34 | V1 | 增加 Level 3/4 混乱数据 | 模拟真实企业系统复杂性 | advanced datasets |
| T35 | V1 | 增加行业增强包 | 能源、金融、制造、政务、供应链 | industry datasets |
| T36 | V1 | 建立 benchmark history | 沉淀工具组合能力画像 | benchmark storage format |
| T37 | V1 | 增强报告生成 | 自动汇总能力矩阵与建议 | report generation flow |
| T38 | V2 | 设计 Deep Agentic Test | 评估自动化流水线能力 | DAT 任务包 |
| T39 | V2 | 增加变更影响测试 | 测本体迭代维护能力 | change impact task |
| T40 | V2 | 建立跨客户对比 dashboard | 长期比较工具能力趋势 | dashboard |
| T41 | V2 | 增加本体质量高级评估 | 抽象层级、一致性、可维护性 | advanced metrics |
| T42 | V2 | 建立操作员培训与认证 | 降低执行偏差 | training pack |

## 3. MVP 必须完成的任务

MVP 必须完成 T00 到 T31。其中当前首次实现只完成基础目录与核心文档骨架，不创建评分脚本、测试数据和 JSON Schema 文件。

## 4. V1 任务

V1 包括 T32 到 T37，目标是从“可初筛”升级为“可真实客户现场多场景使用”。

## 5. V2 任务

V2 包括 T38 到 T42，目标是从“评估包”升级为“长期标准化能力平台”。

## 6. 推荐执行顺序

1. T00 项目边界与术语
2. T01 总体目录结构
3. T02 能力模型
4. T03 评分总则
5. T06 ontology schema 设计
6. T07 evidence map schema 设计
7. T04 customer profile schema
8. T05 tool profile schema
9. T08 task result schema
10. T09 scoring result schema
11. T10 通用采购业务域蓝图
12. T11 Level 1 数据集
13. T12 Level 2 数据集
14. T13 Gold Ontology
15. T14 Gold Evidence Map
16. T15 aliases 与 known conflicts
17. T16 Smoke Test 任务
18. T17 Standard Test 任务
19. T18 固定提示词
20. T19 自由模式指南
21. T20 自动评分规则规格
22. T21-T24 评分脚本
23. T25 人工评分表
24. T26 能力矩阵模板
25. T27 报告模板
26. T28 Operator Playbook
27. T29 Customer Profile Template
28. T30 MVP 试运行
29. T31 评分校准

## 7. 可并行任务

- T00 与 T01 可并行。
- T02 与 T03 可在 T00 初稿后并行。
- T04、T05、T08、T09 可在 schema 方向确认后并行。
- T06 与 T07 可并行，但必须统一 evidence 和 source_ref 设计。
- T11 与 T12 可部分并行，但必须共享 T10 业务蓝图。
- T13 与 T14 可并行，但必须共享 ontology element id 规则。
- T16 与 T17 可并行，但复用同一任务字段模板。
- T21、T22、T23、T24 可在 T20 完成后并行。
- T25、T26、T27 可并行。
- T28 与 T29 可并行。

## 8. 必须串行任务

- T00 -> T02 -> T03
- T02/T03 -> T06/T07
- T10 -> T11/T12
- T11/T12 -> T13/T14/T15
- T13/T15 -> T22
- T14 -> T23
- T16/T17 -> T18
- T20 -> T21/T22/T23/T24
- T21-T25 -> T26
- T26 -> T27
- T16-T29 -> T30
- T30 -> T31

## 9. 适合 Claude Code 实现的任务

适合 Claude Code 的任务包括目录结构、文档初稿、schema 初稿、prompt 初稿、评分脚本、报告模板、benchmark 格式、dashboard 基础实现等。

需要人工复核的任务包括能力模型、评分总则、业务域蓝图、gold answer、known conflicts、人工评分表、行业增强包和 Deep Agentic Test。

## 10. 需要 FDE 负责人确认的任务

必须由 FDE 负责人确认：T00、T02、T03、T06、T07、T10、T12、T13、T14、T16、T17、T20、T24、T25、T27、T28、T30、T31、T35、T38。
