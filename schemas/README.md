# schemas

## 用途

`schemas/` 是后续存放 JSON Schema 和标准数据结构定义的位置，用于约束本体输出、证据链、客户 profile、工具画像、任务结果和评分结果。

## 包含内容

后续可包含：

- ontology schema
- evidence map schema
- customer profile schema
- tool profile schema
- task result schema
- scoring result schema
- capability matrix schema

## 输入

- 能力模型
- 输出结构要求
- 评分和报告需求

## 输出

- 可用于自动校验的 JSON Schema
- schema 使用说明
- 示例数据结构

## 使用规范

- JSON Schema 文件位于本目录根路径，示例文件位于 `examples/`。
- schema 字段使用英文命名，`description` 可使用中文解释业务含义。
- schema 字段应支持证据、来源、置信度、不确定性、冲突和 provenance。
- schema 应保持可自动校验，不在本目录内放置评分脚本。
