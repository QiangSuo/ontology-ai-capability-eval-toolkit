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
  schemas/             JSON Schema 与数据结构定义
  scoring/             自动评分脚本、评分说明和人工复核边界
  operator_guide/      低经验操作员现场执行手册
  report_templates/    标准评估报告、能力矩阵和技术附录模板
  customer_profiles/   客户现场工具、模型、权限和环境配置
  results/             每次现场评估的原始输出、日志、评分和报告
  benchmark_history/   长期沉淀的工具组合能力画像
  tools/               后续辅助工具、转换器和报告生成器
  docs/                补充设计文档、检查报告和决策记录
```

## MVP 当前范围

MVP 阶段当前覆盖：

- 一个通用企业采购审批与合同履约管理系统数据集。
- 四类输入：源代码、DDL、样例数据、业务文档。
- Task 00-07 固定任务提示词。
- JSON Schema：ontology、evidence、task_result、tool_profile、customer_profile、evaluation_report。
- 自动评分脚本：`scoring/score_auto.py`。
- 示例评估结果：`results/demo_baseline/`。
- MVP 一致性检查和 dry run review 文档。

MVP 阶段暂不覆盖：

- 截图真实图片理解。
- Web 页面递归爬取。
- 行业增强数据集。
- Dashboard。
- 最终业务评分自动化。

## 输入 / Reference / Demo 边界

评估输入只应来自：

- `datasets/generic_procurement_contract_mvp/source_code/`
- `datasets/generic_procurement_contract_mvp/database/ddl.sql`
- `datasets/generic_procurement_contract_mvp/database/sample_data/`
- `datasets/generic_procurement_contract_mvp/documents/`

不得把以下内容提供给被评估 AI 工具：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `scoring/`
- `docs/MVP_CONSISTENCY_CHECK.md`
- `docs/DRY_RUN_REVIEW.md`
- 人工复核表、machine score、gold answer 或 known conflicts

这些文件只供操作员评分、复核、示例学习和项目维护使用。

## 使用流程

1. 阅读 `DESIGN_PRINCIPLES.md`，确认工具包边界。
2. 阅读 `CAPABILITY_MODEL.md`，理解能力域和等级。
3. 按 `customer_profiles/README.md` 填写客户现场 profile。
4. 按 `operator_guide/README.md` 执行 Smoke Test 或 Standard Test。
5. 将原始输出、标准化结果和日志保存到 `results/<evaluation_id>/`。
6. 按 `scoring/README.md` 运行自动评分并完成人工复核。
7. 使用 `report_templates/` 和 Task 07 生成标准评估报告。
8. 将脱敏后的工具画像沉淀到 `benchmark_history/`。

## 快速 Smoke Test 路径

```text
1. 建立 results/<evaluation_id>/
2. 执行 Task 00 环境检查
3. 执行 Task 01-04 单源抽取
4. 执行 Task 05 多源融合
5. 必要时执行 Task 06 schema repair
6. 运行 python3 scoring/score_auto.py <evaluation_id> --dataset generic_procurement_contract_mvp
7. 完成人工复核
8. 生成 report/evaluation_report.json 和可选 final_eval_report.md
```

详细步骤见 `operator_guide/README.md`。

## 当前状态

当前仓库已经包含 MVP 基线所需的核心目录、数据集、schemas、prompts、自动评分脚本、demo baseline、A3 一致性检查和 A4 dry run review。下一步应根据 A3/A4 中的 Blocker/Major 做最小收口修复，然后生成 MVP closure summary。
