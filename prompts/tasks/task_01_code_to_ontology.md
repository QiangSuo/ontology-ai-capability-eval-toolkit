# Task 01: 源代码到本体

## 任务目标

只基于采购合同 MVP 源代码抽取本体草案，识别 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict 和 uncertainty。不得使用 DDL、CSV 或业务文档。

## 输入材料

- `datasets/generic_procurement_contract_mvp/source_code/`
- 重点材料：`domain/`、`service/`、`controller/`、`common/`。
- 可参考 schema：`schemas/ontology.schema.json`。

## 操作员步骤

1. 将源代码目录提供给 AI 工具；不能读目录时，按 domain、service、controller、common 复制粘贴。
2. 要求 AI 只基于代码作答。
3. 优先关注 service 中的业务规则、状态流转和动作。
4. 保存原始输出；若 JSON 不合法，允许一次修复追问。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 源代码到本体抽取任务。请只基于我提供的源代码作答，不要使用 DDL、CSV、业务文档或外部采购合同常识。

【任务目标】
从代码中抽取本体草案，覆盖 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty。

【抽取要求】
1. concept：从模型类、核心业务对象、服务对象中抽取。
2. attribute：从模型字段、DTO 字段、函数参数和关键常量中抽取。
3. relation：从对象引用、`*_id` 字段、服务调用和业务逻辑中抽取。
4. event：从创建、提交、审批、关闭、激活、状态变化等代码逻辑中抽取。
5. rule：从 if/else、校验函数、异常、审批判断、状态流转限制中抽取。
6. action：从 service 方法、API 方法和关键业务函数中抽取。
7. state：从枚举、常量、状态字段、阶段字段中抽取。
8. role / permission：从角色常量、权限判断和审批角色判断中抽取。
9. alias：识别 Supplier/Vendor、Purchase Request/PR、Purchase Order/PO、Goods Receipt/GRN、Payment Request/Payment Application 等命名差异。
10. mapping：将本体元素映射到代码文件、类名、函数名或字段名。
11. conflict / uncertainty：代码内部命名不一致、规则缺失或证据不足时必须记录。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-code-ontology",
  "title": "Procurement Contract MVP Code Ontology Draft",
  "domain": "procurement_contract",
  "concepts": [],
  "attributes": [],
  "relations": [],
  "events": [],
  "rules": [],
  "actions": [],
  "states": [],
  "roles": [],
  "permissions": [],
  "aliases": [],
  "mappings": [],
  "conflicts": [],
  "uncertainties": [],
  "evidence_refs": [],
  "confidence": 0.0,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "source_code"
  }
}

【证据要求】
`evidence_refs` 使用 `code:<file_path>#<class_or_function_or_field>`；不能给行号时至少给文件和符号名。

【不确定性要求】
只从函数名推断业务含义时 confidence 不高于 0.7；状态流转不完整时写入 `uncertainties`。

【禁止事项】
不要补充代码中没有出现的字段、状态、审批规则或权限矩阵。
```

## 输出文件名

`results/task_01_code_to_ontology.json`

## 输出格式

- 单个合法 JSON 对象。
- 尽量兼容 `schemas/ontology.schema.json`。
- 字段名使用英文。

## 证据链要求

- 每个核心 concept、attribute、relation、rule、action 应有 `code:*` 证据。
- 关键规则必须追溯到函数、条件判断或常量。

## 不确定性表达要求

- 对只有命名线索、缺少字段定义、状态机不完整的内容写入 `uncertainties`。
- 证据较弱时降低 `confidence`。

## 禁止幻觉要求

- 不得使用 DDL、CSV、业务文档信息。
- 不得补齐未出现的采购合同标准对象。
- 不得自行创造权限矩阵。

## 允许追问次数

最多 1 次。只允许追问缺失代码文件或无法读取的关键模块。

## 常见失败情况

- 混入非代码来源信息。
- 没有 evidence_refs。
- 把 service 方法全部误作 concept。
- 漏掉状态机、审批规则或权限判断。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-01",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | used_wrong_source | hallucination | incomplete_extraction | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_01_code_to_ontology_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

