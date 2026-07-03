# scoring

## 用途

`scoring/` 存放评分规则、人工评分表和后续评分脚本。评分体系必须结合自动评分与人工评分，避免只靠精确匹配判断本体质量。

## 包含内容

后续可包含：

- 自动评分规则说明
- schema validation 脚本
- gold 对比评分脚本
- evidence 检查脚本
- hallucination 检查脚本
- 人工评分表
- 校准样例

## 输入

- 模型原始输出
- 标准化 ontology 输出
- evidence map
- gold ontology
- aliases
- known conflicts
- customer profile

## 输出

- 自动评分结果
- 人工评分表
- 红线失败项
- 能力矩阵输入

## 使用规范

- 当前阶段不创建评分脚本。
- 自动评分不能替代人工业务判断。
- 红线失败项优先于总分。
- 评分应支持 aliases、partial credit 和不确定性表达。
