# Task 02: DDL 到本体

## 任务目标

只基于采购合同 MVP 数据库 DDL 抽取本体草案，识别表对应的业务概念、列属性、主外键关系、约束、枚举候选、状态和命名差异。不得使用源代码、CSV 或业务文档。

## 输入材料

- `datasets/generic_procurement_contract_mvp/database/ddl.sql`
- 可参考 schema：`schemas/ontology.schema.json`。

## 操作员步骤

1. 将完整 DDL 提供给 AI 工具。
2. 要求 AI 只基于 DDL 抽取。
3. DDL 注释可作为证据，但不能过度扩展为完整流程。
4. 若 JSON 不合法，允许一次修复追问。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP DDL 到本体抽取任务。请只基于我提供的数据库 DDL 作答，不要使用源代码、CSV、业务文档或外部知识。

【任务目标】
从 DDL 中抽取 concept、attribute、relation、state、rule、alias、mapping、conflict、uncertainty。

【抽取要求】
1. concept：通常由核心业务表抽取；纯技术表不要轻易作为业务概念。
2. attribute：由列名、类型、是否必填、默认值、注释抽取。
3. relation：由外键、`*_id` 字段、表间引用和约束抽取。
4. state：从 status、stage、type、role_code、check 约束或注释中抽取。
5. rule：从 NOT NULL、CHECK、UNIQUE、FK、注释中的业务约束抽取。
6. event/action：DDL 证据通常不足，除非表或字段明确表示事件/动作，否则写入 `uncertainties`。
7. alias：识别 `pc_` 表前缀、`pr_number`、`po_number`、`receipt_number` 等缩写或同义命名。
8. mapping：将本体元素映射到表、列、约束。
9. conflict / uncertainty：记录缺失外键、命名歧义、注释与约束不一致。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-ddl-ontology",
  "title": "Procurement Contract MVP DDL Ontology Draft",
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
    "source_system": "database_ddl"
  }
}

【证据要求】
`evidence_refs` 使用 `ddl:ddl.sql#<table>` 或 `ddl:ddl.sql#<table>.<column>`；relation 引用外键或相关 `*_id` 字段。

【不确定性要求】
只有 `*_id` 但无外键时 relation confidence 不高于 0.75；无枚举证据时不要展开状态全集。

【禁止事项】
不要补充 DDL 中不存在的表、字段、完整流程或角色权限。
```

## 输出文件名

`results/task_02_ddl_to_ontology.json`

## 输出格式

- 单个合法 JSON 对象。
- 尽量兼容 `schemas/ontology.schema.json`。
- 字段名使用英文。

## 证据链要求

- 每个 attribute 引用对应列。
- 每个 relation 引用外键或 `*_id` 字段。
- 每个 rule 引用约束、列定义或注释。

## 不确定性表达要求

- 弱外键、缩写字段、缺失状态枚举写入 `uncertainties`。
- 注释与约束不一致写入 `conflicts`。

## 禁止幻觉要求

- 不得使用代码、CSV 或文档信息。
- 不得根据采购合同常识补全业务流程。
- 不得创造角色权限。

## 允许追问次数

最多 1 次。只允许追问缺失 DDL 或被截断表定义。

## 常见失败情况

- 机械表转概念但忽略关系。
- 漏掉 check/unique/not null 规则。
- 过度推断业务流程。
- 没有记录缩写和命名差异。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-02",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | over_inference | incomplete_extraction | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_02_ddl_to_ontology_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

