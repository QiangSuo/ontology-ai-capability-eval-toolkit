# Demo Web Execution Log

- Evaluation ID: `demo_web`
- Input mode: `html_snapshot`
- Network access: disabled
- Live Web/browser automation: not used

## Inputs Provided To Simulated Tool

- `datasets/generic_procurement_contract_mvp/web_snapshots/*.html`
- `datasets/generic_procurement_contract_mvp/web_map/page_map.json`
- `datasets/generic_procurement_contract_mvp/web_map/page_map.md`
- Task 12/13/14 prompts

Evaluator-only `gold/*`, `known_conflicts*`, scoring outputs and demo outputs were not provided as task inputs. The `web:*` handles generated in normalized outputs are output-side traceability handles; they are validated by the evaluator after the task, not supplied as gold/reference input.

## Notes

This is a deterministic demo sample. It demonstrates optional Web evidence handling and scoring integration; it is not a real tool performance measurement.
