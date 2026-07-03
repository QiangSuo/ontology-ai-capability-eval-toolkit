# Task 07: 最终报告生成

## 任务目标

基于环境检查、单源抽取、多源融合和 schema repair 记录，生成一次采购合同 MVP 评估的最终报告 JSON。报告关注工具组合能力总结、任务完成情况、风险、冲突处理、不确定性表达和后续建议；不生成评分脚本。

## 输入材料

- `results/task_00_environment_check.json`
- `results/task_01_code_to_ontology.json`
- `results/task_02_ddl_to_ontology.json`
- `results/task_03_sample_data_profile.json`
- `results/task_04_document_to_ontology.json`
- `results/task_05_multi_source_fusion.json`
- `results/task_06_schema_repair.json`
- 原始失败记录，如有。
- 可参考 schema：`schemas/evaluation_report.schema.json`、`schemas/task_result.schema.json`。

## 操作员步骤

1. 将所有任务输出和失败记录提供给 AI 工具。
2. 要求 AI 生成结构化最终报告，不写评分脚本。
3. 报告必须区分事实、能力判断、风险和建议。
4. 失败、阻塞或跳过的任务必须如实记录。
5. 保存最终报告 JSON。

## 给 AI 工具复制使用的完整 prompt

```text
你正在执行采购合同 MVP 最终报告生成任务。请基于我提供的环境检查、单源抽取、多源融合、schema repair 和失败记录，生成结构化评估报告。不要编造未完成任务的结果，不要写评分脚本。

【任务目标】
生成最终评估报告 JSON，总结 AI 工具在采购合同 MVP 数据集上的本体抽取能力，包括输入覆盖、输出质量、证据链、冲突处理、不确定性表达、JSON 稳定性、主要风险和建议。

【报告要求】
1. 如实记录每个任务状态：completed、failed、blocked、skipped。
2. 总结工具环境限制，例如不能联网、不能读文件、不能执行命令、JSON 不稳定。
3. 总结本体覆盖情况：concept、attribute、relation、event、rule、action、state、role、permission。
4. 总结证据链质量：evidence_refs 是否能追溯到 code/ddl/csv/doc。
5. 总结多源融合质量：是否正确归并 alias，是否保留 mapping，是否识别 conflict 和 uncertainty。
6. 总结禁止幻觉表现：是否出现无证据对象、无证据规则、过度推断。
7. 给出风险和建议，但不要超出输入材料。
8. 如果给出 overall_grade，只能作为定性判断，不要声称是自动评分。

【输出要求】
只输出合法 JSON，字段名使用英文：
{
  "report_id": "procurement-contract-mvp-evaluation-report",
  "title": "Procurement Contract MVP Ontology Extraction Evaluation Report",
  "customer_profile_ref": "",
  "tool_profile_ref": "",
  "evaluation_period": {
    "start_date": "",
    "end_date": ""
  },
  "executive_summary": "",
  "overall_score": null,
  "overall_grade": "N/A",
  "task_summary": [],
  "capability_results": [],
  "ontology_coverage": {
    "concept_count": null,
    "attribute_count": null,
    "relation_count": null,
    "event_count": null,
    "rule_count": null,
    "action_count": null,
    "state_count": null,
    "role_count": null,
    "permission_count": null
  },
  "evidence_quality": {
    "has_code_evidence": null,
    "has_ddl_evidence": null,
    "has_csv_evidence": null,
    "has_document_evidence": null,
    "notes": []
  },
  "fusion_quality": {
    "alias_handling_notes": [],
    "mapping_notes": [],
    "conflict_notes": [],
    "uncertainty_notes": []
  },
  "redline_results": [],
  "score_caps": [],
  "key_findings": [],
  "risks": [],
  "recommendations": [],
  "conclusion": {
    "decision": "ready | ready_with_constraints | not_ready | insufficient_data",
    "rationale": "",
    "next_steps": []
  },
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "evaluation_outputs"
  }
}

【证据要求】
关键发现必须引用 task output 或 evidence_refs；失败任务必须引用失败记录或 raw output 路径。

【不确定性要求】
输入结果缺失时写 insufficient_data；覆盖数量无法可靠统计时使用 null 并说明原因。

【禁止事项】
不要假装运行了未运行的任务；不要编造评分、通过率、模型能力或客户名称；不要生成评分脚本。
```

## 输出文件名

`results/task_07_final_report_generation.json`

## 输出格式

- 单个合法 JSON 对象。
- 尽量兼容 `schemas/evaluation_report.schema.json`。
- 字段名使用英文。

## 证据链要求

- 关键发现、风险、建议应关联任务输出或失败记录。
- 统计来自融合本体时引用 `task_05_multi_source_fusion` 或 repaired output。

## 不确定性表达要求

- 缺失任务结果、无法统计、输入不完整必须明确记录。
- 结论需要区分 ready、ready_with_constraints、not_ready、insufficient_data。

## 禁止幻觉要求

- 不得编造未完成任务。
- 不得生成不存在的分数依据。
- 不得把定性判断包装成自动评分。

## 允许追问次数

最多 2 次。允许追问缺失关键任务输出、评估周期、工具名称或客户 profile ref。

## 常见失败情况

- 报告与实际任务结果不一致。
- 把失败任务写成完成。
- 编造分数或评分脚本。
- 缺少风险和限制。
- 输出 JSON 不合法。

## 失败记录方式

```json
{
  "task_id": "TASK-07",
  "status": "failed",
  "failure_type": "invalid_json | fabricated_result | missing_failure_record | unsupported_score | incomplete_report | other",
  "failure_description": "",
  "retry_count": 0,
  "raw_output_path": "results/raw/task_07_final_report_generation_raw_output.txt"
}
```

## 通用约束

- 固定提示词不得暗示标准答案或 gold answer。
- AI 工具只能基于本任务输入材料作答，不得使用外部知识补全业务事实。
- 字段名使用英文；字段值、说明、备注可以使用中文。
- 关键结论必须包含 `evidence_refs`、`confidence`，证据不足时必须包含 `uncertainties`。
- 多源差异不得被静默合并；需要写入 `aliases`、`mappings`、`conflicts` 或 `uncertainties`。
- 不要使用依赖某个工具专属能力的表达；如果工具不能读文件，操作员可复制粘贴材料。

