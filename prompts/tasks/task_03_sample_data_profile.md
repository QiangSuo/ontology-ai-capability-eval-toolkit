# Task 03: 样例数据画像

## 任务目标

只基于采购合同 MVP CSV 样例数据生成数据画像，识别字段值分布、枚举候选、空值、异常值、关系线索和业务语义线索。该任务不要求生成完整本体，应输出可供后续融合使用的数据证据。

## 输入材料

- `datasets/generic_procurement_contract_mvp/database/sample_data/*.csv`
- 可参考 schema：`schemas/evidence.schema.json`、`schemas/ontology.schema.json`。

## 操作员步骤

1. 将 CSV 文件提供给 AI 工具；不能读取全部文件时，提供表头、行数、前 10 行和异常样例。
2. 要求 AI 输出每个 CSV 的表级画像和字段级画像。
3. 明确区分 candidate 与确定结论。
4. 若只提供部分数据，必须记录 `sample_is_partial`。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 样例数据画像任务。请只基于我提供的 CSV 样例数据作答，不要使用源代码、DDL、业务文档或外部知识。

【任务目标】
分析 CSV 样例数据，识别字段含义线索、枚举值、状态值、空值、异常值、主外键候选、关系候选和业务规则线索。

【分析要求】
1. 为每个 CSV 输出 table profile：文件名、行数、字段列表、候选 concept。
2. 为每个字段输出 column profile：字段名、样例值、空值情况、可能数据类型、候选业务含义。
3. 识别枚举候选：status、type、role_code、approval_status、contract_status、invoice_status、payment_status 等。
4. 识别关系候选：相同 ID 值、`*_id` 字段、引用模式。
5. 识别数据质量问题：空值、重复、疑似异常金额、无效状态、引用缺失。
6. 识别业务规则线索，但只能作为 candidate，不要直接断言完整规则。
7. 识别命名差异：PR、PO、GRN、Vendor/Supplier、Payment Application 等缩写或同义词。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "task_id": "TASK-03",
  "title": "Procurement Contract MVP Sample Data Profile",
  "source_system": "sample_data_csv",
  "sample_is_partial": null,
  "table_profiles": [
    {
      "file_name": "",
      "row_count": null,
      "candidate_concept": "",
      "columns": [
        {
          "column_name": "",
          "inferred_type": "",
          "sample_values": [],
          "null_observation": "",
          "candidate_attribute": "",
          "candidate_enum_values": [],
          "evidence_refs": [],
          "confidence": 0.0
        }
      ],
      "candidate_relations": [],
      "data_quality_notes": [],
      "evidence_refs": []
    }
  ],
  "candidate_states": [],
  "candidate_rules": [],
  "candidate_aliases": [],
  "candidate_conflicts": [],
  "uncertainties": [],
  "evidence_refs": [],
  "confidence": 0.0,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "sample_data_csv"
  }
}

【证据要求】
`evidence_refs` 使用 `csv:<file>#column:<column>` 或 `csv:<file>#row:<row_number>`；异常值和枚举值必须引用具体文件与字段。

【不确定性要求】
样本不足、行数未知、关系未验证、字段含义不确定都必须写入 `uncertainties`。

【禁止事项】
不要补充 CSV 中未出现的状态值；不要把样例数据推断成完整业务规则。
```

## 输出文件名

`results/task_03_sample_data_profile.json`

## 输出格式

- 单个合法 JSON 对象。
- 不要求是完整 ontology；候选项使用 `candidate_*` 字段。
- 字段名使用英文。

## 证据链要求

- 字段画像引用 CSV 文件名和列名。
- 枚举、异常、关系候选引用具体文件和字段。
- 部分样本必须记录输入范围。

## 不确定性表达要求

- 样本不足、字段含义不确定、关系未验证写入 `uncertainties`。
- 从值分布推断的规则必须保持 candidate 或低 confidence。

## 禁止幻觉要求

- 不得使用 DDL、代码、文档信息。
- 不得把少量样本当作完整全集。
- 不得生成没有证据的完整状态机。

## 允许追问次数

最多 1 次。只允许追问缺失 CSV、被截断数据或样本是否完整。

## 常见失败情况

- 输出完整本体但缺少数据画像。
- 把样例推断成确定规则。
- 没有记录样本范围。
- 忽略空值和异常值。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-03",
  "status": "failed",
  "failure_type": "invalid_json | over_inference | missing_profile | missing_evidence | partial_input_not_recorded | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_03_sample_data_profile_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

