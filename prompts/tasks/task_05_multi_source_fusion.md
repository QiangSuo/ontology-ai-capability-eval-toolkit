# Task 05: 多源融合

## 任务目标

融合代码、DDL、CSV 数据画像和业务文档四类输入，生成采购合同 MVP 统一本体结果。重点测试多源证据、命名不一致、同义词、轻微冲突、不确定性和 provenance 处理能力。

## 输入材料

- `results/task_01_code_to_ontology.json`
- `results/task_02_ddl_to_ontology.json`
- `results/task_03_sample_data_profile.json`
- `results/task_04_document_to_ontology.json`
- 可选原始片段：`source_code/`、`database/ddl.sql`、`database/sample_data/`、`documents/`。
- 可参考 schema：`schemas/ontology.schema.json`、`schemas/evidence.schema.json`。

## 操作员步骤

1. 将前四个任务输出提供给 AI 工具。
2. 上下文允许时，补充关键原始材料片段用于复核。
3. 要求 AI 生成统一 ontology，而不是四份结果拼接。
4. 要求保留 alias、mapping、conflict、uncertainty、confidence。
5. 若 JSON 不合法，允许一次修复追问。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 多源融合任务。请基于代码抽取结果、DDL 抽取结果、CSV 数据画像和业务文档抽取结果，生成统一本体 JSON。不要简单拼接四份结果，必须去重、归并、融合并保留证据和冲突。

【任务目标】
生成采购合同 MVP 统一本体，覆盖 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty、confidence、evidence_refs、provenance。

【融合原则】
1. 同义词归并：Supplier/Vendor；Purchase Request/PR；Purchase Order/PO；Goods Receipt/GRN；Payment Request/Payment Application。
2. 命名不一致保留 alias：`pc_` 表前缀、`pr_number`、`po_number`、`target_type`/`target_id`、`role_code`、Material/Item。
3. 多源一致时提高 confidence；单一来源支持时保留但降低 confidence。
4. 来源冲突时不要强行选择，写入 `conflicts`，并说明来源差异。
5. 文档说明业务规则，代码说明实际实现，DDL 说明结构约束，CSV 说明样例事实；都要保留 provenance。
6. 不要为了完整性创造没有来源支持的对象或规则。

【必须检查的融合点】
- Supplier / Vendor 是否归并。
- Purchase Request / PR 是否归并，并与 Purchase Order / PO 保持边界。
- Goods Receipt / GRN 是否归并。
- Payment Request / Payment Application 是否归并。
- 审批阈值是否存在 `>= 50000` 与 `> 50000` 差异。
- 发票匹配容差是否存在 2% 与 1.5% 差异。
- 合同激活签署要求是否只有文档证据、缺少 DDL/代码字段支持。
- 付款 hold reason 是否只有文档政策、缺少 DDL/CSV 字段支持。
- Material / Item 语义是否在申请行中出现但缺少独立物料主数据表。
- `pc_approval_record.target_type` / `target_id` 是否需要作为多态关系低置信度处理。
- Goods Receipt 的 COMPLETE 与 Purchase Order 的 CLOSED 是否被错误合并为同一状态。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-fused-ontology",
  "title": "Procurement Contract MVP Fused Ontology",
  "domain": "procurement_contract",
  "description": "Unified ontology fused from code, DDL, sample data and procurement documents.",
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
    "source_system": "multi_source_fusion"
  }
}

【证据要求】
核心 concept 尽量有 2 类来源证据；核心 relation 应引用 DDL 或代码证据；核心 rule 应引用文档或代码证据；冲突必须引用至少两个来源。

【不确定性要求】
单源结论、候选关系、样本推断、规则边界差异都必须表达 uncertainty 或 conflict。

【禁止事项】
不要生成四类输入中都没有证据的对象、字段、关系、规则或动作；不要隐藏冲突。
```

## 输出文件名

`results/task_05_multi_source_fusion.json`

## 输出格式

- 单个合法 JSON 对象。
- 应尽量通过 `schemas/ontology.schema.json` 校验。
- 字段名使用英文。

## 证据链要求

- 核心本体元素尽量有多源 evidence。
- 冲突必须引用至少两个来源。
- alias 和 mapping 必须保留原始命名。

## 不确定性表达要求

- 单源结论、候选关系、样本推断、规则边界差异都必须写入不确定性。
- 不确定性是有效输出，不等于失败。

## 禁止幻觉要求

- 不得补充未提供来源支持的采购合同对象。
- 不得自行解决冲突后删除来源差异。
- 不得输出没有 provenance 的统一本体。

## 允许追问次数

最多 2 次。允许追问前置任务输出缺失、明显截断，或关键冲突需要原始片段复核。

## 常见失败情况

- 简单拼接四份结果，未去重。
- Supplier/Vendor 或 Purchase Request/PR 被错误拆成重复概念。
- 丢失 evidence_refs。
- 忽略 conflict 和 uncertainty。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-05",
  "status": "failed",
  "failure_type": "invalid_json | no_deduplication | missing_conflicts | missing_evidence | hallucination | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_05_multi_source_fusion_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

