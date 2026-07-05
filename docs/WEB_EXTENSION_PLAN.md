# C1 Web 页面快照与页面地图扩展设计方案

> 本文仅做设计，不包含 HTML 创建、page map 创建、prompt 落地、gold 文件扩展或评分代码修改。C1 是现有采购合同 MVP 与 B 阶段 screenshot surrogate 扩展之后的可选 Web 能力扩展，不改变 MVP baseline、screenshot demo、Task 06 schema repair、Task 07 final report generation 或既有 demo 的可评分性。

## 1. 目标与边界

### 1.1 目标

- 评估 AI 工具是否能基于离线 HTML snapshot 和 page map 理解系统页面、菜单、链接、表单、按钮、状态、业务对象和流程路径。
- 验证 Web 页面来源证据是否能与 code / DDL / CSV / document / screenshot surrogate 证据融合，而不是生成重复概念或无证据页面功能。
- 为后续 C2-C7 阶段预留输入目录、page map 字段、prompt 编号、evidence 约定、known conflicts 和最小 scoring 信号。
- 在工具不能访问 live Web 或不能递归爬取时，提供 offline snapshot 降级路径，并明确不能把 snapshot 分析误报为真实 live crawler 能力。

### 1.2 非目标

- 不实现真实递归爬虫、浏览器自动化、登录态处理、JS 执行、网络访问或截图采集。
- 不做图算法评分、真实可达性验证、性能测试、accessibility audit 或安全扫描。
- 不把 Web 能力加入 MVP 必选基线；没有 C 输入时，Web 递归分析域应为 `N/A` 或 `Blocked`，并按现有评分口径披露。
- 不让 evaluator-only gold/reference 文件进入被测 AI 输入。
- 不让 `results/demo_baseline/` 或 `results/demo_screenshot/` 依赖 Web 文件。

## 2. 被评估能力

C 阶段主要评估以下能力：

- 页面识别：识别首页、列表页、详情页、工作台、审批页、发票/付款页等页面类型和业务目的。
- 导航理解：识别菜单、面包屑、页面标题、链接关系、入口页和下钻路径。
- 表单与表格抽取：识别字段、筛选条件、表格列、按钮、状态标签和角色线索。
- 页面到本体映射：将页面、字段、按钮、链接和流程路径映射到 concepts、attributes、relations、actions、states、mappings。
- 页面流程分析：从 page map 和链接关系中识别采购申请、合同、订单、收货、发票、付款等跨页面业务路径。
- 多源融合：将 Web 术语与 code / DDL / CSV / documents / screenshot surrogate 中的术语对齐，记录别名、冲突和不确定性。
- 证据链：每个 Web-derived 结论必须引用 HTML snapshot 或 page map evidence。
- 幻觉控制：不得编造未提供页面、链接、按钮、接口、登录状态或动态行为。

## 3. CAPABILITY_MODEL 映射

- 主域：`3.6 Web 递归分析能力`。覆盖 HTML snapshot、page map、页面识别、链接关系、业务路径和页面 evidence。
- 次域：`3.8 多源融合能力`。Web 术语必须与 code / DDL / CSV / document / screenshot 输出融合，冲突需显式记录。
- 次域：`3.9 结构化输出能力`。Web 输出需要 schema-valid JSON、稳定 task_result wrapper、可被 `score_auto.py` 发现。
- 次域：`3.11 证据链与可追溯能力`。Web 来源 ontology element 必须有 `web:*` evidence handle、HTML path、page_id 或 DOM/source locator。
- 次域：`3.14 幻觉控制能力`。offline snapshot 不得被描述为 live crawling；缺页、断链和动态内容不可见必须写入 uncertainties。
- 次域：`3.15 中文政企业务理解能力`。中文菜单、按钮、流程页标题可能暴露业务别名、审批语义和角色权限。

## 4. Web snapshot 与真实递归爬虫的关系

C 阶段必须区分四类模式：

| 模式 | 含义 | 可评估内容 | 不可声称内容 |
| --- | --- | --- | --- |
| `live_crawl` | 工具可访问 live Web 并递归浏览 | 真实可达性、页面发现、动态链接观察 | 仍需权限/登录/环境记录 |
| `html_snapshot` | 工具读取离线 HTML 文件 | 页面结构、表单、链接、静态 DOM 语义 | 不能声称访问了 live 系统 |
| `page_map_only` | 只有 page map，无 HTML | 页面清单、链接关系、流程推理 | 不能声称解析了 DOM 或看到了页面字段 |
| `manual_page_notes` | 只有人工页面描述 | 低保真页面语义 | 不能声称递归分析或自动页面发现 |

MVP 的 C 阶段建议从 `html_snapshot` + `page_map` 起步。它可以稳定测试页面语义和链接关系，但不测试登录态、动态 JS、真实浏览器、网络权限或爬虫鲁棒性。

## 5. 新增输入数据结构

### 5.1 可选输入包

建议新增以下可选输入目录：

```text
datasets/generic_procurement_contract_mvp/web_snapshots/
datasets/generic_procurement_contract_mvp/web_map/page_map.json
datasets/generic_procurement_contract_mvp/web_map/page_map.md
datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.json
datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.md
datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.json
datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.md
```

其中 `gold/*` 仅供 evaluator / scorer 使用，不提供给被测 AI。

### 5.2 HTML snapshot 建议页面

C2 可创建以下离线 HTML 页面：

- `web_snapshots/index.html`：系统首页 / 模块入口。
- `web_snapshots/purchase_requests.html`：采购申请列表。
- `web_snapshots/purchase_request_detail_PR-2024-001.html`：采购申请详情。
- `web_snapshots/approval_tasks.html`：审批任务工作台。
- `web_snapshots/contracts.html`：合同列表。
- `web_snapshots/contract_detail_CT-2024-001.html`：合同详情。
- `web_snapshots/invoices.html`：发票列表或匹配页。
- `web_snapshots/payments.html`：付款申请列表或工作台。

HTML 应包含菜单、页面标题、字段、状态、按钮、表格、链接、面包屑、角色提示和轻微术语差异。HTML 不需要后端，也不应包含 gold answer。

### 5.3 page map 字段

`page_map.json` 建议包含：

- `page_id`
- `url_or_file`
- `title`
- `page_type`
- `menu_path`
- `breadcrumb`
- `visible_concepts`
- `visible_fields`
- `visible_actions`
- `visible_states`
- `outgoing_links`
- `incoming_links`
- `required_role`
- `evidence_refs`
- `crawl_notes`
- `input_mode`
- `known_limitations`

`page_map.md` 应解释推荐遍历顺序、核心业务流程页面、重复页面、权限/角色线索、断链/缺页和用于测试递归分析能力的点。

## 6. HTML snapshot 设计原则

- 使用纯静态 HTML，避免依赖外部 CDN、真实登录、后端接口或构建步骤。
- 页面之间使用相对链接，确保离线可读和可检查。
- 每个页面包含稳定 `data-page-id` 或可读 `<title>`，便于 evidence locator。
- 关键 UI 元素应有可读文本，例如 label、table header、button text、status badge。
- 页面内容应与现有 DDL / 文档 / source code 有可融合关系，但保留轻微命名差异。
- 不要在 HTML 中嵌入 expected ontology、gold evidence、known conflict 或评分提示。
- 可以包含少量故意断链或权限提示，但必须在 page map 中说明，避免被误判为文件缺失。

## 7. page map 设计原则

- page map 是输入侧页面清单和导航说明，不是 gold answer。
- `evidence_refs` 应引用真实存在的 HTML 文件或 page map 位置。
- `outgoing_links` 应能形成可复核的页面图。
- `required_role` 只表示页面/链接可见性线索，不等价于最终权限规则。
- `crawl_notes` 应说明 offline snapshot、缺失动态内容、重复页面模板、断链和角色限制。
- page map 不应泄漏 evaluator-only expected resolution。

## 8. 新增 prompts

Web prompt 不应占用现有 Task 06 / Task 07，也不应覆盖 Task 08 screenshot。建议从 Task 12 开始，保留 Task 09-11 给 screenshot fusion / screenshot repair / screenshot report 预留空间：

- `task_12_web_snapshot_to_ontology.md`：读取 HTML snapshots 和 page map，输出 Web-derived ontology supplement 和 web evidence。
- `task_13_page_map_to_business_flow.md`：从 page map 和链接关系生成页面流程 / 模块路径分析。
- `task_14_extended_multi_source_fusion.md`：将 Web 输出与 code / DDL / CSV / documents / screenshot outputs 融合。

提示词必须要求：

- 声明 `input_mode`：`html_snapshot`、`page_map_only` 或其他降级模式。
- 若不能访问 live Web，明确说明只基于 offline HTML/page map。
- 每个 Web-derived concept / attribute / action / state / flow / mapping 都引用 `web:*` evidence。
- 页面缺失、断链、动态内容不可见时写入 `uncertainties`。
- 不读取或引用 `gold_evidence_map.web.*`、`known_conflicts.web.*`、demo outputs 或 scoring outputs。

## 9. 新增 evidence 类型

现有 `schemas/evidence.schema.json` 已支持 `evidence_type = web_page`，并为 web evidence 提供 URL、title、DOM path、text snippet 等字段。C 阶段可先使用最小约定：

- `evidence_id`：例如 `web:purchase_requests.table.pr_no`。
- `evidence_type`：`web_page`。
- `source.type`：`file` 或 `website`。
- `content_ref`：离线 HTML 相对路径，例如 `web_snapshots/purchase_requests.html`。
- `locator`：页面标题、CSS selector、DOM path、link text 或 section label。
- `web_page.url`：可使用 snapshot file path 或模拟 URL。
- `web_page.title`：HTML title 或页面标题。
- `web_page.dom_path`：可选 CSS selector / DOM path。
- `web_page.text_snippet`：可见文本片段。
- `metadata.input_mode`：`html_snapshot` / `page_map_only`。

如果只有 page map，无 HTML，则 evidence 仍可引用 `web_map/page_map.json`，但不能声称解析了 DOM。

## 10. 新增 known conflicts

C5 建议新增 evaluator-only Web conflicts：

- `web_vs_document_flow_mismatch`：页面路径与业务文档流程顺序存在轻微差异。
- `page_action_without_backend_evidence`：页面按钮存在，但代码/DDL/文档未确认后端动作。
- `ui_vs_database_naming_mismatch`：页面术语与 DDL/code/document 命名不一致。
- `role_permission_web_vs_doc_mismatch`：菜单/按钮可见角色与文档权限矩阵不完全一致。
- `missing_page_or_broken_link`：page map 声明链接但 snapshot 缺失或故意断链。
- `web_only_business_term`：页面出现仅 Web 来源支持的业务词。

这些 conflicts 用于人工复核和可选 scoring，不应在 prompt 输入中泄漏。

## 11. scoring 最小扩展范围

C6 只做可选 Web evidence 支持，不做真实爬虫评分或图算法评分。

最小要求：

- 可选读取 `gold_evidence_map.web.json`，不存在则跳过。
- 支持 `source_type = web_page` 或 `evidence_type = web_page`。
- 把 `web:*` evidence_id、HTML path、page_map path 加入 available evidence refs。
- 在 `machine_score.json` 的 `evidence_check.web_evidence` 中输出 Web evidence 摘要。
- 在 `machine_score.md` 中增加 Web evidence 覆盖摘要。
- 保持 `results/demo_baseline/` 和 `results/demo_screenshot/` 可评分。
- 不把 Web coverage 默认并入 MVP core concept / key attribute / key relation coverage。

建议指标：

- `gold_web_evidence_count`
- `referenced_web_evidence_count`
- `matched_web_evidence_count`
- `missing_web_evidence_ref_count`
- `invalid_web_snapshot_path_count`
- `page_map_file_count`
- `input_mode`
- `web_evidence_enabled`

## 12. 降级路径

- 工具不能访问 live Web 但能读 HTML：使用 `html_snapshot`，不得声称 live crawl。
- 工具不能读 HTML 但能读 page map：使用 `page_map_only`，只能分析页面清单和链接关系。
- 工具只能复制粘贴页面片段：使用 `manual_page_notes`，需要记录复制范围和缺失页面。
- HTML 中 JS 动态内容不可见：必须写入 `uncertainties`，不能编造运行后 DOM。
- 登录/权限页面不可用：标记 `Blocked` 或 page-level uncertainty。
- 工具声称访问了未提供 URL、点击了未提供页面或发现了未提供链接：作为幻觉控制风险处理。

## 13. 评分上限影响

- 无 Web bundle：Web 递归分析域 `N/A`，不影响 MVP code / DDL / sample / document / fusion / screenshot surrogate 结果。
- 只有 `page_map_only`：不能给 live recursive crawling 高分，最多说明页面图理解能力。
- 只有离线 HTML snapshot：可评估静态页面语义和链接关系，不能声称登录态、动态 JS 或真实可达性。
- 缺少 evidence refs：Web evidence / traceability 应封顶。
- 编造未提供页面或链接：触发幻觉红线风险。
- 客户关键 POC 依赖 live Web/browser automation 但环境不可测：标记 `Blocked`，触发准入限制。

## 14. 实施步骤建议

1. C1：完成本设计文档，冻结 Web 输入、prompt 编号、evidence、known conflicts、scoring scope 和验收标准。
2. C2：创建 `web_snapshots/` HTML 文件，不改 gold/scoring/prompt。
3. C3：创建 `web_map/page_map.json` 和 `page_map.md`，确保所有 evidence refs 指向真实 HTML 或 page map 文件。
4. C4：创建 `task_12_web_snapshot_to_ontology.md`、`task_13_page_map_to_business_flow.md`、`task_14_extended_multi_source_fusion.md`。
5. C5：新增 `gold_evidence_map.web.*` 和 `known_conflicts.web.*`，不覆盖 baseline gold。
6. C6：最小扩展 `score_auto.py` 支持 optional Web evidence，验证 demo_baseline 和 demo_screenshot 不受影响。
7. C7：创建 `results/demo_web/`，演示 Web snapshot / page map 能力如何被评分。

## 15. 验收标准

- `WEB_EXTENSION_PLAN.md` 明确 C1 只设计、不实现，并保持 MVP 与 screenshot baseline 向后兼容。
- Web 输入、gold/reference、demo/scoring 的边界清楚，避免向被测 AI 泄漏 gold。
- 明确区分 `live_crawl`、`html_snapshot`、`page_map_only`、`manual_page_notes`。
- Web prompt 编号不冲突，推荐从 `task_12` 开始。
- Web evidence 约定可被后续 scoring flow 发现，并不破坏现有 MVP metrics。
- 后续 C2/C3 可据此创建离线 HTML 和 page map。
- 人工评审能判断页面目的、流程路径、链接关系、UI-to-business mapping、缺页/断链和最终 Web 等级。
- 文档明确说明：当前 MVP 和 screenshot surrogate 扩展不等于 Web live crawler ready。

## 16. 风险

- HTML snapshot 容易被误解为 live Web 访问；必须强制 input_mode 和 score cap。
- Page map 可能过度提示业务流程；应保持输入清单性质，不泄漏 expected ontology。
- Web 页面按钮可能被误当作后端已实现能力；需要与 code/document 融合确认。
- Web evidence 默认并入 MVP coverage 会破坏历史可比性；必须保持 optional additive。
- 任务编号若复用 Task 06/07/08 会误导操作员和自动发现。
- 客户环境可能禁止导出 HTML；需要 page_map_only 或 manual_page_notes 降级，并在报告中封顶。
- 动态 JS、隐藏菜单、权限差异和登录态无法通过静态 snapshot 完整评估，必须写入 limitations。
