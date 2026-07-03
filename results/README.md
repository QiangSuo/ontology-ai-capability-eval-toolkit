# results

## 用途

`results/` 存放每次评估的原始输出、标准化结果、评分结果、人工复核和最终报告。

## 包含内容

每次评估后续建议按如下结构保存：

```text
results/{date}-{customer_code}-{tool_stack}/
  customer_profile.json
  execution_log.md
  raw_outputs/
  normalized_outputs/
  scoring/
  manual_review/
  report/
  artifacts/
```

## 输入

- 操作员执行记录
- AI 工具原始回答
- 标准化 ontology 输出
- evidence map
- 评分结果

## 输出

- 可复盘评估结果包
- 最终评估报告
- 可脱敏沉淀到 benchmark_history 的工具画像

## 使用规范

- 原始输出必须保存，不得只保存整理后的答案。
- 追问记录、失败记录和人工修复必须保存。
- 客户敏感材料不能未经授权带出客户环境。
- 可沉淀的历史结果应先脱敏再进入 `benchmark_history/`。
