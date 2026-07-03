# Task 06: Schema 修复

## 任务目标

修复前置任务输出中的 JSON 格式错误和 schema 兼容问题，使结果可用于自动校验。只允许修复结构、字段名、类型和格式，不允许新增没有证据支持的业务内容。

## 输入材料

- 一个或多个待修复输出：`task_01` 至 `task_05` 的 JSON。
- 相关 schema：`schemas/ontology.schema.json`、`schemas/evidence.schema.json`、`schemas/task_result.schema.json`。
- JSON 校验错误信息，如有。

## 操作员步骤

1. 将待修复 JSON、目标 schema 和校验错误提供给 AI 工具。
2. 要求 AI 只修复结构，不扩展业务内容。
3. 缺失必要字段时，使用空数组、null、低 confidence 或 uncertainty，不编造。
4. 保存修复后的 JSON 和 repair log。
5. 第二次仍无法修复时记录失败。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP schema repair 任务。请修复我提供的 JSON，使其成为合法 JSON，并尽量兼容目标 schema。你只能修复结构、字段名、类型、缺失必填字段和格式问题，不允许新增没有证据支持的业务事实。

【任务目标】
输出修复后的 JSON 和 repair_log，说明修复了哪些结构问题。

【修复原则】
1. 保留原始业务结论，不要重写本体。
2. 修复非法 JSON：逗号、引号、括号、代码围栏、注释等。
3. 修复字段类型：字符串、数字、布尔、数组、对象。
4. 修复字段名：例如 evidences -> evidence_refs，uncertainty -> uncertainties。
5. 缺失必填数组时使用空数组。
6. 缺失 confidence 时使用 null 或低置信度，不要伪造高置信度。
7. 缺少证据的新增必填字段必须在 `remaining_uncertainties` 或 `repair_log` 中说明。
8. 不要新增新的 concept、rule、relation，除非它们已在原始 JSON 中但结构错误。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "repaired_output": {},
  "repair_log": [
    {
      "issue_type": "invalid_json | missing_required_field | wrong_type | wrong_field_name | schema_compatibility | other",
      "path": "",
      "repair_action": "",
      "business_content_changed": false
    }
  ],
  "remaining_uncertainties": [],
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "schema_repair"
  }
}

【证据要求】
保留原有 evidence_refs；如果移动证据字段，在 repair_log 说明；不要伪造 evidence_refs。

【不确定性要求】
无法判断字段映射时保留原值并写入 `remaining_uncertainties`；必填字段缺失但无证据时用空值并记录。

【禁止事项】
不要新增原始 JSON 中不存在的业务对象、字段、状态、规则或关系；不要把 repair 任务变成重新抽取任务。
```

## 输出文件名

`results/task_06_schema_repair.json`

## 输出格式

- 单个合法 JSON 对象。
- 顶层包含 `repaired_output`、`repair_log`、`remaining_uncertainties`、`provenance`。
- `repaired_output` 是修复后的原任务输出。

## 证据链要求

- 保留原 evidence_refs。
- 不伪造新证据。
- repair_log 说明任何证据字段迁移。

## 不确定性表达要求

- 无法可靠修复的字段写入 `remaining_uncertainties`。
- 必填字段缺失但无证据时，用空值或空数组并记录。

## 禁止幻觉要求

- 不得新增业务结论。
- 不得改写冲突为已解决。
- 不得提高 confidence 掩盖证据不足。

## 允许追问次数

最多 1 次。只允许追问目标 schema、原始 JSON 是否完整或校验错误是否完整。

## 常见失败情况

- 借 repair 机会重新生成本体。
- 删除 evidence_refs、conflicts 或 uncertainties。
- 伪造缺失字段内容。
- 输出仍不是合法 JSON。
- 没有 repair_log。

## 失败记录方式

```json
{
  "task_id": "TASK-06",
  "status": "failed",
  "failure_type": "invalid_json | changed_business_content | dropped_evidence | missing_repair_log | unresolved_schema_error | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_06_schema_repair_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

