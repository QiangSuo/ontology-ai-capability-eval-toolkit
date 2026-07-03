# B1 截图能力扩展设计方案

> 本文仅做设计，不包含实现、数据创建、提示词落地或评分代码修改。B1 是现有采购合同 MVP 的可选 UI / 截图理解扩展，不改变当前 MVP 基线、Task 06 schema repair、Task 07 final report generation 或 `results/demo_baseline` 的可评分性。

## 1. 目标与边界

### 1.1 目标

- 评估 AI 工具是否能从给定 UI 截图或等价降级输入中识别页面对象、字段、按钮、状态、动作、角色线索，并映射到本体元素。
- 验证截图来源的 UI 证据是否能与代码、DDL、CSV 样例数据、文档证据融合，而不是生成重复概念或无证据结论。
- 为后续 B2/B3/B5 阶段预留输入、提示词、schema 约定和评分信号，但 B1 本身不创建截图、不写 prompt、不改 scorer。
- 在工具不能看图时明确降级模式、评分上限和幻觉红线，避免把 OCR/文本替身误报为真实视觉能力。

### 1.2 非目标

- 不实现真实截图采集、浏览器自动化、OCR 评分或图像区域识别。
- 不扩展 live Web / recursive crawling；截图扩展与 Web 快照能力保持分离。
- 不把截图能力加入 MVP 必选基线；没有 B1 输入时，UI / 截图域应为 `N/A` 或 `Blocked`，并按现有评分口径披露。
- 不把 evaluator-only gold/reference 文件提供给被测 AI。

## 2. 被评估能力

B1 主要评估以下能力：

- 页面理解：识别列表页、详情页、编辑页、审批页等页面类型和业务目的。
- UI 元素抽取：识别可见字段、表格列、按钮、菜单、状态标签、提示信息、角色/权限线索。
- UI 到本体映射：将页面字段映射到 attributes，将按钮映射到 actions，将状态标签映射到 states，将页面/业务对象映射到 concepts、relations 或 mappings。
- 多源融合：将 UI 术语与代码、数据库、样例数据、文档中的术语对齐，记录别名、冲突和不确定性。
- 证据链：每个截图来源结论必须有可复核的 screenshot evidence 引用。
- 幻觉控制：不能看到图片时必须说明限制；不能宣称“看到了”具体 UI 细节。

## 3. CAPABILITY_MODEL 映射

- 主域：`3.5 UI / 截图理解能力`。覆盖页面对象、字段、按钮、状态、动作、角色、截图证据、可见文本和 UI 到业务对象映射。
- 次域：`3.8 多源融合能力`。截图术语必须与 code / DDL / CSV / document 输出融合，冲突要显式记录。
- 次域：`3.9 结构化输出能力`。截图输出需要 schema-valid JSON、稳定 task_result wrapper、可被 `score_auto.py` 发现。
- 次域：`3.11 证据链与可追溯能力`。截图来源的 ontology element 必须有 `evidence_id`、`source_ref` / `content_ref` 或可复核路径。
- 次域：`3.14 幻觉控制能力`。无图能力工具不得宣称视觉观察；OCR / surrogate-only 运行必须标注并封顶。
- 次域：`3.15 中文政企业务理解能力`。中文 UI 标签可能暴露别名、审批语义、角色权限和工作流状态。

## 4. 新输入设计

### 4.1 可选输入包

B1 输入应作为可选 supplement，例如：

```text
datasets/generic_procurement_contract_mvp/screenshots/
metadata/screenshot_manifest.json
datasets/generic_procurement_contract_mvp/gold/gold_screenshot_evidence_map.json
datasets/generic_procurement_contract_mvp/gold/known_screenshot_conflicts.json
```

其中 `gold/*` 仅供 evaluator / scorer 使用，不提供给被测 AI。

### 4.2 manifest 字段

建议 `screenshot_manifest.json` 包含：

- `screenshot_id`
- `page_id`
- `page_name` / `page_title`
- `page_type`：list、detail、edit、approval、payment 等。
- `image_path`：PNG/JPG 相对路径；无真实图片时为空或缺省。
- `surrogate_path`：`.screen.md` 文本替身路径。
- `ocr_text_path`：可选 OCR 文本路径。
- `role_context` / `view_context`
- `capture_context` / `viewport`
- `input_mode`
- `known_limitations`

### 4.3 evaluator-only gold

截图 gold 应记录但不泄漏给 AI：

- 关键可见字段、表格列、按钮、状态、动作、页面目的。
- UI-to-ontology 期望映射。
- 截图特有冲突，例如 UI label 与 DB/code/document 命名不一致。
- 评分所需 evidence handles、page_id、ui_area、visible_text 或 region_ref。

## 5. 截图替身与 PNG 的关系

B1 必须区分四类模式：

| 模式 | 含义 | 可评估内容 | 不可声称内容 |
|---|---|---|---|
| `real_image` | 工具直接处理 PNG/JPG | 视觉截图理解、UI 元素识别、证据引用 | 仍需人工复核业务映射 |
| `image_plus_surrogate` | 图片加 OCR/人工转写辅助 | 图像理解 + 文本辅助推理 | 不能把 surrogate 当 gold |
| `ocr_text_only` | 只有 OCR 文本，无图像视觉处理 | UI 文本语义和部分映射 | 不能声称布局、图标、视觉区域识别 |
| `surrogate_only` | 只有 `.screen.md` 或人工页面描述 | 离线稳定的 UI 语义抽取 | 不能报告为真实截图视觉能力 |

Surrogate 是可访问性/降级输入，不等价于 PNG。它可测试可见文本、字段、动作和业务语义映射，但不测试 OCR 鲁棒性、空间布局、图标识别或视觉歧义处理。

## 6. 新提示词设计

B1 不立即新增提示词；后续建议使用不冲突编号：

- `task_08_screenshot_to_ontology.md`：读取截图、manifest、允许的 OCR/surrogate 输入，输出 `ui_ontology.json` 和 screenshot evidence。
- `task_09_screenshot_fusion.md` 或并入后续 fusion prompt：将 UI 输出与既有 ontology supplement 融合，保留冲突和不确定性。
- `task_10_screenshot_repair.md` 如确有需要，只做 JSON/schema 修复，不得新增原输出没有的视觉事实。
- `task_11_screenshot_report.md` 如确有需要，消费机器分和人工评审，不得在 `human_review.status=pending` 时宣称 ready。

提示词必须要求：

- 声明 `input_mode`。
- 若不能看图，明确说明限制，只能基于 OCR/surrogate 推理。
- 每个 UI-derived concept / attribute / action / state / role / mapping 都引用 screenshot evidence。
- UI 与 backend/document 冲突时写入 conflicts / uncertainties，不静默覆盖。
- 不读取或引用 `gold_screenshot_evidence_map`、`known_screenshot_conflicts`。

## 7. Schema 字段扩展

### 7.1 现有 schema 可复用能力

- `schemas/evidence.schema.json` 已支持 `evidence_type = screenshot`，并为 screenshot evidence 提供 `image_path`、`ui_area`、`ocr_text`、`annotations` 等字段。
- `schemas/ontology.schema.json` 已允许 `mappings.source_type = screenshot`，ontology 元素也可通过 `evidence_refs` 引用截图证据。
- UI 字段可表达为 attributes，按钮可表达为 actions，状态可表达为 states，角色可表达为 roles/permissions，页面到业务对象的连接可表达为 mappings 或 relations。

### 7.2 B1 建议约定

最小可行设计不要求破坏性 schema 修改。若需要更强自动评分，可先在 metadata / annotations 中约定以下字段：

- `input_mode`
- `page_id`
- `page_name`
- `ui_element_type`
- `visible_text`
- `role_context`
- `region_ref`
- `normalized_bbox` 或 `bounding_box`（可选，不作为 MVP 必填）
- `surrogate_ref`
- `screenshot_path`
- `ocr_confidence`
- `extraction_limitations`
- `source_type = screenshot`

若后续 B5 要做区域级自动评分，再考虑把 `region_id`、`bbox`、`visible_text`、`element_type` 提升为结构化 schema 字段。

## 8. 证据类型

B1 应支持以下证据形态：

- 真实截图证据：`source.type = image`，`evidence_type = screenshot`，`screenshot.image_path` 或 `content_ref` 指向图片。
- OCR 辅助证据：仍可为 screenshot evidence，但需标注 OCR 来源、置信度和限制；只基于 OCR 的结论降低置信度。
- Surrogate 文本证据：无图片时不得伪装为 direct visual evidence；应标注 `input_mode = surrogate_only`，并在 source / metadata 中说明来源。
- Manifest 证据：连接 page_id、image_path、surrogate_path、OCR path、role/context 和限制。
- 区域/注释证据：使用 `ui_area`、`annotations`、`region_ref` 或未来 bbox 字段支持字段/按钮/状态定位。
- 跨源证据：截图可支持 mappings、conflicts、uncertainties，但不能无人工评审地覆盖 code / DDL / document 证据。

## 9. 已知冲突与任务编号碰撞

### 9.1 能力与 MVP 状态冲突

- CAPABILITY_MODEL 已把 UI / 截图理解列为一等能力域，但当前 MVP closure 明确没有截图输入、OCR 约定或截图 evidence scoring。
- evidence schema 支持 screenshot，不代表 scorer 已具备截图评分能力。
- ontology schema 支持 `source_type = screenshot`，但没有一等 page/screen entity；B1 需使用 convention 或后续 schema 扩展。
- scoring README 的通用 evidence discovery 不等价于 screenshot-specific validation。

### 9.2 任务编号碰撞

必须避免以下命名：

- `task_06_screenshot_to_ontology.md`：会与现有 `task_06_schema_repair.md` 冲突。
- `task_07_web_snapshot_to_ontology.md`：会与现有 `task_07_final_report_generation.md` 冲突，也会混淆 Web 与 screenshot 边界。

建议从 `task_08_screenshot_to_ontology.md` 开始，或采用 `b1_task_01_*` 的独立命名空间。不要重编号现有 MVP tasks。

### 9.3 业务冲突类型

B1 应显式记录：

- `ui_vs_database_naming_mismatch`
- `ui_vs_document_rule_mismatch`
- `role_permission_ui_vs_doc_mismatch`
- `button_action_ambiguity`
- `visible_status_mismatch`
- `screenshot_only_business_term`

## 10. score_auto 需要的变化

B1 只提出设计需求，后续实现应满足：

- feature-gated：仅当存在 screenshot manifest、B1 task result 或 `--enable-screenshot-b1` 时启用。
- 保持 baseline：无 B1 输入时，当前 `machine_metrics`、coverage、evidence、hallucination 语义不变。
- 发现 B1 task_result wrappers、`ui_ontology.json`、`evidence_map.json` 和 normalized outputs。
- 校验 screenshot evidence：`evidence_type=screenshot`、`source.type=image/file`、`image_path` / `content_ref` 存在、`evidence_id` 被 ontology `evidence_refs` 正确引用。
- 计算 UI coverage：关键字段、按钮/动作、状态、页面目的、角色线索。
- 计算 screenshot hallucination candidates：声称的 UI 字段/按钮/状态/动作不在 manifest、OCR、visible text 或 gold 中。
- 识别 `input_mode` 并应用 caps / redlines。
- 输出 `b1_screenshot_metrics`，不要默认并入现有 core concept / key attribute / key relation coverage。

建议指标：

- `screenshot_evidence_file_count`
- `referenced_screenshot_evidence_count`
- `missing_screenshot_ref_count`
- `invalid_screenshot_path_count`
- `ui_source_type_mapping_count`
- `key_visible_field_coverage`
- `key_button_action_coverage`
- `key_status_coverage`
- `screenshot_conflict_recall`
- `screenshot_hallucination_candidate_count`
- `input_mode_cap_applied`

## 11. 降级规则

- `real_image` 不可用但有 OCR/surrogate：允许降级运行，但必须标注模式并封顶。
- `surrogate_only`：可评估 UI 语义抽取和映射，不能评估真实视觉截图能力。
- `ocr_text_only`：布局、图标、空间区域、视觉层级均需标记不确定。
- 无图片也无 surrogate：`3.5 UI / 截图理解能力` 标记 `N/A` 或 `Blocked`。
- region 坐标不可用：可做 page-level / ui_area / visible_text smoke test，区域级定位交给人工评审并封顶。
- OCR 质量差：要求 uncertainties/confidence，不得把 OCR 文本直接提升为确定业务事实。
- 工具宣称看到了无图输入中的具体视觉内容：视为幻觉控制红线。

## 12. 评分上限影响

- 无 B1 bundle：UI / 截图域 `N/A`，不影响现有 code / DDL / sample / document / fusion / evidence 域评分，但报告需披露未测风险。
- 客户关键 POC 需要截图但权限导致不可测：标记 `Blocked`，触发准入限制。
- `surrogate_only`：真实视觉理解不得给 A/B；最多只能说明 UI 文本语义能力，建议封顶 C 或按 rubric 标记 N/A。
- `ocr_text_only`：若布局、角色、按钮结构无法可靠还原，应低于 surrogate-rich 模式。
- 缺少图片路径、区域/文本 locator 或 manifest 链接：证据链与多源融合应封顶，因为 reviewer 无法复核 UI 来源。
- 截图 claim 无 evidence_refs：增加 evidence / hallucination 风险，不应提高分数。
- B1 成功最多影响 CAPABILITY_MODEL 中 UI / 截图相关权重，不得改变既有 MVP 基线域的可比性。

## 13. 实施步骤建议

B1 之后可按以下阶段推进：

1. B1：完成本设计文档，冻结输入模式、编号规则、证据约定、score cap 和验收标准。
2. B2：创建可选 screenshot / surrogate 数据包，例如 `.screen.md`、manifest、README；gold 仍放 evaluator-only 路径。
3. B3：新增 `task_08_screenshot_to_ontology.md`，要求 input_mode、degradation、evidence、uncertainty 和 no-hallucination。
4. B4：新增可选 screenshot gold evidence / conflict 文件，不触碰原始 `gold_evidence_map.json` 或 `known_conflicts.json`。
5. B5：在 `score_auto.py` 中实现 opt-in B1 metrics，确认 `results/demo_baseline` 仍可按原语义评分。
6. B6：补充人工评审模板，覆盖页面目的、UI-to-business mapping、OCR/替身限制、冲突处理和 redline。

## 14. 验收标准

- 设计明确声明 B1 只设计、不实现，并保持 MVP baseline 向后兼容。
- 现有 Task 06 schema repair 和 Task 07 final report generation 不改名、不重编号。
- 截图 prompt 编号不冲突，推荐 `task_08_screenshot_to_ontology.md` 或独立 `b1_task_*` 命名空间。
- 明确定义 allowed inputs、forbidden evaluator-only gold、output artifacts、task IDs、evidence conventions、scoring signals、manual review 和 score caps。
- B1 run 可产生 schema-valid `ui_ontology.json`、`evidence_map.json`、task_result wrapper，并被后续 scoring flow 发现。
- 每个截图来源 ontology element 都引用可复核 screenshot `evidence_id`。
- 自动检查能区分 `real_image`、`image_plus_surrogate`、`ocr_text_only`、`surrogate_only`，并应用 cap/redline。
- 人工评审能判断页面目的、UI-to-business mapping、OCR 不确定性、冲突和最终 UI / 截图等级。
- 文档明确说明：当前 MVP 仍为 Conditional Go；截图能力在扩展实现和验证前不算已 ready。

## 15. 风险

- schema 已支持 screenshot 但 scorer 未实现截图专项评分，容易被误解为已具备能力。
- surrogate-only 可能被高估为真实视觉理解，必须强制 input_mode 和 score cap。
- 截图 gold 若放入 AI 输入会泄漏答案；OCR helper 必须只包含可见文本，不包含期望本体映射。
- 把 B1 metrics 默认并入现有 `machine_metrics` 会破坏 demo baseline 和历史结果可比性。
- UI 标签若权重过高，可能错误覆盖 DDL/code/document 的更强证据；应记录冲突和不确定性。
- 当前阶段/任务编号中已有 Task 06/07，新增 screenshot task 若复用编号会误导操作员和自动发现。
- 必填 bbox / pixel-level 字段会排除能语义读图但不能稳定输出坐标的工具；B1 应先以 page-level / ui_area / visible_text 为主。
- 客户环境可能禁止保存图片；此时应使用 manifest + OCR/surrogate provenance，并标记 N/A/Blocked 或封顶。
