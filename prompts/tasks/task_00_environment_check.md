# Task 00: 环境能力检查

## 任务目标

登记当前客户环境、AI 工具、模型、权限边界和输入材料可访问性，形成后续采购合同 MVP 测试任务的环境基线。本任务不评价本体质量，只确认工具组合是否具备读取代码、DDL、CSV、业务文档和稳定输出 JSON 的能力。

## 输入材料

- 操作员填写的工具名称、工具版本、模型名称。
- 客户环境说明：联网状态、内网/隔离/混合环境、文件访问限制、命令执行限制。
- 采购合同 MVP 数据集目录说明：`source_code/`、`database/ddl.sql`、`database/sample_data/`、`documents/`。
- 可参考 schema：`schemas/tool_profile.schema.json`、`schemas/customer_profile.schema.json`。

## 操作员步骤

1. 确认 AI 工具能否读取文件；不能读取时，准备复制粘贴输入材料。
2. 确认 AI 工具能否执行命令；不能执行时，不要求其运行命令。
3. 确认联网、图片、浏览器、数据库连接、长上下文和 JSON 输出稳定性。
4. 将已知能力和未知能力都写入 prompt。
5. 保存输出；若 JSON 不合法，允许一次要求修复为合法 JSON。

## 给 AI 工具复制使用的完整 prompt

```text
你正在参与一个采购合同 MVP 本体抽取能力评估。请只基于我提供的信息登记环境和工具能力，不要根据工具品牌或模型名称推断未知能力。

【任务目标】
生成环境能力登记 JSON，用于判断后续任务是否可以处理源代码、数据库 DDL、CSV 样例数据和业务说明文档。

【已知信息】
- 工具名称：<操作员填写，未知写 unknown>
- 工具版本：<操作员填写，未知写 unknown>
- 模型名称：<操作员填写，未知写 unknown>
- 客户环境：<internet / intranet / isolated / hybrid / unknown>
- 是否联网：<true / false / unknown>
- 是否可读文件：<true / false / unknown>
- 是否可执行命令：<true / false / unknown>
- 是否支持图片：<true / false / unknown>
- 是否支持浏览器：<true / false / unknown>
- 是否支持数据库连接：<true / false / unknown>
- 长上下文能力：<none / limited / medium / long / very_long / unknown>
- 可访问输入目录：<source_code / database_ddl / sample_data_csv / documents 中可访问项>
- 不可访问输入目录：<不可访问项>
- 其他限制：<操作员填写>

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "task_id": "TASK-00",
  "tool_profile": {
    "tool_name": "",
    "tool_version": "",
    "model_name": "",
    "customer_environment": {
      "environment_type": "unknown",
      "restrictions": []
    },
    "capabilities": {
      "internet_access": null,
      "can_read_files": null,
      "can_execute_commands": null,
      "supports_images": null,
      "supports_browser": null,
      "supports_database_connection": null,
      "long_context_capability": {
        "level": "unknown",
        "max_context_tokens": null,
        "notes": ""
      }
    },
    "json_output_stability": {
      "level": "unknown",
      "failure_modes": [],
      "notes": ""
    },
    "recommended_use_cases": [],
    "not_recommended_use_cases": [],
    "known_limitations": []
  },
  "input_access": {
    "source_code": "available | unavailable | partial | unknown",
    "database_ddl": "available | unavailable | partial | unknown",
    "sample_data_csv": "available | unavailable | partial | unknown",
    "documents": "available | unavailable | partial | unknown"
  },
  "uncertainties": [],
  "evidence_refs": [],
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated"
  }
}

【证据要求】
操作员描述使用 `operator_statement:<说明>`；实际尝试观察使用 `observed:<说明>`。

【禁止事项】
不要输出评分，不要引用外部资料，不要假设未验证能力。
```

## 输出文件名

`results/<evaluation_id>/raw_outputs/task_00_environment_check_raw.md`

同时由操作员整理并保存：

- `results/<evaluation_id>/tool_profile.json`：尽量兼容 `schemas/tool_profile.schema.json`。
- `results/<evaluation_id>/customer_profile.json`：尽量兼容 `schemas/customer_profile.schema.json`。

说明：Task 00 是环境/工具 metadata，不是 ontology 评分任务；默认不要求 `score_auto.py` 发现它。

## 输出格式

- 单个合法 JSON 对象。
- 字段名使用英文。
- 未知能力使用 `unknown` 或 `null`，不要写成确定值。

## 证据链要求

- 每个能力判断都要有 `evidence_refs`。
- 操作员口述信息用 `operator_statement:*`。
- 实际观察信息用 `observed:*`。

## 不确定性表达要求

- 未知模型版本、未知上下文长度、未知联网状态等写入 `uncertainties`。
- 无法验证的能力不得写成确定能力。

## 禁止幻觉要求

- 不得根据工具品牌推断能力。
- 不得声称已读取未实际读取的目录。
- 不得生成不存在的客户环境信息。

## 允许追问次数

最多 2 次。只允许追问工具/模型名称、文件访问、命令执行、网络访问等环境信息。

## 常见失败情况

- 输出不是合法 JSON。
- 把未知能力写成确定能力。
- 混入评分结论。
- 缺少 `uncertainties` 或 `evidence_refs`。

## 失败记录方式

```json
{
  "task_id": "TASK-00",
  "status": "failed",
  "failure_type": "invalid_json | hallucinated_capability | missing_uncertainty | incomplete_output | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_00_environment_check_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

## A5 metadata 补充说明

- Task 00 原始输出可以使用本文件 prompt 中的环境登记结构。
- 操作员应把信息整理为 `tool_profile.json` 和 `customer_profile.json`。
- 对 schema 中必须为 boolean 的能力字段，如果现场无法验证，使用保守值 `false`，并在 `known_limitations`、`metadata.unverified_capabilities` 或 notes 中记录 unknown/unverified。
- Task 00 默认不参与 ontology coverage 自动评分。
- 不要把 gold/reference/demo 文件作为可访问输入目录。
