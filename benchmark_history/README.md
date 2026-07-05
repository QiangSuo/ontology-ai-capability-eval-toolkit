# benchmark_history

## 用途

`benchmark_history/` 用于长期沉淀工具组合能力画像，支持跨客户、跨工具、跨模型、跨权限环境的比较。

## 包含内容

后续可包含：

- tool profiles
- comparison matrix
- longitudinal records
- 匿名化历史 benchmark
- 推荐使用场景和不推荐使用场景记录

## 已沉淀报告

- [CodeBuddy vs Claude Code 对比报告（2026-07-05）](codebuddy_vs_claude_code_20260705.md)：基于公开资料与本地脱敏 Smoke Test 的工具选型参考。

## 输入

- 脱敏后的评分结果
- 工具组合信息
- customer profile 摘要
- 能力矩阵
- POC 准入结论

## 输出

- 工具组合能力画像
- 横向比较矩阵
- 历史趋势记录
- FDE 内部工具准入参考

## 使用规范

- 默认不保存客户敏感原始数据。
- 只沉淀能力画像、评分、限制和建议。
- 比较时必须同时展示权限边界，不能只比较总分。
- 历史画像应记录评估日期和数据集版本。
