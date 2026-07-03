# customer_profiles

## 用途

`customer_profiles/` 存放客户现场评估配置，包括客户环境、工具、模型、权限、数据源能力和操作员信息。每次评估必须先填写 customer profile，用于确定可用输入、权限限制、降级路径和评分上限。

## 包含内容

- `customer_profile.template.json`：MVP 可用的客户画像模板，兼容 `schemas/customer_profile.schema.json`。
- 后续可增加真实客户 profile、匿名化 profile 和示例 profile。

## 使用步骤

1. 复制模板：

```bash
cp customer_profiles/customer_profile.template.json results/<evaluation_id>/customer_profile.json
```

2. 将 `unknown` 替换为现场真实信息。无法确认的字段保留 `unknown`，不要猜测。
3. 检查 `data_sources`，只列出允许提供给 AI 的输入来源。
4. 检查 `access_constraints`，如实记录网络、文件、命令、数据库、浏览器、图片和导出限制。
5. 检查 `evaluation_scope`，MVP Smoke Test 默认不包含截图和 Web。
6. 保存到 `results/<evaluation_id>/customer_profile.json`。

## 输入

- 客户现场网络环境。
- AI 工具和模型信息。
- 权限边界。
- 可用数据源。
- 操作员信息。

## 输出

- 标准 customer profile。
- 评分上限依据。
- 降级路径依据。
- 报告中的环境和权限说明。

## 使用规范

- 每次评估必须先填写 customer profile。
- 客户敏感信息应尽量使用代号或脱敏字段。
- 权限限制必须如实记录，不能为了评分好看而省略。
- 不得把 `datasets/*/gold/`、`results/demo_baseline/` 或 machine score 作为被测 AI 的输入数据源。
- 中石油等客户只应作为示例 profile，不应污染核心包。
