# CodeBuddy vs Claude Code 对比报告

- 生成日期：2026-07-05
- 资料口径：截至 2026-07 的公开资料 + 本工具包 `20260704-local-codebuddy-smoke` / `20260704-local-claude-code-smoke` 脱敏 Smoke Test 结果
- 适用范围：FDE 团队在客户现场评估 AI 编程工具组合时的选型参考
- 重要声明：本报告比较的是“工具产品形态 + 官方能力边界 + 本地受限 Smoke Test 表现”，不是单一模型的绝对能力排名。

## 1. 结论摘要

CodeBuddy 与 Claude Code 都可以作为 AI 编程助手使用，但产品重心不同。

- CodeBuddy 更偏“中文企业/腾讯云生态内的全流程智能编程工具”，强调 IDE、插件、CLI 三种形态，以及从 PRD、设计稿、编码、测试、审查到部署的端到端链路。
- Claude Code 更偏“CLI 原生的 Agentic Coding Tool”，以终端 Agent 工作流为核心，并扩展到 IDE、桌面端、浏览器、Git/PR、CI、Routines、Background Agents、MCP 等工程自动化入口。
- 如果客户团队以中文协作、腾讯云生态、IDE 插件体验、企业知识库、设计转代码和产品到研发一体化为优先，应优先评估 CodeBuddy。
- 如果客户团队更看重复杂代码库改造、命令行自动化、跨工具 Agent 工作流、MCP 连接外部系统、CI/PR 协作和可组合工程流程，应优先评估 Claude Code。
- 大型团队不必把两者视为互斥替代：CodeBuddy 可覆盖中文 IDE/产品研发链路，Claude Code 可覆盖高级工程自动化、长任务改造和跨系统 Agent 流程。

## 2. 一页对比表

| 维度 | CodeBuddy | Claude Code | 评估含义 |
| --- | --- | --- | --- |
| 官方定位 | 基于 AI 的全流程智能编程工具，强调“对话即编程”和端到端交付 | Agentic coding tool / agentic assistant，可读取代码库、编辑文件、运行命令并集成开发工具 | CodeBuddy 更像一体化研发助手；Claude Code 更像可执行工程任务的 Agent Harness |
| 产品形态 | IDE、插件、CLI | Terminal CLI、IDE、Desktop、Browser、GitHub/GitLab CI、Routines、Background Agents | Claude Code 的自动化入口更丰富；CodeBuddy 的中文 IDE/插件入口更直接 |
| 核心能力 | PRD 生成、设计稿转代码、代码补全、多文件生成、行间对话、代码解释、代码审查、单元测试生成 | 代码库理解、多文件修改、命令执行、测试验证、Bug Fix、Feature Work、Lint/依赖/冲突处理 | CodeBuddy 覆盖产品到代码；Claude Code 覆盖代码到验证与流程自动化 |
| 模型与上下文 | 官方文档提到支持混元、DeepSeek 等多模型，以及 `@workspace`、`#Codebase`、自定义指令、企业知识库、企业模型接入/切换 | 官方资料更强调项目上下文、代码库理解、工具调用和上下文管理；本轮未把具体模型切换作为已核验结论 | CodeBuddy 多模型与企业知识库表述更明确；Claude Code 的强项在 Agent 运行框架 |
| Agent / 工具调用 | CLI 支持 Shell、文件、网络操作；支持 ACP/IDE 集成；腾讯云资料提到 MCP Server | 官方描述 gather context -> take action -> verify results 的 agentic loop，内置文件、搜索、执行、Web、代码智能工具，可通过 Skills、MCP、Hooks、Subagents 扩展 | Claude Code 的 Agent/MCP 生态证据更充分 |
| 测试验证 | 明确宣传单元测试生成、测试代码生成、错误检查、智能代码审查 | 强调运行测试/命令验证结果，并在 CI 中做 PR review、issue triage、代码审查 | CodeBuddy 更像生成测试/审查建议；Claude Code 更像把验证纳入任务闭环 |
| 团队与企业能力 | 企业知识库、自定义指令、企业模型接入/切换、腾讯云产品化入口 | Git/PR、CI review/triage、scheduled tasks、Routines、subagents/background agents、MCP 外部系统连接 | CodeBuddy 偏企业知识沉淀；Claude Code 偏工程协作自动化 |
| 成本与可用性 | 本轮未核验价格、套餐、SLA、地区、私有化/专有云条款 | 本轮未核验价格、套餐、SLA、地区、企业采购条款 | 必须按客户采购与现场网络条件单独确认 |
| 本地 Smoke Test 表现 | 核心概念 91.67%，关键属性 48.65%，关键关系 34.88% | 核心概念 91.67%，关键属性 97.30%，关键关系 46.51% | 在本次受限任务中 Claude Code 属性/关系覆盖更高，但人工复核仍未完成 |

## 3. 产品定位与边界

### CodeBuddy

公开资料显示，CodeBuddy 的官方定位是“基于 AI 的全流程智能编程工具”，覆盖需求规划、产品设计、代码研发、测试、审查、部署等链路。它的叙事重点不是只做代码补全，而是把产品构思、PRD、设计稿、编码和交付串起来。

对本工具包的意义：

- 在客户现场，如果要评估“低经验操作员 + 中文业务材料 + 企业知识库 + 研发落地”的组合，CodeBuddy 的产品定位与本工具包的 FDE 现场评估目标较匹配。
- 但公开资料更多证明“厂商宣称具备这些入口和能力”，不能直接证明复杂本体任务上的准确率、稳定性和可复盘性。

### Claude Code

Claude Code 官方定位为 agentic coding tool / agentic assistant。公开资料强调它运行在开发者环境中，可以读取代码库、编辑文件、运行命令、理解项目上下文，并接入 IDE、Git、CI、MCP 等工程工具。

对本工具包的意义：

- Claude Code 更适合把 AI 工具评估扩展到真实工程闭环：读项目、改文件、跑命令、验证、提交、PR、CI、Issue 分流、跨系统检索。
- 在客户内网或高权限环境使用时，需要重点评估权限边界、命令执行策略、MCP 凭据管理、审计和人工确认流程。

## 4. IDE / CLI / 工作流能力

### CodeBuddy

已核验的公开资料显示 CodeBuddy 覆盖 IDE、插件、CLI 三种产品形态。

典型能力包括：

- 自然语言生成结构化 PRD。
- 设计稿一键转代码。
- 实时代码续写和代码补全。
- 多文件生成与行间对话。
- 代码解释、智能代码审查、错误检查。
- 工程结构分析，支持 `@workspace`、`#Codebase` 等上下文方式。
- 单元测试或测试代码生成。
- CLI 侧支持自然语言驱动开发流程，并支持 ACP agent server、`--ide` 或 `/ide` 等 IDE 集成方式。

适合的现场验证任务：

- 中文业务文档到本体草案。
- PRD/设计/代码多源材料抽取。
- 低经验操作员通过 IDE 插件完成单源抽取。
- 企业知识库或自定义指令对术语一致性的影响。

### Claude Code

已核验的公开资料显示 Claude Code 的 Terminal CLI 是完整交互界面，同时也支持 IDE、桌面端、浏览器、GitHub Actions/GitLab CI、Routines、Background Agents 等入口。

典型能力包括：

- 理解整个代码库，并跨多文件和多工具工作。
- 构建功能、修复 Bug、编写测试、修复 lint 错误。
- 解决 merge conflict、更新依赖、执行命令。
- 在 CI 中做自动化 code review 和 issue triage。
- 通过 Routines、scheduled tasks、background agents、subagents 支持更复杂的协作与自动化。

适合的现场验证任务：

- 多源融合后的 schema repair。
- 在工具包内执行评分脚本并解释失败项。
- 根据人工复核意见迭代修复 normalized artifact。
- 连接内网知识库、工单、数据库只读查询或文档系统进行跨源证据检索。

## 5. Agent、工具调用与 MCP

Claude Code 的公开资料对 Agent 运行机制描述更完整：其核心循环可概括为 gather context、take action、verify results。内置工具类别包括文件操作、搜索、执行、Web、代码智能，并可通过 Skills、MCP、Hooks、Subagents 扩展。

MCP 对本体项目评估尤其关键，因为真实客户现场经常需要连接：

- 内网 Git / 代码仓库。
- 数据库只读查询。
- Confluence / Wiki / 文档库。
- Jira / TAPD / 禅道等需求或缺陷系统。
- Slack / 飞书 / 企业微信等沟通记录。
- 内部 API、权限系统、数据目录或元数据平台。

CodeBuddy CLI 公开资料也提到 Shell、文件、网络操作、ACP/IDE 集成，以及腾讯云资料中的 MCP Server。但本轮资料中，CodeBuddy 对 MCP 使用场景、连接器生态、权限治理和跨系统工作流的描述不如 Claude Code 充分。

评估建议：

- 如果客户评估重点是“AI 是否能在 IDE 内读懂项目并辅助产出”，CodeBuddy 足够进入候选。
- 如果客户评估重点是“AI 是否能作为可审计 Agent 串起多系统工作流”，Claude Code 应作为重点候选。
- 无论选择哪一方，MCP/外部工具接入都必须单独做安全评审，不能把“支持连接”理解为“默认安全可用”。

## 6. 模型、上下文与企业知识

### CodeBuddy

公开资料明确提到 CodeBuddy 支持混元、DeepSeek 等多种对话大模型，并支持：

- `@workspace` / `#Codebase` 工程级上下文。
- 自定义指令。
- 企业专属知识库。
- 企业模型接入与切换。

这对客户现场评估很重要，因为很多企业不会只考察通用模型能力，而是会关注：

- 能否接入客户批准的模型。
- 能否使用内网知识库。
- 能否沉淀领域术语、规则、流程和历史交付经验。
- 能否在中文业务材料上保持术语一致。

### Claude Code

Claude Code 公开资料更强调 Agentic Harness、代码库理解、项目上下文、工具调用和上下文管理。本轮研究确认了其代码库理解与多工具工作流能力，但没有把“具体模型切换能力”作为已核验结论。

评估建议：

- 对 Claude Code，不应只问“上下文窗口多大”，而应验证它在任务中如何检索、裁剪、使用和更新上下文。
- 对 CodeBuddy，不应只看“支持哪些模型”，而应验证不同模型/知识库组合对本体抽取准确率和证据引用质量的实际影响。

## 7. 测试、验证与质量闭环

本体项目 AI 工具评估不应只看模型输出是否“像样”，而要看是否形成可复盘的质量闭环。

CodeBuddy 的公开资料明确宣传：

- 单元测试生成。
- 测试代码生成。
- 错误检查。
- 智能代码审查。

Claude Code 的公开资料更强调：

- 在 Agent 循环中运行测试或命令验证结果。
- 在 CI 中自动化 PR review、issue triage 和代码审查。
- 与 Git/PR/CI 形成工程闭环。

对工具包的建议：

- Smoke Test 阶段：限制工具只能读文件，观察其抽取和融合能力。
- Standard Test 阶段：允许只读命令、评分脚本和 schema validation，观察其能否定位失败原因。
- Extended Test 阶段：允许受控编辑、修复和重新评分，观察其能否形成“修改 -> 验证 -> 解释”的闭环。
- 企业准入阶段：增加权限审计、命令审批、MCP 凭据隔离和人工 sign-off。

## 8. 本工具包本地 Smoke Test 对比

本地已有两次脱敏 Smoke Test：

- `results/20260704-local-codebuddy-smoke/`
- `results/20260704-local-claude-code-smoke/`

两次运行都采用受限模式：

- 工具可读文件。
- 故意禁用 shell 执行和编辑。
- 不启用图片、浏览器、数据库连接、互联网访问。
- 操作员提供任务提示词与数据集路径。
- 未向被评估工具提供 gold/reference/demo/scoring 输出。

### 自动评分结果

| 指标 | CodeBuddy CLI 2.115.0 | Claude Code CLI 2.1.193 | 备注 |
| --- | ---: | ---: | --- |
| Core concepts | 91.67% | 91.67% | 两者都缺少 `concept:material` |
| Key attributes | 48.65% | 97.30% | Claude Code 明显更高 |
| Key relations | 34.88% | 46.51% | Claude Code 更高，但两者关系覆盖均有提升空间 |
| Schema-valid ontology files | 1 / 1 | 1 / 1 | 两者 schema 均通过 |
| Task result files checked | 5 | 5 | 两者任务 wrapper 均通过 schema 校验 |
| Evidence references checked | 270 | 954 | Claude Code 输出证据引用数量更多 |
| Missing evidence references | 92 | 177 | Claude Code 绝对缺失更多，需看比例与引用规范 |
| Possible hallucinations | 1 relation | 1 relation | 两者均出现 1 个疑似关系幻觉 |
| Human review | pending | pending | 最终结论必须等待人工复核 |

### 对本地结果的解释

- 在本次受限 Smoke Test 下，Claude Code 在关键属性覆盖和关键关系覆盖上优于 CodeBuddy。
- 两者核心概念覆盖相同，都没有覆盖 `material` 概念，说明该数据集对物料/行项目抽象仍是共同难点。
- Claude Code 的证据引用数量明显更多，但缺失引用也更多，人工复核需要关注“引用密度提升是否真的提升可追溯性”。
- 两者均通过 schema validation，说明在固定提示词和受限文件读取下都能产出结构化结果。
- 由于两次运行都禁用了 shell、编辑、浏览器、数据库和互联网，本结果不能反映它们在完整 Agent 模式下的真实上限。

## 9. 优势、短板与风险

### CodeBuddy 优势

- 中文与腾讯云生态资料更完整，适合国内客户现场沟通和采购路径。
- IDE、插件、CLI 三形态覆盖较广，容易从开发者日常工作流切入。
- PRD 生成、设计稿转代码、行间对话、多文件生成等能力更贴近产品到研发链路。
- 多模型、企业知识库、自定义指令、企业模型接入/切换的公开表述更明确。

### CodeBuddy 短板和风险

- 公开资料多为厂商能力声明，缺少足够第三方实测数据支持复杂本体任务表现。
- MCP、外部工具生态、跨系统 Agent 自动化的公开证据不如 Claude Code 充分。
- 本地 Smoke Test 中关键属性和关系覆盖低于 Claude Code，需进一步验证是否与提示词、权限模式、模型配置或操作方式有关。
- codebuddy.cn、codebuddy.ai、腾讯云文档之间可能存在版本与表述差异，正式评估应固定文档版本和产品版本。

### Claude Code 优势

- Agentic CLI 工作流成熟，适合复杂代码库、多文件修改、命令执行、测试验证和工程自动化。
- MCP、Skills、Hooks、Subagents、Background Agents 等扩展机制公开资料更充分。
- Git/PR/CI/Routines/scheduled tasks 等协作与自动化入口丰富。
- 本地 Smoke Test 中关键属性和关系覆盖更好，尤其适合需要高结构化抽取能力的任务。

### Claude Code 短板和风险

- 权限、命令执行、MCP 凭据、外部系统连接需要更严格治理，否则容易扩大操作风险。
- 中文本地生态、腾讯云集成、国内采购与合规路径不是其公开定位重点，需要客户现场单独确认。
- “理解整个代码库”应理解为产品能力目标和上下文管理能力，不应解释为无限上下文或无需裁剪。
- 成本、限额、地区可用性、企业条款需要按官方价格页和采购合同确认。

## 10. 选型建议

### 优先选择 CodeBuddy 的场景

- 客户团队主要使用中文业务材料和中文研发协作。
- 客户已在腾讯云生态内，采购、账号、权限、知识库和模型治理希望走腾讯云路径。
- 评估重点是 IDE 插件、代码补全、PRD/设计稿到代码、企业知识库和低经验操作员辅助。
- 客户更关注“产品经理/业务分析师/开发者协同完成交付”的一体化体验。

### 优先选择 Claude Code 的场景

- 客户允许 CLI Agent 在受控权限下读取项目、运行命令、执行测试或修改文件。
- 评估重点是复杂代码库理解、多文件改造、schema repair、自动验证和工程闭环。
- 客户需要连接 Git、CI、工单、文档、数据库、API 等多个系统。
- 团队有能力设计权限边界、命令 allowlist、MCP 凭据隔离、审计和人工审批流程。

### 两者并用的场景

- CodeBuddy 用于中文需求、PRD、设计稿、IDE 内辅助、企业知识库问答。
- Claude Code 用于工具包执行、批量修复、CI/PR 自动化、跨系统证据收集和长任务 Agent 工作流。
- FDE 团队用同一套 `ontology-ai-capability-eval-toolkit` 跑 Smoke/Standard/Extended Test，避免凭主观体验选型。

## 11. 后续验证清单

在进入客户现场或采购建议前，建议补充以下验证：

1. 价格与限额：确认 seat/token/usage 计费、免费额度、并发限制、企业报价、SLA。
2. 地区与合规：确认中国大陆/海外可用性、数据驻留、日志保留、训练使用、审计能力。
3. 权限与安全：确认 shell/edit/network/MCP 的默认权限、审批机制、allowlist、denylist、凭据隔离。
4. 企业知识：用同一份术语表和业务规则验证企业知识库/自定义指令对输出一致性的影响。
5. Agent 闭环：在 Standard/Extended Test 中允许受控执行评分脚本，验证工具能否基于错误报告修复输出。
6. 人工复核：完成 `20260704-local-codebuddy-smoke` 和 `20260704-local-claude-code-smoke` 的 manual review 后再给出最终排名。

## 12. 资料来源

### CodeBuddy / 腾讯云

- https://www.codebuddy.cn/docs/ide/Introduction
- https://www.codebuddy.ai/docs/zh/ide/Introduction
- https://www.codebuddy.ai/docs/zh/cli/README
- https://www.codebuddy.ai/docs/zh/cli/ide-integrations
- https://cloud.tencent.com/document/product/1749/104236
- https://cloud.tencent.com/document/product/1749/111508
- https://www.codebuddy.cn/docs/ide/Features/Subagents
- https://staging-codebuddy.tencent.com/docs/cli/sub-agents
- https://marketplace.visualstudio.com/items?itemName=Tencent-Cloud.coding-copilot

### Claude Code / Anthropic

- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/how-claude-code-works
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/sub-agents
- https://docs.anthropic.com/en/docs/claude-code/cli-usage
- https://docs.anthropic.com/en/docs/mcp
- https://docs.anthropic.com/en/docs/claude-code/security
- https://www.anthropic.com/product/enterprise
- https://support.anthropic.com/en/articles/9797531-what-is-the-claude-enterprise-plan

### 第三方/社区资料

- https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/
- https://github.com/anthropics/claude-code/issues/49244

## 13. 证据边界

- 主要证据来自厂商官方文档和产品页，适合支持“官方定位/宣称具备某能力”，不能直接证明实际效果、稳定性或性能优势。
- 本地 Smoke Test 是受限模式，不能代表完整权限、完整 Agent、联网、数据库、浏览器或企业知识库接入后的表现。
- 成本、套餐、限额、地区可用性、企业 SLA、私有化/专有云、数据驻留和合规条款没有在本轮形成可验证结论。
- 最终工具准入建议必须结合客户环境、权限边界、操作员能力、底层模型、网络条件和人工复核结果。