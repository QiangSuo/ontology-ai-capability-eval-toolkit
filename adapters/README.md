# adapters

## 用途

`adapters/` 存放不同数据源类型的评估任务适配说明。这里的 adapter 不是连接真实系统的程序，而是指导操作员如何把不同数据源交给 AI 工具测试的任务模板。

## 包含内容

后续可包含：

- code adapter：源代码理解任务说明
- database adapter：DDL 和 metadata 任务说明
- sample_data adapter：CSV/Excel 样例数据任务说明
- documents adapter：业务文档和接口文档任务说明
- screenshots adapter：截图理解任务说明
- web_snapshots adapter：离线页面快照任务说明
- multi_source adapter：多源融合任务说明

## 输入

- 数据源类型
- 数据源文件或导出物
- 对应测试任务和 prompt

## 输出

- 操作员输入步骤
- 期望输出格式
- 降级测试方式
- 评分映射说明

## 使用规范

- 每个 adapter 应说明正常路径和降级路径。
- adapter 不应包含客户敏感数据。
- adapter 应与 `operator_guide/` 和 `prompts/` 保持一致。
