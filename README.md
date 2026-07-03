# 本体项目 AI 工具能力评估工具包

`ontology-ai-capability-eval-toolkit` 是一套面向 FDE 团队的标准化评估工具包，用于在客户内网现场评估“客户环境 + AI 编码工具 + 底层大模型 + 权限边界 + 可用数据源 + 操作人员 + 标准任务包”这一完整组合，是否足以支撑本体项目交付。

## 它是什么

- 本体项目 AI 工具能力评估工具包。
- 客户现场 AI 能力准入评估工具。
- FDE 团队判断客户内网 AI 工具组合是否可支撑本体交付的标准方法。
- 可复用、可配置、可离线执行、可横向比较的测试框架。
- 面向真实交付可用性，而不是泛泛聊天、代码补全或单模型排名。

## 它不是什么

- 不是单一客户 POC 测试包。
- 不是专属测试包。
- 不是单纯模型 benchmark。
- 不是单纯 AI 编码工具评测。
- 不是学术型本体评测集。
- 不是只看问答质量的提示词题库。

## 被测对象

每次评估的对象不是单独模型或单独工具，而是完整工具组合：

```text
客户环境 + AI 工具 + 底层模型 + 权限边界 + 数据源能力 + 操作人员能力 + 标准任务包
```

评估结论必须绑定该组合，不应外推为某个模型或工具品牌的绝对能力。

## 目录概览

```text
ontology-ai-capability-eval-toolkit/
  core/                通用能力模型、任务协议、评分规则和核心方法论
  datasets/            标准测试数据集和未来行业扩展数据集
  adapters/            不同数据源类型的评估任务适配说明
  prompts/             固定提示词和自由模式提示词规范
  schemas/             后续 JSON Schema 与数据结构定义的位置
  scoring/             评分规则、人工评分表和后续评分脚本的位置
  operator_guide/      低经验操作员现场执行手册
  report_templates/    标准评估报告、能力矩阵和技术附录模板
  customer_profiles/   客户现场工具、模型、权限和环境配置
  results/             每次现场评估的原始输出、日志和报告
  benchmark_history/   长期沉淀的工具组合能力画像
  tools/               后续辅助工具、转换器和报告生成器
  docs/                补充设计文档、术语表和决策记录
```

## MVP 范围

MVP 阶段只覆盖：

- 一个通用企业采购审批与合同履约管理系统数据集。
- 四类输入：源代码、DDL、样例数据、业务/接口文档。
- Smoke Test 与 Standard Test。
- 基础本体输出结构、证据链结构、评分规则、报告模板和操作手册。

MVP 阶段暂不创建：

- 评分脚本实现。
- JSON Schema 文件。
- 实际测试数据集文件。
- 截图/Web/行业增强数据集。
- Dashboard。

## 使用流程

1. 阅读 `DESIGN_PRINCIPLES.md`，确认工具包边界。
2. 阅读 `CAPABILITY_MODEL.md`，理解能力域和等级。
3. 按 `customer_profiles/README.md` 填写客户现场 profile。
4. 按 `operator_guide/README.md` 执行 Smoke Test 或 Standard Test。
5. 将原始输出和日志保存到 `results/`。
6. 按 `scoring/README.md` 完成自动评分和人工评分。
7. 使用 `report_templates/` 生成标准评估报告。
8. 将脱敏后的工具画像沉淀到 `benchmark_history/`。

## 当前状态

当前仓库只包含项目基础目录和核心文档骨架；尚未包含评分脚本、测试数据和 JSON Schema。
