# operator_guide

## 用途

`operator_guide/` 存放低经验操作员现场执行手册，要求 checklist 化，确保不熟悉本体方法论的交付人员也能按步骤完成评估。

## 包含内容

后续可包含：

- Operator Playbook
- Smoke Test checklist
- Standard Test checklist
- 降级路径说明
- 失败记录规范
- 输出文件命名规则
- 异常上报流程

## 输入

- 测试任务定义
- customer profile
- prompts
- 评估数据集

## 输出

- execution log
- 原始模型输出
- 标准化结果
- 失败记录
- 人工评分输入

## 使用规范

- 每一步必须明确输入、动作和输出。
- 允许追问和禁止追问的场景必须写清楚。
- 任何失败、超时、工具限制和人工介入都必须记录。
- 不得把人工补写结果伪装为模型输出。
