# Task 13: Page Map 到业务流程

## 任务目标

基于可选 Web page map 和 HTML snapshot 链接关系，生成页面流程、模块路径、角色路径和递归导航分析。重点测试 AI 工具是否能从页面清单、菜单、面包屑、outgoing_links / incoming_links 和断链说明中理解业务流程，而不是把 page map 误当作 gold ontology。

## 输入材料

- `datasets/generic_procurement_contract_mvp/web_map/page_map.json`
- `datasets/generic_procurement_contract_mvp/web_map/page_map.md`
- 可选：`datasets/generic_procurement_contract_mvp/web_snapshots/*.html` 用于复核页面标题、链接和可见文本
- 可参考 schema：`schemas/evidence.schema.json`、`schemas/task_result.schema.json`

禁止提供给被评估 AI：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `results/demo_screenshot/`
- `results/demo_web/`（如未来存在）
- `machine_score.json`、`machine_score.md`、人工复核内容或 evaluator-only Web gold/conflict 文件

## 操作员步骤

1. 确认本轮评估启用了可选 Web page map extension；否则不要运行 Task 13。
2. 将 `page_map.json` 和 `page_map.md` 提供给 AI 工具。
3. 如果上下文允许，提供对应 HTML snapshot 以便复核链接；如果不提供 HTML，声明 `input_mode = page_map_only`。
4. 要求 AI 输出页面流程和业务路径分析，而不是输出完整本体或修改 Task 12 结果。
5. 保存原始输出；若 JSON 不合法，允许一次 schema repair。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP Page Map 到业务流程分析任务。请只基于我提供的 page_map.json、page_map.md 和可选 HTML snapshot 作答，不要使用源代码、DDL、CSV、业务文档、gold answer、demo outputs、评分输出或外部采购合同常识。

【重要输入模式声明】
如果我提供了 HTML snapshot，请把 input_mode 写成 html_snapshot_with_page_map。如果我只提供 page map，请把 input_mode 写成 page_map_only。page map 是输入侧页面清单和导航说明，不是标准答案。

【任务目标】
从 page map 和链接关系中生成页面流程 / 模块路径分析，覆盖 module_paths、business_flows、role_paths、navigation_graph、recursive_analysis_points、missing_pages、uncertainties、evidence_refs、confidence、provenance。

【分析要求】
1. module path：按菜单路径和 page_type 归纳 Purchase Requests、Workflow、Contracts、Finance 等模块。
2. business flow：根据 outgoing_links / incoming_links 推断候选页面流程，例如 PR list -> PR detail -> contract detail -> invoice -> payment。
3. role path：根据 required_role 和按钮/页面可见性识别不同角色可能看到的路径。
4. recursive navigation：识别通用 approval task、related documents、反向链接和跨模块链接。
5. repeated template：识别 list/detail/workbench 页面模板，避免把同一对象重复计数。
6. missing page：记录 page map 声明或页面暗示但没有 snapshot 的页面，例如 Purchase Order Detail、Goods Receipt Detail、Supplier Master。
7. uncertainty：page_map_only 时不得声称解析 DOM；缺页、断链、静态按钮和角色限制都写入 uncertainty。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "task_id": "TASK-13",
  "title": "Procurement Contract MVP Web Page Map Business Flow Analysis",
  "domain": "procurement_contract",
  "input_mode": "page_map_only",
  "source_system": "web_page_map",
  "module_paths": [],
  "business_flows": [],
  "role_paths": [],
  "navigation_graph": {
    "nodes": [],
    "edges": []
  },
  "recursive_analysis_points": [],
  "repeated_templates": [],
  "missing_pages": [],
  "flow_mappings": [],
  "uncertainties": [],
  "evidence_refs": [],
  "confidence": 0.0,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "web_page_map"
  }
}

【business_flows 建议结构】
每个流程对象建议包含：
{
  "flow_id": "flow:...",
  "flow_name": "",
  "pages_in_order": [],
  "primary_business_objects": [],
  "roles_involved": [],
  "navigation_edges": [],
  "missing_or_implied_pages": [],
  "evidence_refs": [],
  "confidence": 0.0,
  "uncertainties": []
}

【证据要求】
1. 每个 flow、module path、role path 或 navigation edge 必须引用 `web:*` evidence handle 或 `web_map/page_map.*` source_ref。
2. 导航边必须说明来源：page_map outgoing_links、incoming_links、HTML href 或 page_map.md crawl order。
3. 缺页/断链也要引用 page map 中的说明或触发页面。
4. 不要引用 gold、demo baseline、machine_score、known conflicts 或未提供文件。

【不确定性要求】
1. page_map_only 只能证明页面清单和链接说明，不能证明 DOM 字段、按钮真实存在或 live Web 可达。
2. HTML snapshot 只能证明静态链接和文本，不能证明登录权限、动态 JS、API 调用或后端执行。
3. 页面顺序是候选业务路径，不等于唯一流程或完整流程。
4. 角色可见性是 UI 线索，不等价于最终权限规则。

【禁止事项】
1. 不要把 page map 当作 gold ontology 或 scoring reference。
2. 不要声称访问了 live Web、登录、点击或执行 JS。
3. 不要补充 page map / HTML 中没有出现的页面、链接或角色。
4. 不要用外部系统常识补全完整采购流程。
5. 不要把本任务输出当作最终融合 ontology；它只是 Web navigation / flow analysis。
```

## 输出文件名

`results/<evaluation_id>/normalized_outputs/task_13_page_map_to_business_flow.json`

同时保存：

- 原始输出：`results/<evaluation_id>/raw_outputs/task_13_page_map_to_business_flow_raw.md`
- task result wrapper：`results/<evaluation_id>/task_13_page_map_to_business_flow_result.json`

## 输出格式

- 单个合法 JSON 对象。
- 字段名使用英文。
- 重点输出流程和导航分析，不要求兼容完整 ontology schema。
- `input_mode` 必须是 `page_map_only`、`html_snapshot_with_page_map` 或未来明确提供的其他模式。

## Evidence 要求

- 每个页面流程、角色路径、导航边、缺页说明都必须包含 evidence。
- 可引用 `web_map/page_map.json#<page_id>`、`web_map/page_map.md#recommended-crawl-order`、`web_snapshots/<file>.html#<page_id>`。
- 导航边建议同时记录 `from_page_id`、`to_page_id`、`link_source` 和 `evidence_refs`。
- 不得引用 evaluator-only gold、known conflicts、demo outputs 或 scoring 输出。

## 不确定性要求

- page_map_only 不能声称 HTML DOM 已解析。
- 页面图不完整、缺页、断链、重复模板和角色可见性都应写入 uncertainties。
- 页面路径只是候选业务流程；不得声称唯一、完整或已验证后端实现。

## 禁止幻觉要求

- 不得声称 live crawl、登录、点击、JS 执行、API 调用、浏览器自动化或真实网络可达性。
- 不得补充未提供页面、未出现链接、未出现角色或未出现状态。
- 不得根据外部采购系统常识填补未提供的页面流程。
- 不得把 page map 中的导航线索当作最终权限规则或最终业务规则。

## 无法访问 Web 时的 HTML snapshot 降级

- 工具不能访问 live Web 但能读 HTML：使用 `html_snapshot_with_page_map`，基于静态 href 和可见文本复核 page map。
- 工具不能读 HTML 但能读 page map：使用 `page_map_only`，只分析 page map 已声明内容。
- 工具只能读取部分 HTML：记录处理页面清单和缺失页面。
- HTML 中 JS 动态链接不可见：写入 uncertainty，不要编造运行后链接。

## 允许追问次数

最多 1 次。只允许追问 page map 是否完整、HTML 是否可用，或输入模式应为 `page_map_only` 还是 `html_snapshot_with_page_map`。

## 常见失败

- 把 page map 当作 gold answer。
- 没有声明 `input_mode`。
- 导航边没有 evidence。
- 编造未提供页面或链接。
- 声称 live crawl 或真实点击。
- 输出完整本体而不是页面流程分析。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-13",
  "status": "failed",
  "failure_type": "invalid_json | missing_evidence | wrong_input_mode | claimed_live_web | invented_pages | wrong_output_type | hallucination | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_13_page_map_to_business_flow_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 复制 prompt 时只复制 fenced code block 内的内容；不要把操作员步骤、输出文件名说明、gold/reference 路径或 scoring 输出复制给被评估 AI。
