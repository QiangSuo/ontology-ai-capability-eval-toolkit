# Task 08: Screenshot Surrogate 到本体

## 任务目标

基于可选 screenshot surrogate 输入抽取 UI 来源的本体补充，识别页面对象、可见字段、表格列、按钮动作、状态标签、角色线索、UI 术语、mapping、alias、conflict 和 uncertainty。当前 B3 任务只支持 `surrogate_only` 文本截图替身；不得声称测试了真实图片、OCR、布局检测或视觉理解能力。

## 输入材料

- `datasets/generic_procurement_contract_mvp/metadata/screenshot_manifest.json`
- `datasets/generic_procurement_contract_mvp/screenshots/*.screen.md`
- 可参考 schema：`schemas/ontology.schema.json`、`schemas/evidence.schema.json`、`schemas/task_result.schema.json`

禁止提供给被评估 AI：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `results/demo_screenshot/`（如未来存在）
- `machine_score.json`、`machine_score.md`、人工复核内容或任何 evaluator-only screenshot gold/conflict 文件

## 操作员步骤

1. 确认本轮评估明确启用了可选 screenshot surrogate extension；否则不要运行 Task 08。
2. 将 `metadata/screenshot_manifest.json` 和需要评估的 `.screen.md` 文件提供给 AI 工具。
3. 告诉 AI 当前输入模式是 `surrogate_only`，不是真实 PNG/JPG 图片。
4. 要求 AI 只基于 screenshot surrogate 输入作答；不要使用代码、DDL、CSV、业务文档或外部系统常识补全。
5. 保存原始输出；若 JSON 不合法，允许一次 schema repair。
6. 后续如需与 MVP 统一本体融合，应另开后续融合任务，不要在本任务中直接改写 Task 05 输出。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP Screenshot Surrogate 到本体抽取任务。请只基于我提供的 screenshot_manifest.json 和 *.screen.md 文件作答，不要使用源代码、DDL、CSV、业务文档、gold answer、demo baseline、评分输出或外部采购合同常识。

【重要输入模式声明】
本任务的输入模式是 surrogate_only。你看到的是 Markdown 文本形式的截图替身，不是真实 PNG/JPG 图片，也不是 OCR 结果。你可以抽取 UI 文本语义，但不得声称自己看到了真实图片、视觉布局、图标、颜色、像素区域、bounding box 或 OCR 质量。

【任务目标】
从 screenshot surrogate 中抽取 UI 来源的本体补充，覆盖 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty、evidence_refs、confidence、provenance。

【抽取要求】
1. page / screen：识别页面类型、页面目的、页面主业务对象。
2. visible field：将可见字段映射到 candidate attribute、relation 或 concept。
3. table column：将表格列映射到 candidate attribute、relation、state 或 action 线索。
4. button / action：将按钮映射到 candidate action；按钮可见性只是 UI 证据，不等于后端能力已实现。
5. status badge：将状态标签映射到 candidate state；不要把不同对象的状态强行合并。
6. role context：从页面角色、按钮可见性、审批角色中抽取 role / permission 候选。
7. alias：识别 UI 术语与后端/业务术语可能不同的情况，例如 Vendor/Supplier、PR/Purchase Request、GRN/Goods Receipt、Payment Application/Payment Request。
8. mapping：记录 UI label、page_id、evidence handle 与 candidate ontology element 的映射。
9. conflict：UI 术语、按钮、状态或角色与其他来源可能冲突时，写成候选 conflict 或 uncertainty，不要静默解决。
10. uncertainty：仅由 UI 文本支持、缺少后端/文档确认的结论必须降低 confidence 并写入 uncertainty。

【降级与能力声明】
1. 如果只有 *.screen.md：`input_mode` 必须写 `surrogate_only`。
2. 如果没有真实图片：不得输出 `real_image`、`image_seen`、`ocr_detected`、`bbox`、`pixel_region` 等暗示真实视觉能力的字段或说法。
3. 如果某个页面缺失：只抽取已提供页面，并在 `uncertainties` 中说明未覆盖页面。
4. 如果按钮或字段只在 UI 中出现：标记为 `screenshot_only_candidate` 或低 confidence。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-screenshot-surrogate-ontology",
  "title": "Procurement Contract MVP Screenshot Surrogate Ontology Draft",
  "domain": "procurement_contract",
  "description": "UI-derived ontology supplement extracted from screenshot surrogate Markdown files. This is surrogate_only and does not prove real image understanding.",
  "input_mode": "surrogate_only",
  "source_system": "screenshot_surrogate",
  "pages": [],
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
    "source_system": "screenshot_surrogate",
    "input_mode": "surrogate_only"
  }
}

【pages 建议结构】
每个页面对象建议包含：
{
  "page_id": "screen:...",
  "page_name": "",
  "page_type": "list | detail | approval_task | payment | other",
  "input_mode": "surrogate_only",
  "primary_business_objects": [],
  "visible_fields": [],
  "table_columns": [],
  "button_actions": [],
  "status_labels": [],
  "role_context": [],
  "evidence_refs": []
}

【证据要求】
1. 每个 UI-derived concept、attribute、relation、action、state、role 或 mapping 必须引用 `screen:*` evidence handle。
2. `evidence_refs` 使用 screenshot surrogate 中已有的 handle，例如 `screen:purchase_request_list.field.pr_no`、`screen:contract_detail.button.activate_contract`。
3. source_ref / mapping 中可使用 `screenshots/<file>.screen.md#<screen:...>`。
4. 不要引用 gold、demo baseline、machine_score 或未提供文件。

【不确定性要求】
1. UI 只显示按钮但没有后端证据时，写入 uncertainty。
2. UI label 与其他来源可能不一致时，写入 alias、mapping 或 conflict candidate。
3. 单一页面支持的结论 confidence 不高于 0.7；跨多个 UI 页面一致时可提高，但仍不得当作后端事实。
4. 只由 surrogate 支持的视觉/布局结论必须标记为不支持，而不是低置信度视觉结论。

【禁止事项】
1. 不要声称看到了真实截图、颜色、图标、布局、OCR 或坐标。
2. 不要补充 screenshot surrogate 中没有出现的字段、按钮、状态、页面或角色。
3. 不要读取或引用 gold answer、known conflicts、demo baseline、scoring 输出或人工复核材料。
4. 不要把 UI 按钮直接等同于已实现的后端服务能力。
5. 不要把本任务输出当作最终融合 ontology；它只是 UI-derived supplement。
```

## 输出文件名

`results/<evaluation_id>/normalized_outputs/task_08_screenshot_to_ontology.json`

同时保存：

- 原始输出：`results/<evaluation_id>/raw_outputs/task_08_screenshot_to_ontology_raw.md`
- task result wrapper：`results/<evaluation_id>/task_08_screenshot_to_ontology_result.json`

## 输出格式

- 单个合法 JSON 对象。
- 字段名使用英文。
- 建议尽量兼容 `schemas/ontology.schema.json`，但允许包含 UI 补充字段如 `input_mode`、`source_system`、`pages`。
- `input_mode` 必须是 `surrogate_only`，除非未来任务明确提供真实图片输入。

## 证据链要求

- 每个 UI-derived 结论必须包含 `screen:*` evidence handle。
- 页面级结论引用 `screen:<page>.page`。
- 字段级结论引用 `screen:<page>.field.*`。
- 表格列引用 `screen:<page>.column.*` 或具体表格 handle。
- 按钮动作引用 `screen:<page>.button.*`。
- 状态引用 `screen:<page>.status.*` 或字段 handle。
- 不得引用 evaluator-only gold、known conflicts、demo baseline 或 scoring 输出。

## 不确定性表达要求

- `surrogate_only` 输入不能证明真实视觉能力；必须在 provenance 或 uncertainties 中说明。
- UI-only button/action、UI-only role visibility、UI-only status、UI-only calculated indicators 都应标记为候选或低置信度。
- 如果 UI 术语与已知后端/文档术语可能不同，只能记录 alias/mapping/conflict candidate，不得自行裁决。
- 如果页面缺失或 manifest 与 `.screen.md` 不一致，写入 `uncertainties`。

## 禁止幻觉要求

- 不得声称执行了 OCR、看到了真实图片、识别了图标、颜色、布局、区域坐标或像素级位置。
- 不得补充未提供页面、未出现按钮、未出现字段、未出现状态或未出现角色。
- 不得用外部采购系统常识补全付款、合同、审批或发票规则。
- 不得把 UI 文案直接上升为最终业务规则；需要后续多源融合确认。

## 降级执行规则

- 工具不能看图片但能读 `.screen.md`：正常执行，标记 `input_mode = surrogate_only`。
- 工具不能读目录但能读粘贴文本：操作员逐个复制 `.screen.md` 文件内容，并记录复制范围。
- 工具只能处理部分页面：只输出已处理页面，并记录缺失页面。
- 工具无法稳定输出 JSON：运行 Task 06 schema repair，但不得新增业务内容。
- 工具声称看到了真实图片或 OCR：记录为 hallucination / capability misrepresentation 风险。

## 允许追问次数

最多 1 次。只允许追问缺失的 `.screen.md` 文件、manifest 是否完整，或输入模式是否为 surrogate-only。

## 常见失败情况

- 声称看到了真实截图、颜色、图标、坐标或 OCR。
- 没有声明 `input_mode = surrogate_only`。
- 没有引用 `screen:*` evidence handle。
- 把 UI button 当成已实现后端动作。
- 混入代码、DDL、CSV、文档或 gold answer 信息。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-08",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | wrong_input_mode | claimed_real_image | used_wrong_source | hallucination | incomplete_extraction | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_08_screenshot_to_ontology_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

## B3 结果保存补充说明

- 不要把 `datasets/generic_procurement_contract_mvp/gold/`、`results/demo_baseline/`、`machine_score.json` 或人工复核内容提供给被评估 AI。
- AI 原始回答保存到 `results/<evaluation_id>/raw_outputs/`。
- 操作员整理后的合法 JSON 保存到 `results/<evaluation_id>/normalized_outputs/`。
- 每个参与评分的任务还需要一个 `task_result` wrapper，保存到 `results/<evaluation_id>/task_08_screenshot_to_ontology_result.json`，并通过 `output_artifacts` 指向 raw/normalized 文件。
- 复制 prompt 时只复制 fenced code block 内的内容；不要把操作员步骤、输出文件名说明、gold/reference 路径或 scoring 输出复制给被评估 AI。
- 本任务不修改 Task 05 fused ontology；如需融合 UI 来源结果，应在后续独立 fusion task 中完成。
