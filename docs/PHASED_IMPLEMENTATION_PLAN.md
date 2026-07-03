# 分阶段实施计划：MVP 收口、截图扩展、Web 扩展

本文档用于指导后续 Claude Code 执行。核心目标是把工作拆成小步、可 review、可验收、可回滚的工程任务，避免 MVP 收口、截图能力扩展、Web 能力扩展混在一起。

## 0. 总体原则

1. 先收口 MVP，再扩截图，最后扩 Web。
2. 每个任务尽量控制在 30-90 分钟 Claude Code 工作量内。
3. 检查和修复必须分离：先记录问题，再单独修复。
4. demo、dry run、consistency check、scoring 修改不得混做。
5. B/C 扩展不得破坏原有 MVP baseline。
6. 涉及 `score_auto.py` 的任务必须保持向后兼容：新增文件存在则读取，不存在则跳过。
7. 每个任务完成后只输出：新增/修改文件、用途、验证结果、未修复问题、建议 commit message。
8. 不自动 commit，除非另行明确要求。

建议执行节奏：

```text
Day 1: A1 -> A2 -> A3 -> A4
Review: 人工查看 A3/A4 的 Blocker/Major
Day 2: A5 -> A6
Day 3: B1 -> B2 -> B3 -> B4 -> B5 -> B6
Day 4: C1 -> C2 -> C3 -> C4 -> C5 -> C6 -> C7
```

如果想减少交互，可以合并：

```text
A1 + A2 可合并
A3 + A4 可合并，但必须只检查不修复
A5 单独执行
A6 单独执行
B2 + B3 可合并
C2 + C3 可合并
C4 + C5 可合并
```

---

## 1. 阶段 A：MVP 收口

阶段目标：确认当前 MVP 工具包可以被低经验操作员理解、执行、评分和复核，并形成明确的 Internal Pilot 判断。

阶段边界：

- 不扩展截图。
- 不扩展 Web。
- 不引入新数据集。
- 不做大规模重构。
- 只在 A5 修复 Blocker/Major。

### A1. 补齐 scoring 使用说明

目标：让低经验操作员只看 `scoring/README.md` 就知道如何准备输入和运行评分。

执行 prompt：

```text
现在只做一个小任务：补齐 scoring 使用说明。

请创建或完善：

scoring/README.md

内容包括：
1. score_auto.py 的用途
2. 输入目录结构要求
3. results/<evaluation_id>/ 应该包含哪些文件
4. 如何运行 score_auto.py
5. 命令示例
6. machine_score.json 字段解释
7. machine_score.md 字段解释
8. 常见错误和排查方法
9. 离线环境运行注意事项

要求：
- 使用中文。
- 面向低经验操作员。
- 不要修改 score_auto.py。
- 不要创建 demo result。
- 不要做 dry run。
- 完成后请输出：新增/修改文件、每个文件用途、是否运行验证、验证结果、发现但未修复的问题、建议 commit message。
```

验收标准：

```text
超聚变团队成员只看 scoring/README.md，就知道如何准备输入和运行评分。
```

建议 commit message：

```text
docs: add scoring usage guide
```

### A2. 创建 demo_baseline 示例结果

目标：展示一次完整评估跑完后 `results/` 目录应该长什么样。

执行 prompt：

```text
现在只做一个小任务：创建 demo_baseline 示例评估结果。

请创建：

results/demo_baseline/

其中包含一组模拟 AI 工具输出，用于演示当前 MVP 的完整评分流程。

要求：
1. 模拟输出必须基于 datasets/generic_procurement_contract_mvp/
2. 模拟输出不要完美，要包含少量合理缺失和少量可解释错误
3. 至少包含：
   - task_01_code_to_ontology_result.json
   - task_02_ddl_to_ontology_result.json
   - task_03_sample_data_profile_result.json
   - task_04_document_to_ontology_result.json
   - task_05_multi_source_fusion_result.json
   - tool_profile.json
   - human_effort_log.json
4. 如果可以运行 scoring/score_auto.py，请运行并生成：
   - machine_score.json
   - machine_score.md
5. 如果当前环境无法运行脚本，请生成符合预期结构的示例输出，并明确标注为 demo sample。
6. 如果发现数据集、gold answer、schema 或 scoring 之间存在疑似不一致，不要修复，只在输出摘要中列为“待 A3 检查确认的问题”。

要求：
- 不要修改数据集。
- 不要修改 gold answer。
- 不要修改 scoring 逻辑。
- 不要做一致性检查。
- 完成后请输出：新增/修改文件、每个文件用途、是否运行验证、验证结果、发现但未修复的问题、建议 commit message。
```

验收标准：

```text
别人能看到一次完整评估跑完后，results 目录应该长什么样。
```

建议 commit message：

```text
demo: add baseline evaluation result
```

### A3. MVP 一致性检查，不修复

目标：系统性找出当前 MVP 的 Blocker/Major/Minor/Suggestion。

执行 prompt：

```text
现在只做一个小任务：对当前 MVP 工具包做一致性检查。

请创建：

docs/MVP_CONSISTENCY_CHECK.md

检查范围包括：
1. 输入数据集中的源代码、DDL、CSV、文档是否互相一致
2. gold_ontology.json 中的 concept、attribute、relation、event、rule、action 是否都能在输入数据集中找到证据
3. gold_evidence_map.json 引用的文件、表、字段、类、方法、文档章节是否真实存在
4. acceptable_aliases.json 中的 canonical_id 是否都存在于 gold ontology
5. known_conflicts.json 中的 conflict 是否都能在输入数据集中找到来源
6. prompts 的输出要求是否和 schemas 一致
7. score_auto.py 期望的输入结构是否和 results/demo_baseline 一致
8. report template 是否能承接 machine_score 输出
9. 是否存在命名不一致、路径不一致、字段不一致的问题

请把发现的问题分为：
- Blocker：必须立即修复
- Major：内部试跑前应修复
- Minor：后续优化
- Suggestion：可选改进

注意：
- 本轮只检查，不修复。
- 不要修改任何被检查文件。
- 只创建或更新 docs/MVP_CONSISTENCY_CHECK.md。
- 完成后请输出：问题摘要、Blocker 数量、Major 数量、建议优先级、建议 commit message。
```

验收标准：

```text
可以清楚看到当前工具包到底有哪些 blocker / major，而不是一边检查一边改。
```

建议 commit message：

```text
docs: add MVP consistency check
```

### A4. MVP dry run，不修复

目标：模拟低经验操作员执行 MVP Smoke Test，记录卡点。

执行 prompt：

```text
现在只做一个小任务：模拟低经验操作员执行 MVP Smoke Test 的 dry run。

请创建：

docs/DRY_RUN_REVIEW.md

模拟流程包括：
1. 阅读 README
2. 选择 MVP 数据集
3. 执行 Smoke Test prompts
4. 保存任务输出
5. 运行自动评分
6. 查看 machine_score.md
7. 填写人工复核字段
8. 生成 final_eval_report.md

请重点记录：
1. 当前流程是否能跑通
2. 哪些步骤说明不清楚
3. 哪些路径容易出错
4. 哪些 prompt 不适合直接复制
5. 哪些输出文件命名需要统一
6. score_auto.py 的输入输出是否清楚
7. Gold answer 和 evidence map 是否够用
8. 超聚变低经验人员可能在哪些地方卡住
9. 需要修正的文档和文件
10. 建议的优先级修复清单

注意：
- 本轮只做 dry run 和记录问题。
- 不要修复问题。
- 不要修改 prompt、schema、scoring、dataset。
- 完成后请输出：问题摘要、建议修复优先级、是否存在 Blocker/Major、建议 commit message。
```

验收标准：

```text
可以判断超聚变团队拿着这套东西是否能跑通。
```

建议 commit message：

```text
docs: add MVP dry run review
```

### A5. 只修复 Blocker 和 Major

目标：只针对 A3/A4 发现的 Blocker/Major 做最小修复。

强制边界：

- 只修复 Blocker 和 Major。
- 不修复 Minor 和 Suggestion。
- 不扩展截图和 Web。
- 不引入新数据集。
- 不做大规模重构。
- 涉及数据模型重构或 gold answer 大改时，必须停止并询问。

执行 prompt：

```text
现在请根据以下两个文件中的问题清单，只修复 Blocker 和 Major 问题：

1. docs/MVP_CONSISTENCY_CHECK.md
2. docs/DRY_RUN_REVIEW.md

修复原则：
1. 只修复 Blocker 和 Major
2. 不修复 Minor 和 Suggestion
3. 优先修复路径、文件名、schema、prompt、score_auto.py 输入输出不一致问题
4. 不做大规模重构
5. 不引入新数据集
6. 不扩展截图和 Web
7. 每个修复都要说明原因
8. 修复后更新上述两个文档中的问题状态

执行方式：
- 修改前先列出拟修复清单。
- 如果修复范围只涉及路径、文件名、schema、prompt、score_auto.py 输入输出不一致问题，可以继续执行。
- 如果涉及数据模型重构、gold answer 大改、评分规则重写，必须停止并询问。

完成后请输出：
1. 修复了哪些问题
2. 修改了哪些文件
3. 仍未修复的问题
4. 是否还存在 Blocker
5. 是否还存在 Major
6. 运行了哪些验证
7. 验证结果
8. 建议 commit message
```

验收标准：

```text
Blocker = 0，Major 尽量 = 0；如果还有 Major，要有明确理由。
```

建议 commit message：

```text
fix: resolve MVP blocker and major issues
```

### A6. MVP closure summary

目标：形成 MVP 是否可以进入 Internal Pilot 的明确结论。

执行 prompt：

```text
现在请创建 MVP 收口总结文档：

docs/MVP_CLOSURE_SUMMARY.md

内容包括：
1. 当前 MVP 已完成的功能清单
2. 当前 MVP 可以评估哪些能力
3. 当前 MVP 暂不支持哪些能力
4. 当前 MVP 的标准使用流程
5. 当前 MVP 的输入输出闭环
6. 当前 MVP 的目录结构说明
7. 当前 MVP 的自动评分能力
8. 当前 MVP 的人工复核边界
9. 当前 MVP 的已知限制
10. 当前是否可以进入 Internal Pilot
11. 进入客户现场前还需要做什么
12. 下一阶段扩展截图能力的前置条件
13. 下一阶段扩展 Web 能力的前置条件

请在文档最后增加：

## Internal Pilot Readiness

Status: Go / Conditional Go / No-Go
Decision:
Reason:
Remaining Blockers:
Remaining Majors:
Required Before Customer Site:

要求：
- 不要再修改核心代码。
- 不要新增功能。
- 只做总结。
- 结论要明确：是否建议进入 Internal Pilot。
- 完成后请输出：新增文件、结论摘要、建议 commit message。
```

验收标准：

```text
可以拿这份文档向团队说明：MVP 到底完成了什么、怎么用、还不能做什么。
```

建议 commit message：

```text
docs: add MVP closure summary
```

---

## 2. 阶段 B：截图能力扩展

阶段目标：在不破坏 MVP baseline 的前提下，增加 screenshot surrogate 输入、截图分析 prompt、截图 evidence/conflict，以及最小 scoring 支持。

阶段边界：

- 不生成真实图片。
- 不做真实图片理解评分。
- 不扩展 Web。
- 不要求原 MVP 必须依赖 screenshot 文件。
- `results/demo_baseline/` 必须继续可评分。

### B1. 截图扩展设计

执行 prompt：

```text
现在开始下一阶段：截图能力扩展。

本轮只做设计，不创建截图数据，不写 prompt，不改 scoring。

请创建：

docs/SCREENSHOT_EXTENSION_PLAN.md

内容包括：
1. 截图能力扩展目标
2. 它要评估 AI 工具的哪些能力
3. 如何映射到现有 CAPABILITY_MODEL
4. 需要新增哪些输入数据
5. screenshot surrogate 与真实 PNG 的关系
6. 需要新增哪些 prompt
7. 需要扩展哪些 schema 字段
8. 需要扩展哪些 evidence 类型
9. 需要扩展哪些 known conflicts
10. 是否需要修改 score_auto.py
11. 如果工具不能看图片，如何降级
12. 对评分上限的影响
13. 实施步骤
14. 验收标准

要求：
- 不要实现。
- 只写设计文档。
- 完成后请输出：新增文件、设计结论、风险点、建议 commit message。
```

建议 commit message：

```text
docs: add screenshot extension plan
```

### B2. 创建 screenshot surrogate 数据

执行 prompt：

```text
现在只创建截图输入数据，不改 prompt，不改 scoring，不改 gold ontology。

请在现有数据集下创建：

datasets/generic_procurement_contract_mvp/screenshots/

创建至少 5 个 screenshot surrogate 文件：

1. purchase_request_list.screen.md
2. purchase_request_detail.screen.md
3. approval_task.screen.md
4. contract_detail.screen.md
5. invoice_payment.screen.md

每个文件必须包含：
- 页面名称
- 页面类型
- 用户角色
- 可见字段
- 表格列
- 按钮动作
- 状态展示
- 页面业务术语
- 可抽取的 concept / attribute / relation / action / state
- 与 DDL / 文档 / 代码的命名差异
- 可作为 evidence 的 source_location

要求：
- 这些文件是 screenshot surrogate，用 Markdown 表达截图内容。
- 不要生成真实图片。
- 不要修改 gold evidence。
- 不要修改 prompt。
- 完成后请输出：文件列表、每个页面覆盖的业务对象、建议 commit message。
```

建议 commit message：

```text
data: add screenshot surrogate inputs
```

### B3. 创建 screenshot prompt

执行 prompt：

```text
现在只创建截图分析任务 prompt。

请创建：

prompts/tasks/task_06_screenshot_to_ontology.md

要求包含：
1. 任务目标
2. 输入材料
3. 操作员步骤
4. 可复制给 AI 工具的完整 prompt
5. 输出文件名
6. 输出格式
7. 证据链要求
8. 不确定性要求
9. 禁止幻觉要求
10. 如果工具不能看图片或只能读取 screenshot surrogate，如何降级执行
11. 常见失败情况
12. 失败记录方式

要求：
- 不改数据集。
- 不改 scoring。
- 不改 gold files。
- 完成后请输出：新增文件、prompt 使用方式、建议 commit message。
```

建议 commit message：

```text
prompts: add screenshot ontology task
```

### B4. 扩展 screenshot evidence 和 conflicts

执行 prompt：

```text
现在只扩展截图相关 gold evidence 和 known conflicts。

请创建：

datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.screenshot.json
datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.screenshot.md
datasets/generic_procurement_contract_mvp/gold/known_conflicts.screenshot.json
datasets/generic_procurement_contract_mvp/gold/known_conflicts.screenshot.md

要求：
1. 不覆盖原始 gold_evidence_map.json 和 known_conflicts.json
2. 只新增 screenshot evidence
3. 每条 evidence 都必须引用真实存在的 screenshots/*.screen.md
4. 新增冲突类型包括：
   - ui_vs_database_naming_mismatch
   - screenshot_only_business_term
   - role_permission_ui_vs_doc_mismatch
5. 冲突要轻量、真实、可解释
6. 不修改 score_auto.py
7. 完成后请输出：新增文件、evidence 数量、conflict 数量、引用校验结果、建议 commit message。
```

建议 commit message：

```text
data: add screenshot evidence and conflicts
```

### B5. 最小扩展 scoring 支持 screenshot evidence

执行 prompt：

```text
现在只做 score_auto.py 的最小扩展，支持 screenshot evidence。

要求：
1. 支持读取 gold_evidence_map.screenshot.json
2. 支持解析 source_type = screenshot
3. 支持检查 screenshot evidence ref 是否存在
4. machine_score.md 中增加 screenshot evidence 覆盖摘要
5. 不做图片理解评分
6. 不做复杂语义判断
7. 保持原有 MVP 评分兼容
8. gold_evidence_map.screenshot.json 存在则读取，不存在则跳过
9. 不得让 results/demo_baseline/ 依赖 screenshot 文件
10. 修改后必须验证 results/demo_baseline/ 仍可评分
11. 完成后更新 scoring/README.md

完成后请输出：修改文件、兼容性说明、验证命令、验证结果、建议 commit message。
```

验收标准：

```text
原 MVP baseline 可继续评分；存在 screenshot evidence 时可生成覆盖摘要。
```

建议 commit message：

```text
scoring: support optional screenshot evidence
```

### B6. 创建 screenshot demo

执行 prompt：

```text
现在创建截图能力扩展 demo。

请创建：

results/demo_screenshot/

内容包括：
1. 模拟 AI 对 task_06_screenshot_to_ontology.md 的输出
2. tool_profile.json
3. human_effort_log.json
4. machine_score.json
5. machine_score.md
6. final_eval_report.md

要求：
- 基于 screenshot surrogate 数据
- 模拟输出不要完美
- 展示截图能力如何被评分
- 不扩展 Web
- 不破坏 results/demo_baseline/
- 如可运行 scoring/score_auto.py，请运行并生成评分文件
- 完成后请输出：文件列表、demo 用途、验证结果、建议 commit message。
```

建议 commit message：

```text
demo: add screenshot evaluation result
```

---

## 3. 阶段 C：Web 能力扩展

阶段目标：在 MVP 和 screenshot baseline 均稳定后，增加 HTML snapshot、page map、Web prompts、Web evidence/conflict，以及最小 scoring 支持。

阶段边界：

- 不做真实递归爬虫。
- 不做图算法评分。
- 不要求原 MVP 或 screenshot demo 必须依赖 Web 文件。
- `results/demo_baseline/` 和 `results/demo_screenshot/` 必须继续可评分。

### C1. Web 扩展设计

执行 prompt：

```text
现在开始 Web 页面快照与页面地图能力扩展。

本轮只做设计，不创建 HTML，不写 prompt，不改 scoring。

请创建：

docs/WEB_EXTENSION_PLAN.md

内容包括：
1. Web 能力扩展目标
2. 它要评估 AI 工具的哪些能力
3. Web snapshot 与真实递归爬虫的关系
4. 新增输入数据结构
5. HTML snapshot 设计原则
6. page map 设计原则
7. 新增 prompts
8. 新增 evidence 类型
9. 新增 known conflicts
10. scoring 最小扩展范围
11. 如果工具不能访问 Web，如何降级到 HTML snapshot
12. 验收标准

要求：
- 不要实现。
- 只写设计文档。
- 完成后请输出：新增文件、设计结论、风险点、建议 commit message。
```

建议 commit message：

```text
docs: add web extension plan
```

### C2. 创建 HTML snapshots

执行 prompt：

```text
现在只创建 Web HTML snapshot 数据。

请在现有数据集下创建：

datasets/generic_procurement_contract_mvp/web_snapshots/

至少包含：

1. index.html
2. purchase_requests.html
3. purchase_request_detail_PR-2024-001.html
4. approval_tasks.html
5. contracts.html
6. contract_detail_CT-2024-001.html
7. invoices.html
8. payments.html

要求：
- HTML 要真实可信
- 包含菜单、页面标题、字段、状态、按钮、表格、链接、面包屑
- 链接关系要能形成页面地图
- 术语与 DDL / 文档 / 代码存在轻微不一致
- 不需要后端
- 不改 gold files
- 不改 scoring
- 完成后请输出：文件列表、页面关系摘要、建议 commit message。
```

建议 commit message：

```text
data: add web HTML snapshots
```

### C3. 创建 page map

执行 prompt：

```text
现在只创建 Web page map。

请创建：

datasets/generic_procurement_contract_mvp/web_map/page_map.json
datasets/generic_procurement_contract_mvp/web_map/page_map.md

内容包括：
- page_id
- url_or_file
- title
- page_type
- menu_path
- visible_concepts
- visible_actions
- outgoing_links
- required_role
- evidence_refs
- crawl_notes

page_map.md 需要解释：
- 推荐爬取顺序
- 核心业务流程页面
- 重复页面
- 权限/角色线索
- 用于测试递归分析能力的点

要求：
- evidence_refs 必须引用真实存在的 web_snapshots 文件或 page_map 文件。
- 不改 gold files。
- 不改 scoring。
- 完成后请输出：新增文件、引用校验结果、建议 commit message。
```

建议 commit message：

```text
data: add web page map
```

### C4. 创建 Web prompts

执行 prompt：

```text
现在只创建 Web 相关 prompts。

请创建：

prompts/tasks/task_07_web_snapshot_to_ontology.md
prompts/tasks/task_08_page_map_to_business_flow.md
prompts/tasks/task_09_extended_multi_source_fusion.md

每个 prompt 必须包含：
- 任务目标
- 输入材料
- 操作员步骤
- 可复制 prompt
- 输出文件名
- 输出格式
- evidence 要求
- 不确定性要求
- 禁止幻觉要求
- 无法访问 Web 时如何使用 HTML snapshot 降级
- 常见失败
- 失败记录方式

要求：
- 不改数据集。
- 不改 scoring。
- 不改 gold files。
- 完成后请输出：新增文件、每个 prompt 的用途、建议 commit message。
```

建议 commit message：

```text
prompts: add web evaluation tasks
```

### C5. 扩展 Web evidence / conflicts

执行 prompt：

```text
现在只扩展 Web 相关 gold evidence 和 known conflicts。

请创建：

datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.json
datasets/generic_procurement_contract_mvp/gold/gold_evidence_map.web.md
datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.json
datasets/generic_procurement_contract_mvp/gold/known_conflicts.web.md

要求：
1. 不覆盖原始 gold 文件
2. 只新增 web_page evidence
3. 每条 evidence 都引用真实存在的 web_snapshots 或 web_map 文件
4. 新增冲突类型包括：
   - web_vs_document_flow_mismatch
   - page_action_without_backend_evidence
   - ui_vs_database_naming_mismatch
   - role_permission_web_vs_doc_mismatch
5. 不改 scoring
6. 完成后请输出：新增文件、evidence 数量、conflict 数量、引用校验结果、建议 commit message。
```

建议 commit message：

```text
data: add web evidence and conflicts
```

### C6. 最小扩展 scoring 支持 Web evidence

执行 prompt：

```text
现在只做 score_auto.py 的最小扩展，支持 Web evidence。

要求：
1. 支持读取 gold_evidence_map.web.json
2. 支持 source_type = web_page
3. 支持 page_map evidence ref
4. machine_score.md 中增加 Web evidence 覆盖摘要
5. 不做真实爬虫评分
6. 不做图算法评分
7. 保持 MVP 和 screenshot 评分兼容
8. gold_evidence_map.web.json 存在则读取，不存在则跳过
9. 不得让 results/demo_baseline/ 或 results/demo_screenshot/ 依赖 Web 文件
10. 修改后必须验证 demo_baseline 和 demo_screenshot 仍可评分
11. 完成后更新 scoring/README.md

完成后请输出：修改文件、兼容性说明、验证命令、验证结果、建议 commit message。
```

验收标准：

```text
原 MVP baseline 和 screenshot demo 可继续评分；存在 Web evidence 时可生成覆盖摘要。
```

建议 commit message：

```text
scoring: support optional web evidence
```

### C7. 创建 Web demo

执行 prompt：

```text
现在创建 Web 能力扩展 demo。

请创建：

results/demo_web/

内容包括：
1. 模拟 AI 对 Web prompts 的输出
2. tool_profile.json
3. human_effort_log.json
4. machine_score.json
5. machine_score.md
6. final_eval_report.md

要求：
- 基于 HTML snapshots 和 page_map
- 模拟输出不要完美
- 展示 Web snapshot / page map 能力如何被评分
- 不破坏 results/demo_baseline/ 和 results/demo_screenshot/
- 如可运行 scoring/score_auto.py，请运行并生成评分文件
- 完成后请输出：文件列表、demo 用途、验证结果、建议 commit message。
```

建议 commit message：

```text
demo: add web evaluation result
```

---

## 4. 每步完成后的标准输出格式

每次让 Claude Code 执行一个任务时，要求它用以下格式收尾：

```text
完成情况：
- 新增/修改文件：
- 每个文件用途：
- 是否运行验证：
- 验证命令：
- 验证结果：
- 发现但未修复的问题：
- 是否存在 Blocker：
- 是否存在 Major：
- 建议 commit message：
```

---

## 5. 关键风险控制点

### 5.1 A5 修复范围扩散

风险：Claude Code 可能把 Minor/Suggestion 一起修掉，或者重构评分器。

控制方式：

```text
A5 必须只修 Blocker/Major；涉及数据模型重构、gold answer 大改、评分规则重写时，必须停止并询问。
```

### 5.2 B5/C6 破坏 MVP baseline

风险：新增 screenshot/web 逻辑后，原 MVP 结果无法评分。

控制方式：

```text
新增 evidence 文件必须可选读取：存在则读取，不存在则跳过。
results/demo_baseline/ 必须继续可评分。
```

### 5.3 demo 与真实评分混淆

风险：demo 输出被误认为真实评测结果。

控制方式：

```text
所有 demo result 都必须在说明中标注为 simulated/demo sample，不代表真实工具能力。
```

### 5.4 检查阶段偷偷修复

风险：A3/A4 过程中 Claude Code 发现问题后直接修改。

控制方式：

```text
A3/A4 明确只创建或更新检查文档，不修改 prompt、schema、scoring、dataset、gold files。
```

---

## 6. 推荐里程碑

### Milestone 1: MVP Closure

完成任务：

```text
A1, A2, A3, A4, A5, A6
```

完成标准：

```text
Blocker = 0
Major = 0 或有明确例外说明
results/demo_baseline/ 可评分
MVP_CLOSURE_SUMMARY 给出 Go / Conditional Go / No-Go
```

### Milestone 2: Screenshot Extension

完成任务：

```text
B1, B2, B3, B4, B5, B6
```

完成标准：

```text
screenshot surrogate 数据存在
截图 prompt 存在
screenshot evidence/conflict 存在且引用有效
score_auto.py 兼容 MVP baseline
results/demo_screenshot/ 可评分
```

### Milestone 3: Web Extension

完成任务：

```text
C1, C2, C3, C4, C5, C6, C7
```

完成标准：

```text
HTML snapshots 存在
page_map 存在且引用有效
Web prompts 存在
Web evidence/conflict 存在且引用有效
score_auto.py 兼容 MVP 和 screenshot baseline
results/demo_web/ 可评分
```

---

## 7. 建议先执行的第一条命令式任务

建议下一步只执行 A1：

```text
现在只做一个小任务：补齐 scoring 使用说明。

请创建或完善 scoring/README.md，内容包括 score_auto.py 的用途、输入目录结构、results/<evaluation_id>/ 必备文件、运行方式、命令示例、machine_score.json 字段解释、machine_score.md 字段解释、常见错误、离线环境注意事项。

要求使用中文，面向低经验操作员；不要修改 score_auto.py；不要创建 demo result；不要做 dry run。完成后输出新增/修改文件、每个文件用途、是否运行验证、验证结果、发现但未修复的问题、建议 commit message。
```
