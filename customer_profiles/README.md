# customer_profiles

## 用途

`customer_profiles/` 存放客户现场评估配置，包括客户环境、工具、模型、权限、数据源能力和操作员信息。

## 包含内容

后续可包含：

- customer profile template
- 示例 customer profile
- 当前活跃客户 profile
- 匿名化 profile

## 输入

- 客户现场网络环境
- AI 工具和模型信息
- 权限边界
- 可用数据源
- 操作员信息

## 输出

- 标准 customer profile
- 评分上限依据
- 降级路径依据
- 报告中的环境和权限说明

## 使用规范

- 每次评估必须先填写 customer profile。
- 客户敏感信息应尽量使用代号或脱敏字段。
- 权限限制必须如实记录，不能为了评分好看而省略。
- 中石油等客户只应作为示例 profile，不应污染核心包。
