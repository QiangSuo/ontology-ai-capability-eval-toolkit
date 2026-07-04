# Task 14: 扩展多源融合（含 Web）

## 任务目标

融合 MVP 多源本体输出、可选 screenshot surrogate 输出、Web snapshot 输出和 page map flow 输出，生成扩展统一本体或融合补充。重点测试 AI 工具能否处理 code / DDL / CSV / documents / screenshot surrogate / Web snapshot / page map 之间的证据层级、命名差异、冲突、不确定性和能力边界。

## 输入材料

按本轮评估实际启用范围提供以下输入：

- `results/<evaluation_id>/normalized_outputs/task_05_multi_source_fusion.json`
- 可选：`results/<evaluation_id>/normalized_outputs/task_08_screenshot_to_ontology.json`
- 可选：`results/<evaluation_id>/normalized_outputs/task_12_web_snapshot_to_ontology.json`
- 可选：`results/<evaluation_id>/normalized_outputs/task_13_page_map_to_business_flow.json`
- 可选原始复核材料：`web_snapshots/*.html`、`web_map/page_map.json`、`web_map/page_map.md`、`screenshots/*.screen.md`
- 可参考 schema：`schemas/ontology.schema.json`、`schemas/evidence.schema.json`、`schemas/task_result.schema.json`

禁止提供给被评估 AI：

- `datasets/generic_procurement_contract_mvp/gold/`
- `results/demo_baseline/`
- `results/demo_screenshot/`
- `results/demo_web/`（如未来存在）
- `machine_score.json`、`machine_score.md`、人工复核内容或 evaluator-only Web / screenshot gold/conflict 文件

## 操作员步骤

1. 确认已完成 Task 05；按评估启用范围确认 Task 08、Task 12、Task 13 是否存在。
2. 将已启用任务的 normalized outputs 提供给 AI 工具；必要时补充少量原始 Web / screenshot 片段用于 evidence 复核。
3. 明确声明输入模式组合，例如 `mvp_plus_web_snapshot`、`mvp_plus_screenshot_plus_web` 或 `mvp_plus_page_map_only`。
4. 要求 AI 生成统一扩展本体或融合补充，不要简单拼接多个输出。
5. 要求 AI 保留 evidence、alias、mapping、conflict、uncertainty、confidence 和 provenance。
6. 保存原始输出；若 JSON 不合法，允许一次 schema repair。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 扩展多源融合任务。请基于我提供的 Task 05 多源融合输出，以及可选的 Task 08 screenshot surrogate 输出、Task 12 Web snapshot 输出、Task 13 page map flow 输出，生成扩展统一本体 JSON 或融合补充。不要简单拼接多份结果，必须去重、归并、融合并保留证据、冲突和不确定性。

【重要输入模式声明】
请在输出中声明 input_mode。可用值包括 mvp_plus_web_snapshot、mvp_plus_page_map_only、mvp_plus_screenshot_plus_web、mvp_only_with_optional_outputs_missing 或其他准确描述本轮输入的模式。Web snapshot 不等于 live Web；screenshot surrogate 不等于真实图片或 OCR。

【任务目标】
生成采购合同 MVP 扩展统一本体，覆盖 concept、attribute、relation、event、rule、action、state、role、permission、alias、mapping、conflict、uncertainty、confidence、evidence_refs、provenance、source_coverage 和 fusion_decisions。

【融合原则】
1. 以 Task 05 为 MVP baseline ontology，不覆盖或删除已有多源结论；Web / screenshot 输出作为 optional additive evidence。
2. 同义词归并：Supplier/Vendor；Purchase Request/PR；Purchase Order/PO；Goods Receipt/GRN；Payment Request/Payment Application。
3. Web / screenshot 支持的 UI label、button、status、role visibility 是 UI evidence，不等于后端能力或最终权限规则。
4. 多源一致时提高 confidence；仅 Web 或仅 screenshot 支持时保留但降低 confidence，并标记 source_specific_candidate。
5. 来源冲突时不要强行选择，写入 conflicts，并说明来源差异和建议复核方式。
6. 页面流程可支持业务路径候选，但不能证明唯一流程、live crawl 成功或后端事务完成。
7. 不要为了完整性创造没有来源支持的对象、字段、关系、规则、页面或动作。

【必须检查的融合点】
- Vendor/Supplier 是否归并，并保留 UI 与文档/DDL 命名差异。
- PR/Purchase Request 是否归并，并与 Purchase Order / PO 保持边界。
- GRN/Goods Receipt 是否归并，并说明是否只有 Web/screenshot 页面支持 GRN label。
- Payment Application/Payment Request 是否归并，并保留菜单、页面和 DDL-style label 差异。
- Approval Task 的 Target Type / Target No 是否作为 polymorphic approval target 候选处理。
- UI 中的 Activate Contract、Create Purchase Order、Match Invoice、Mark Paid、Release Hold 等按钮是否仅作为候选 action，等待 code/document 复核。
- Difference % / matching tolerance UI 指标是否与 policy 或 code 存在潜在阈值差异。
- Held payment 的 Hold Reason 是否只是操作界面线索，不能自动当作 DDL 字段。
- 缺少 Purchase Order Detail、Goods Receipt Detail、Supplier Master standalone page 是否写入 uncertainty。
- Web input_mode 是否明确区别 html_snapshot、page_map_only、live_crawl。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-extended-fused-ontology",
  "title": "Procurement Contract MVP Extended Fused Ontology",
  "domain": "procurement_contract",
  "description": "Extended ontology fused from MVP sources and optional UI/Web-derived outputs.",
  "input_mode": "mvp_plus_web_snapshot",
  "source_coverage": {
    "task_05_mvp_fusion": "provided | missing",
    "task_08_screenshot": "provided | missing | not_enabled",
    "task_12_web_snapshot": "provided | missing | not_enabled",
    "task_13_page_map_flow": "provided | missing | not_enabled"
  },
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
  "page_flows": [],
  "fusion_decisions": [],
  "conflicts": [],
  "uncertainties": [],
  "evidence_refs": [],
  "confidence": 0.0,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "extended_multi_source_fusion"
  }
}

【fusion_decisions 建议结构】
每个融合决策建议包含：
{
  "decision_id": "fusion:...",
  "topic": "",
  "merged_element_id": "",
  "source_terms": [],
  "source_evidence_types": [],
  "decision": "merged | kept_separate | candidate_only | conflict_recorded | uncertain",
  "rationale": "",
  "evidence_refs": [],
  "confidence": 0.0,
  "uncertainties": []
}

【证据要求】
1. 保留原有 Task 05 evidence，同时新增 Web 结论必须引用 `web:*` evidence，screenshot 结论必须引用 `screen:*` evidence。
2. 融合决策必须能追溯到具体 source task output 或原始材料路径。
3. 冲突必须引用至少两个来源或明确说明另一个来源缺失。
4. 不要引用 gold、demo baseline、machine_score、known conflicts 或未提供文件。

【不确定性要求】
1. Web-only / screenshot-only 结论必须标记为候选或较低 confidence。
2. 页面按钮、角色可见性和状态标签不能直接证明后端规则或权限规则。
3. page_map_only 只能支持页面图理解，不能声称 HTML DOM 或 live Web 观察。
4. 缺失可选任务输出时，记录 source_coverage 和 uncertainty，不要补写其内容。

【禁止事项】
1. 不要简单拼接 Task 05、08、12、13 输出。
2. 不要声称访问了 live Web、真实截图、OCR、点击、JS 执行或 API 调用，除非输入明确提供了对应证据。
3. 不要补充所有输入中都没有证据的对象、字段、页面、按钮、状态、关系、规则或动作。
4. 不要自行解决冲突后删除来源差异。
5. 不要读取或引用 gold answer、known conflicts、demo outputs、scoring 输出或人工复核材料。
```

## 输出文件名

`results/<evaluation_id>/normalized_outputs/task_14_extended_multi_source_fusion.json`

同时保存：

- 原始输出：`results/<evaluation_id>/raw_outputs/task_14_extended_multi_source_fusion_raw.md`
- task result wrapper：`results/<evaluation_id>/task_14_extended_multi_source_fusion_result.json`

## 输出格式

- 单个合法 JSON 对象。
- 字段名使用英文。
- 建议尽量兼容 `schemas/ontology.schema.json`，但允许包含扩展字段如 `input_mode`、`source_coverage`、`page_flows`、`fusion_decisions`。
- 必须声明哪些可选输入 provided / missing / not_enabled。

## Evidence 要求

- MVP baseline 结论保留 Task 05 原 evidence。
- Web-derived 结论引用 `web:*` evidence handle 或 `web_snapshots/` / `web_map/` source_ref。
- Screenshot-derived 结论引用 `screen:*` evidence handle 或 `screenshots/*.screen.md` source_ref。
- 融合决策和冲突必须说明涉及来源和 source-specific terms。
- 不得引用 evaluator-only gold、known conflicts、demo outputs 或 scoring 输出。

## 不确定性要求

- UI-only button/action、UI-only role visibility、UI-only calculated indicator、page_map_only flow 都必须保留 uncertainty 或低 confidence。
- 可选任务缺失时，不要假装已处理；在 `source_coverage` 和 `uncertainties` 中说明。
- 多源差异不得静默归并；需要写入 `aliases`、`mappings`、`conflicts`、`fusion_decisions` 或 `uncertainties`。

## 禁止幻觉要求

- 不得声称 live Web、真实图片、OCR、JS 执行、API 调用或后端事务已验证。
- 不得补充未提供页面、未出现按钮、未出现字段、未出现状态或未出现角色。
- 不得用外部采购系统常识补全付款、合同、审批、发票或页面流程。
- 不得把 UI 文案直接上升为最终业务规则；需要 code/document/DDL 等来源确认。

## 无法访问 Web 时的 HTML snapshot 降级

- 如果提供 Task 12 且 input_mode 为 `html_snapshot`：将其作为静态 Web evidence 融合，不能声称 live crawl。
- 如果仅提供 Task 13 且 input_mode 为 `page_map_only`：只能融合页面图和流程候选，不新增 DOM 字段证据。
- 如果只提供复制粘贴页面片段：标记为 `manual_page_notes`，记录复制范围。
- 如果 Web 输出缺失：保持 MVP baseline，记录 Web optional source missing，不要编造 Web 结论。

## 允许追问次数

最多 2 次。允许追问 Task 05 是否完整、可选 Task 08/12/13 是否启用、输入模式组合或关键输出是否截断。

## 常见失败

- 简单拼接多个 JSON，未去重、未融合。
- 把 Web / screenshot UI button 当成已实现后端动作。
- 忽略 `input_mode` 或 source_coverage。
- 丢失 `web:*` / `screen:*` evidence_refs。
- 忽略 conflict 和 uncertainty。
- 声称 live Web、真实截图或 OCR 能力。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-14",
  "status": "failed",
  "failure_type": "invalid_json | no_deduplication | missing_source_coverage | missing_conflicts | missing_evidence | claimed_live_web | claimed_real_image | hallucination | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_14_extended_multi_source_fusion_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts`、`fusion_decisions` 或 `uncertainties`。
- 复制 prompt 时只复制 fenced code block 内的内容；不要把操作员步骤、输出文件名说明、gold/reference 路径或 scoring 输出复制给被评估 AI。
