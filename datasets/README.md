# datasets

## 用途

`datasets/` 存放标准测试数据集和未来行业扩展数据集，用于评估 AI 工具组合在本体项目场景中的真实产出能力。

## 包含内容

后续可包含：

- 通用企业采购审批与合同履约管理系统数据集
- Level 1 到 Level 4 难度数据
- 行业增强数据集：能源、金融、制造、政务、供应链
- Gold ontology
- Gold evidence map
- Acceptable aliases
- Known conflicts

## 输入

- 业务域蓝图
- 构造的代码、DDL、metadata、样例数据和文档
- 后续截图和 Web 快照

## 输出

- 标准测试输入材料
- 标准答案和证据基准
- 自动评分和人工评分所需的 reference data

## 使用规范

- 数据集应可离线执行。
- MVP 阶段不放真实客户敏感数据。
- Gold answer 不应过死，必须支持合理抽象差异。
- 行业增强包应与通用数据集结构保持一致。
