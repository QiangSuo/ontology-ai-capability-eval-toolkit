# Screenshot Surrogate Inputs

## Purpose

This directory contains optional screenshot surrogate inputs for the B2 screenshot extension of the generic procurement contract MVP dataset.

A screenshot surrogate is a Markdown representation of a UI screen. It captures visible labels, fields, tables, buttons, states, business terms, candidate ontology mappings and evidence handles in text form.

## What These Files Test

These files can be provided to an AI tool only when the evaluation lead explicitly enables the optional screenshot-surrogate task. They can test whether the tool can:

- extract UI business terms from text-based screen descriptions;
- map visible fields to ontology attributes and relations;
- map buttons to candidate actions;
- map badges and labels to candidate states;
- record UI-derived evidence handles;
- distinguish UI evidence from code, DDL, CSV and document evidence.

## What These Files Do Not Test

These files do not test real screenshot or vision capability. They do not include PNG/JPG image files and do not test:

- OCR quality;
- visual layout detection;
- icon recognition;
- bounding boxes or region coordinates;
- pixel-level visual perception;
- browser automation or live UI access.

If a tool only receives these `.screen.md` files, its UI capability must be reported as `surrogate_only`, not `real_image`.

## Files

- `purchase_request_list.screen.md` — purchase request search/list page.
- `purchase_request_detail.screen.md` — purchase request detail page with line items and approval history.
- `approval_task.screen.md` — approval task workbench.
- `contract_detail.screen.md` — contract lifecycle detail page.
- `invoice_payment.screen.md` — invoice matching and payment request workbench.

The machine-readable inventory is `../metadata/screenshot_manifest.json`.

## Usage Rules

- Provide these files only for optional screenshot-surrogate evaluation.
- Do not provide `gold/`, scoring outputs or demo results to the AI tool under evaluation.
- Require every UI-derived claim to cite a `screen:*` evidence handle.
- Require the tool to declare `input_mode = surrogate_only`.
- Require conflicts and uncertainties when UI terms differ from code, DDL, CSV or documents.
- Do not treat button visibility as proof of backend behavior unless other sources support it.

## Future Task Numbering

Future screenshot prompts should use `task_08_screenshot_to_ontology.md` or a dedicated B-series namespace.

Do not use `task_06_screenshot_to_ontology.md`, because `task_06_schema_repair.md` already exists. Do not use `task_07_*` for screenshot or Web work, because `task_07_final_report_generation.md` already exists.
