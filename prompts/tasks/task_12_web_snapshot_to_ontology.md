# Task 12: Web Snapshot 到本体

## 任务目标

基于可选 Web HTML snapshot 和 page map 输入，抽取 Web 来源的本体补充，识别页面对象、可见字段、表格列、按钮动作、状态标签、角色线索、页面链接、UI 术语、mapping、alias、conflict 和 uncertainty。当前任务只评估离线 HTML / page map 语义理解；不得声称访问了 live Web、登录系统、执行按钮或观察动态 JavaScript 结果。

## 输入材料

- `datasets/generic_procurement_contract_mvp/web_snapshots/*.html`
- `datasets/generic_procurement_contract_mvp/web_map/page_map.json`
- `datasets/generic_procurement_contract_mvp/web_map/page_map.md`
- 可参考 schema：`schemas/ontology.schema.json`、`schemas/evidence.schema.json`、`schemas/task_result.schema.json`

禁止提供给被评估 AI：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `results/demo_screenshot/`
- `results/demo_web/`（如未来存在）
- `machine_score.json`、`machine_score.md`、人工复核内容或任何 evaluator-only Web gold/conflict 文件

## 操作员步骤

1. 确认本轮评估明确启用了可选 Web snapshot extension；否则不要运行 Task 12。
2. 将 `web_snapshots/*.html`、`web_map/page_map.json` 和 `web_map/page_map.md` 提供给 AI 工具。
3. 告诉 AI 当前输入模式是 `html_snapshot`；如果只能提供 page map，则声明 `page_map_only`。
4. 要求 AI 只基于 Web snapshot / page map 作答；不要使用代码、DDL、CSV、业务文档、gold answer、demo outputs 或外部系统常识补全。
5. 保存原始输出；若 JSON 不合法，允许一次 schema repair。
6. 后续如需与 MVP 或 screenshot 输出融合，应运行 Task 14；不要在本任务中直接改写 Task 05 输出。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP Web Snapshot 到本体抽取任务。请只基于我提供的 web_snapshots/*.html、page_map.json 和 page_map.md 作答，不要使用源代码、DDL、CSV、业务文档、gold answer、demo outputs、评分输出或外部采购合同常识。

【重要输入模式声明】
本任务的输入模式是 html_snapshot。你看到的是离线静态 HTML 和 page map，不是 live Web，不是登录后的真实系统，不包含后端接口执行结果。如果我只提供 page map 而没有 HTML，请把 input_mode 写成 page_map_only，并且不要声称解析了 DOM。

【任务目标】
从 Web snapshot 中抽取 UI 来源的本体补充，覆盖 page、concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty、evidence_refs、confidence、provenance。

【抽取要求】
1. page：识别页面类型、页面目的、页面主业务对象、菜单路径和面包屑。
2. visible field：将 HTML 中可见 label、table header、field value 映射到 candidate attribute、relation 或 concept。
3. table column：将表格列映射到 candidate attribute、relation、state 或 action 线索。
4. button / link / action：将按钮和链接映射到 candidate action 或 navigation flow；按钮存在不等于后端能力已实现。
5. status badge：将状态标签映射到 candidate state；不要把不同对象的状态强行合并。
6. role context：从页面角色提示、按钮可见性和菜单可见性中抽取 role / permission 候选。
7. alias：识别 UI 术语与其他来源可能不同的情况，例如 Vendor/Supplier、PR/Purchase Request、GRN/Goods Receipt、Payment Application/Payment Request。
8. mapping：记录 UI label、page_id、DOM locator、link text 与 candidate ontology element 的映射。
9. conflict：页面术语、按钮、状态或角色与其他来源可能冲突时，只写成候选 conflict 或 uncertainty，不要自行裁决。
10. uncertainty：仅由 Web UI 支持、缺少后端/文档确认的结论必须降低 confidence 并写入 uncertainty。

【降级与能力声明】
1. 如果有 HTML snapshot：input_mode 必须写 html_snapshot。
2. 如果只有 page_map：input_mode 必须写 page_map_only，只能分析页面清单、链接关系和 map 中可见字段，不得声称解析了 HTML DOM。
3. 如果 HTML 中出现按钮但没有真实执行：写成 UI-derived candidate action。
4. 如果页面缺失、断链或动态内容不可见：写入 uncertainties。
5. 不得声称进行了 live crawl、登录、点击、API 调用、JS 执行或真实可达性验证。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-web-snapshot-ontology",
  "title": "Procurement Contract MVP Web Snapshot Ontology Draft",
  "domain": "procurement_contract",
  "description": "Web-derived ontology supplement extracted from offline HTML snapshots and page map.",
  "input_mode": "html_snapshot",
  "source_system": "web_snapshot",
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
    "source_system": "web_snapshot",
    "input_mode": "html_snapshot"
  }
}

【pages 建议结构】
每个页面对象建议包含：
{
  "page_id": "web:...",
  "page_name": "",
  "page_type": "home | list | detail | approval_task | invoice_matching | payment | other",
  "input_mode": "html_snapshot",
  "menu_path": [],
  "breadcrumb": [],
  "primary_business_objects": [],
  "visible_fields": [],
  "table_columns": [],
  "button_actions": [],
  "status_labels": [],
  "role_context": [],
  "outgoing_links": [],
  "evidence_refs": []
}

【证据要求】
1. 每个 Web-derived concept、attribute、relation、action、state、role、flow 或 mapping 必须引用 `web:*` evidence handle。
2. evidence_ref 可使用页面级 handle，例如 `web:purchase_requests.page`，也可使用字段级 handle，例如 `web:purchase_requests.table.pr_no`。
3. source_ref / mapping 中可使用 `web_snapshots/<file>.html#<page_id>`、CSS selector、DOM path、link text 或 section label。
4. 不要引用 gold、demo baseline、machine_score、known conflicts 或未提供文件。

【不确定性要求】
1. UI 只显示按钮但没有后端证据时，写入 uncertainty。
2. UI label 与其他来源可能不一致时，写入 alias、mapping 或 conflict candidate。
3. 单一页面支持的结论 confidence 不高于 0.7；多个 Web 页面一致时可提高，但仍不得当作后端事实。
4. 动态内容、登录权限、断链、缺页和 page_map_only 限制必须写入 uncertainties。

【禁止事项】
1. 不要声称访问了 live Web、登录系统、点击按钮、执行 JavaScript 或调用 API。
2. 不要补充 HTML / page map 中没有出现的页面、按钮、字段、状态或角色。
3. 不要读取或引用 gold answer、known conflicts、demo outputs、scoring 输出或人工复核材料。
4. 不要把 UI 按钮直接等同于已实现的后端服务能力。
5. 不要把本任务输出当作最终融合 ontology；它只是 Web-derived supplement。
```

## 输出文件名

`results/<evaluation_id>/normalized_outputs/task_12_web_snapshot_to_ontology.json`

同时保存：

- 原始输出：`results/<evaluation_id>/raw_outputs/task_12_web_snapshot_to_ontology_raw.md`
- task result wrapper：`results/<evaluation_id>/task_12_web_snapshot_to_ontology_result.json`

## 输出格式

- 单个合法 JSON 对象。
- 字段名使用英文。
- 建议尽量兼容 `schemas/ontology.schema.json`，但允许包含 Web 补充字段如 `input_mode`、`source_system`、`pages`、`page_flows`。
- `input_mode` 必须是 `html_snapshot` 或 `page_map_only`，除非未来任务明确提供 live Web 输入。

## Evidence 要求

- 每个 Web-derived 结论必须包含 `web:*` evidence handle。
- 页面级结论引用 `web:<page>.page` 或 `web_snapshots/<file>.html#web:<page>`。
- 字段级结论引用具体 label、CSS selector、DOM path 或 section label。
- 链接关系引用 link text、href 和 page_map entry。
- 不得引用 evaluator-only gold、known conflicts、demo outputs 或 scoring 输出。

## 不确定性要求

- `html_snapshot` 输入不能证明 live Web、登录态、动态 JS 或后端执行；必须在 provenance 或 uncertainties 中说明。
- UI-only button/action、UI-only role visibility、UI-only state 和 UI-only calculated indicators 都应标记为候选或低置信度。
- 如果 UI 术语与已知后端/文档术语可能不同，只能记录 alias/mapping/conflict candidate，不得自行裁决。
- 如果页面缺失、断链或 page map 与 HTML 不一致，写入 `uncertainties`。

## 禁止幻觉要求

- 不得声称 live crawl、登录、点击、JS 执行、API 调用、浏览器自动化或真实网络可达性。
- 不得补充未提供页面、未出现按钮、未出现字段、未出现状态或未出现角色。
- 不得用外部采购系统常识补全付款、合同、审批或发票规则。
- 不得把 UI 文案直接上升为最终业务规则；需要后续多源融合确认。

## 无法访问 Web 时的降级规则

- 工具不能访问 live Web 但能读 HTML：正常执行，标记 `input_mode = html_snapshot`。
- 工具不能读 HTML 但能读 page map：标记 `input_mode = page_map_only`，只输出页面清单、链接关系和 map 中已列字段。
- 工具只能处理复制粘贴片段：标记 `input_mode = manual_page_notes`，记录复制范围和缺失页面。
- HTML 中 JS 动态内容不可见：写入 uncertainty，不能编造运行后 DOM。
- 登录/权限页面不可用：标记 `blocked_or_unavailable` uncertainty。

## 允许追问次数

最多 1 次。只允许追问缺失的 HTML 文件、page map 是否完整，或输入模式是否为 `html_snapshot` / `page_map_only`。

## 常见失败

- 声称访问了 live Web、点击按钮或执行 JS。
- 没有声明 `input_mode`。
- 没有引用 `web:*` evidence handle。
- 把 UI button 当成已实现后端动作。
- 混入代码、DDL、CSV、文档或 gold answer 信息。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-12",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | wrong_input_mode | claimed_live_web | used_wrong_source | hallucination | incomplete_extraction | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_12_web_snapshot_to_ontology_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 复制 prompt 时只复制 fenced code block 内的内容；不要把操作员步骤、输出文件名说明、gold/reference 路径或 scoring 输出复制给被评估 AI。
