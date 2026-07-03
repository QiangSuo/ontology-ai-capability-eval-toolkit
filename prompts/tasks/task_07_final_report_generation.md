# Task 07: 最终报告生成

## 任务目标

基于环境检查、单源抽取、多源融合、schema repair 记录、自动评分结果和人工复核结果，生成采购合同 MVP 评估的最终结构化报告。报告关注工具组合能力总结、任务完成情况、风险、冲突处理、不确定性表达和后续建议；不生成评分脚本。

## 输入材料

- `results/<evaluation_id>/customer_profile.json`
- `results/<evaluation_id>/tool_profile.json`
- `results/<evaluation_id>/task_01_code_to_ontology_result.json`
- `results/<evaluation_id>/task_02_ddl_to_ontology_result.json`
- `results/<evaluation_id>/task_03_sample_data_profile_result.json`
- `results/<evaluation_id>/task_04_document_to_ontology_result.json`
- `results/<evaluation_id>/task_05_multi_source_fusion_result.json`
- `results/<evaluation_id>/task_06_schema_repair_result.json`，如有
- `results/<evaluation_id>/scoring/machine_score.json`
- `results/<evaluation_id>/manual_review/manual_review.md`
- `results/<evaluation_id>/execution_log.md`
- 原始失败记录，如有
- 可参考 schema：`schemas/evaluation_report.schema.json`、`schemas/task_result.schema.json`

## 操作员步骤

1. 确认 `machine_score.json` 已生成。
2. 确认人工复核已完成；如未完成，报告结论只能是 `insufficient_data` 或 `ready_with_constraints`。
3. 将 task results、machine score、manual review 和 execution log 提供给 AI 工具。
4. 要求 AI 生成结构化最终报告 JSON，不写评分脚本。
5. 报告必须区分事实、机器检查信号、人工判断、风险和建议。
6. 失败、阻塞或跳过的任务必须如实记录。
7. 保存最终报告 JSON；如需要，再整理成 Markdown 展示版。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 最终报告生成任务。请基于我提供的 customer profile、tool profile、task results、machine_score、manual review、execution log 和失败记录，生成结构化评估报告。不要编造未完成任务的结果，不要写评分脚本。

【任务目标】
生成最终评估报告 JSON，总结 AI 工具在采购合同 MVP 数据集上的本体抽取能力，包括输入覆盖、输出质量、证据链、冲突处理、不确定性表达、JSON 稳定性、主要风险和建议。

【报告要求】
1. 如实记录每个任务状态：completed、failed、blocked、skipped。
2. 总结工具环境限制，例如不能联网、不能读文件、不能执行命令、JSON 不稳定。
3. 总结 machine_score 中的 schema validation、coverage、missing evidence refs 和 possible hallucinations。
4. 明确说明 machine_score 是机器信号，不是最终人工评分。
5. 总结人工复核结论；人工复核缺失时不得给出无约束 ready。
6. 总结多源融合质量：alias、mapping、conflict、uncertainty 是否保留。
7. 总结禁止幻觉表现：是否出现无证据对象、无证据规则、过度推断。
8. 给出风险和建议，但不要超出输入材料。
9. 如果给出 overall_grade，只能作为人工复核后的定性判断，不要声称是自动评分。

【输出要求】
只输出合法 JSON，字段名使用英文，并尽量兼容 evaluation_report.schema.json：
{
  "report_id": "report:<evaluation_id>",
  "title": "Procurement Contract MVP Ontology Extraction Evaluation Report",
  "customer_profile_ref": "customer:<evaluation_id>",
  "tool_profile_ref": "tool:<evaluation_id>",
  "evaluation_period": {
    "start_date": "2026-07-03",
    "end_date": "2026-07-03"
  },
  "executive_summary": "",
  "overall_grade": "N/A",
  "capability_results": [
    {
      "capability_id": "cap:structured_output",
      "capability_name": "Structured Output",
      "grade": "N/A",
      "task_result_refs": [],
      "notes": ""
    }
  ],
  "task_result_refs": [],
  "redline_results": [],
  "score_caps": [],
  "key_findings": [],
  "risks": [],
  "recommendations": [],
  "conclusion": {
    "decision": "insufficient_data",
    "rationale": "",
    "next_steps": []
  },
  "generated_at": "2026-07-03T00:00:00Z",
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "evaluation_outputs"
  }
}

【字段约束】
- conclusion.decision 只能使用：ready、ready_with_constraints、not_ready、insufficient_data。
- overall_score 如果没有人工确认，不要输出该字段；不要输出 null。
- 不要添加 evaluation_report.schema.json 未定义的顶层字段，例如 ontology_coverage、evidence_quality、fusion_quality、task_summary。
- machine_score 中的信息应写入 key_findings、risks、redline_results、score_caps 或 capability_results.notes。

【证据要求】
关键发现必须引用 task_result_refs、machine_score section 名称、manual review 结论或 raw output 路径；失败任务必须引用失败记录或 raw output 路径。

【不确定性要求】
输入结果缺失时写 insufficient_data；覆盖数量无法可靠统计时在 risks 或 key_findings 中说明原因。

【禁止事项】
不要假装运行了未运行的任务；不要编造评分、通过率、模型能力或客户名称；不要生成评分脚本；不要把 possible hallucinations 直接当成确认幻觉。
```

## 输出文件名

Canonical 结构化输出：

`results/<evaluation_id>/report/evaluation_report.json`

可选 Markdown 展示输出：

`results/<evaluation_id>/report/final_eval_report.md`

## 输出格式

- 单个合法 JSON 对象。
- 尽量兼容 `schemas/evaluation_report.schema.json`。
- 字段名使用英文。
- Markdown 展示版只能由 JSON 报告、machine score 和人工复核内容整理，不得新增无依据结论。

## 证据链要求

- 关键发现、风险、建议应关联任务输出、machine score、manual review 或失败记录。
- 统计来自融合本体时引用 `task_05_multi_source_fusion` 或 repaired output。

## 不确定性表达要求

- 缺失任务结果、无法统计、输入不完整必须明确记录。
- 结论需要区分 ready、ready_with_constraints、not_ready、insufficient_data。

## 禁止幻觉要求

- 不得编造未完成任务。
- 不得生成不存在的分数依据。
- 不得把定性判断包装成自动评分。

## 允许追问次数

最多 2 次。允许追问缺失关键任务输出、评估周期、工具名称、customer profile ref 或人工复核结论。

## 常见失败情况

- 报告与实际任务结果不一致。
- 把失败任务写成完成。
- 编造分数或评分脚本。
- 缺少风险和限制。
- 输出 JSON 不合法。
- 输出 schema 不允许的字段。

## 失败记录方式

```json
{
  "task_id": "TASK-07",
  "status": "failed",
  "failure_type": "invalid_json | fabricated_result | missing_failure_record | unsupported_score | schema_mismatch | incomplete_report | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "raw_outputs/task_07_final_report_generation_raw.md"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须有来源说明，证据不足时必须写入 risks 或 key_findings。
- 多源差异不得被静默合并；需要在报告中说明 conflict 或 uncertainty。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

## A5 结果保存补充说明

- 不要把 `datasets/generic_procurement_contract_mvp/gold/`、`results/demo_baseline/`、`machine_score.json` 或人工复核内容提供给被评估 AI，除非本任务明确要求 machine_score/manual review 作为报告输入。
- AI 原始回答保存到 `results/<evaluation_id>/raw_outputs/`。
- 结构化报告保存到 `results/<evaluation_id>/report/evaluation_report.json`。
- Markdown 展示报告保存到 `results/<evaluation_id>/report/final_eval_report.md`。
- 复制 prompt 时只复制 fenced code block 内的内容；不要把操作员步骤、输出文件名说明或 gold/reference 路径复制给被评估 AI。
