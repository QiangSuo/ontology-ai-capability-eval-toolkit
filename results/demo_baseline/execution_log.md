# Demo Baseline Execution Log

This is a simulated execution log for `results/demo_baseline/`.

- Dataset: `datasets/generic_procurement_contract_mvp/`
- Mode: fixed prompt demo sample
- Operator profile: low experience
- Tool profile: `tool_profile.json`
- Scope: MVP only; no screenshot or Web extension

Known intentional imperfections:

1. The fused ontology omits `concept:material` and `concept:goods_receipt`.
2. Several required attributes are missing, especially optional lifecycle timestamps and goods receipt fields.
3. Several relations are missing, including goods receipt and material relations.
4. `concept:budget_reservation` is weakly inferred and should be flagged as possible hallucination.
5. `doc:nonexistent_budget_policy` is an intentionally broken evidence reference.
