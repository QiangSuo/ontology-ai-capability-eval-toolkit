# Task 04: 业务文档到本体

## 任务目标

只基于采购合同 MVP 业务说明文档抽取本体草案，识别业务概念、流程、状态机、业务规则、角色权限、别名和术语。不得使用源代码、DDL 或 CSV。

## 输入材料

- `datasets/generic_procurement_contract_mvp/documents/`
- 推荐文档：`business_overview.md`、`procurement_process.md`、`business_rules.md`、`contract_lifecycle.md`、`receipt_invoice_payment_policy.md`、`role_permission_matrix.md`、`glossary.md`。
- 可参考 schema：`schemas/ontology.schema.json`。

## 操作员步骤

1. 将业务文档提供给 AI 工具；不能读目录时，按文档顺序复制 Markdown。
2. 要求 AI 只基于文档抽取本体。
3. 要求保留流程、状态机、规则、角色权限和术语证据。
4. 若 JSON 不合法，允许一次修复追问。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 业务文档到本体抽取任务。请只基于我提供的业务说明文档作答，不要使用源代码、DDL、CSV 或外部知识。

【任务目标】
从业务文档中抽取 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty。

【抽取要求】
1. concept：从业务名词、对象定义、术语表中抽取。
2. attribute：只从文档明确列出的字段、必填信息、业务属性中抽取。
3. relation：从“属于、关联、生成、转换、包含、审批、交接”等表述中抽取。
4. event：从流程节点和状态变化中抽取。
5. rule：从政策、前置条件、审批规则、禁止事项、终态规则中抽取。
6. action：从用户可执行动作、流程动作和审批动作中抽取。
7. state：从 PurchaseRequest、Contract、PurchaseOrder、GoodsReceipt、Invoice、PaymentRequest 等状态机中抽取。
8. role / permission：从角色说明和权限矩阵中抽取。
9. alias：从术语表和同义词表抽取，例如 Supplier/Vendor、Purchase Request/PR、Purchase Order/PO、Goods Receipt/GRN、Payment Request/Payment Application。
10. conflict / uncertainty：不同文档之间说法不一致、边界不清或证据不足时必须记录。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-document-ontology",
  "title": "Procurement Contract MVP Document Ontology Draft",
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
    "source_system": "documents"
  }
}

【证据要求】
`evidence_refs` 使用 `doc:<file>#<section>`；rule、state、permission、alias 必须引用具体章节。

【不确定性要求】
文档只描述业务意图但没有字段定义时，attribute confidence 降低；规则边界不清写入 `uncertainties`。

【禁止事项】
不要补充文档未提到的数据库字段、状态值、审批阈值或流程分支。
```

## 输出文件名

`results/task_04_document_to_ontology.json`

## 输出格式

- 单个合法 JSON 对象。
- 尽量兼容 `schemas/ontology.schema.json`。
- 字段名使用英文。

## 证据链要求

- 使用文档文件名和章节作为证据。
- 业务规则、状态机、权限矩阵必须有章节引用。
- 同义词必须有 alias evidence。

## 不确定性表达要求

- 文档未说明字段、状态流转缺失、规则边界不清时必须记录。
- 文档之间规则不一致时写入 conflict。

## 禁止幻觉要求

- 不得使用代码、DDL、CSV 信息。
- 不得生成文档未出现的状态值和审批阈值。
- 不得把同义词当作重复核心概念。

## 允许追问次数

最多 1 次。只允许追问缺失文档、文档被截断或章节顺序不清。

## 常见失败情况

- 忽略 alias 和 glossary。
- 将文档描述扩展成不存在字段。
- 不记录规则边界冲突。
- 缺少角色权限。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-04",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | hallucinated_fields | missed_aliases | missed_permissions | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_04_document_to_ontology_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

