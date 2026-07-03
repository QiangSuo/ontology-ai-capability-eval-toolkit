# prompts

## 用途

`prompts/` 存放固定提示词和自由模式指南，用于保证测试可重复、可比较，同时允许评估真实交付上限。

## 包含内容

后续可包含：

- fixed prompts：用于横向比较的标准提示词
- free mode guides：自由发挥模式操作指南
- prompt fragments：可复用提示词片段

## 输入

- 测试任务定义
- ontology 输出结构要求
- evidence map 要求
- 降级路径规则

## 输出

- 可复制到客户工具中的标准 prompt
- 自由模式执行和记录规范

## 使用规范

- 固定提示词不得暗示 gold answer。
- 固定模式和自由模式结果必须分开记录。
- prompt 必须要求“只基于提供材料，不得编造”。
- prompt 必须要求输出 evidence、source_ref、confidence、uncertainty 和 conflict。
