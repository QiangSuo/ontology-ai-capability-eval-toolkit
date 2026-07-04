# Web Known Conflicts (Evaluator Only)

These Web conflict notes are evaluator-only review aids. Do not provide them to AI tools under evaluation.

| Conflict ID | Type | Severity | Expected handling |
| --- | --- | --- | --- |
| `web_conflict:web_vs_document_flow_mismatch` | `web_vs_document_flow_mismatch` | medium | Record as candidate page-flow evidence and do not claim it is the only or canonical process order. |
| `web_conflict:page_action_without_backend_evidence` | `page_action_without_backend_evidence` | high | Keep as candidate actions with uncertainty until fused with non-Web sources. |
| `web_conflict:ui_vs_database_naming_mismatch` | `ui_vs_database_naming_mismatch` | medium | Create aliases and mappings rather than duplicate concepts. |
| `web_conflict:role_permission_web_vs_doc_mismatch` | `role_permission_web_vs_doc_mismatch` | medium | Represent as role visibility evidence or permission candidates with uncertainty. |
| `web_conflict:missing_page_or_broken_link` | `missing_page_or_broken_link` | high | Record missing pages and do not invent unseen fields or flows. |
| `web_conflict:web_only_business_term` | `web_only_business_term` | medium | Represent as Web-only candidates or uncertainties; do not add required database fields without evidence. |
