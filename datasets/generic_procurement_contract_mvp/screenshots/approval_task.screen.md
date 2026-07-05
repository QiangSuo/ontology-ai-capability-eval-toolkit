# Screenshot Surrogate: Approval Task

## Page Metadata

- page_id: `screen:approval_task`
- page_name: Approval Task Workbench
- page_type: approval_task
- user_role: Department Manager / Finance Manager / Legal Reviewer
- input_mode: surrogate_only
- source_location: `screenshots/approval_task.screen.md#screen:approval_task`

## Visible Layout

- Top navigation: Workflow > My Approval Tasks
- Page title: My Approval Tasks
- Left panel: pending task list
- Main panel: selected approval target details
- Footer: Approve, Reject, Return, View Source Document

## Visible Fields

| UI label | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| Task ID | APR-90001 | `attr:approval_task.approval_id` | `screen:approval_task.field.task_id` |
| Target Type | Purchase Request | `attr:approval_task.target_type` / `concept:purchase_request` | `screen:approval_task.field.target_type` |
| Target No | PR-2024-001 | `attr:approval_task.target_id` plus target document ref | `screen:approval_task.field.target_no` |
| Step | Finance Review | `attr:approval_task.step_name` | `screen:approval_task.field.step` |
| Approver Role | Finance Manager | `role:finance_manager` | `screen:approval_task.field.approver_role` |
| Submitted At | 2024-03-11 10:05 | `attr:approval_task.submitted_at` | `screen:approval_task.field.submitted_at` |
| Amount | CNY 68000.00 | `attr:purchase_request.estimated_amount` | `screen:approval_task.field.amount` |
| Requester | Alice Chen | `concept:employee` | `screen:approval_task.field.requester` |
| Comment | Required when rejecting | `attr:approval_task.approval_comment` / `rule:rejection_requires_comment` | `screen:approval_task.field.comment` |

## Table Columns

Pending task list:

| Column | Candidate ontology mapping | Evidence handle |
| --- | --- | --- |
| Task ID | `attr:approval_task.approval_id` | `screen:approval_task.column.task_id` |
| Target Type | `attr:approval_task.target_type` | `screen:approval_task.column.target_type` |
| Target No | target object number | `screen:approval_task.column.target_no` |
| Step | `attr:approval_task.step_name` | `screen:approval_task.column.step` |
| Status | `attr:approval_task.approval_status` | `screen:approval_task.column.status` |
| Submitted At | `attr:approval_task.submitted_at` | `screen:approval_task.column.submitted_at` |

## Button Actions

| Button | Visibility | Candidate action | Evidence handle |
| --- | --- | --- | --- |
| Approve | Assigned approver | `action:approve_normal_purchase_request` or `action:approve_high_value_purchase_request` | `screen:approval_task.button.approve` |
| Reject | Assigned approver | `action:reject_purchase_request` | `screen:approval_task.button.reject` |
| Return | Assigned approver | `action:return_for_revision` | `screen:approval_task.button.return` |
| View Source Document | All approvers | `action:view_purchase_request` | `screen:approval_task.button.view_source` |

## Status Display

- PENDING: yellow badge in task list and detail panel.
- APPROVED: green badge in completed history.
- REJECTED: red badge; rejection comment required.
- SKIPPED: grey badge for bypassed approval step.

## Page Business Terms

- Approval Task
- Approval Record
- Finance Review
- Department Review
- Legal Review
- Approver Role
- Source Document
- Reject Comment

## Extractable Ontology Candidates

### Concepts

- `concept:approval_task`
- `concept:purchase_request`
- `concept:payment`
- `concept:contract`
- `concept:employee`

### Attributes

- `attr:approval_task.approval_id`
- `attr:approval_task.target_type`
- `attr:approval_task.target_id`
- `attr:approval_task.step_name`
- `attr:approval_task.approver_user_id`
- `attr:approval_task.approval_status`
- `attr:approval_task.approval_comment`
- `attr:approval_task.submitted_at`
- `attr:approval_task.decided_at`

### Relations

- `rel:approval_task.approves_purchase_request`
- `rel:approval_task.approves_payment`
- `rel:approval_task.performed_by_employee`
- `rel:purchase_request.has_approval_task`
- `rel:payment.has_approval_task`

### Actions

- `action:approve_normal_purchase_request`
- `action:approve_high_value_purchase_request`
- `action:approve_payment`
- `action:reject_purchase_request`
- `action:view_purchase_request`

### States

- Approval status: PENDING, APPROVED, REJECTED, SKIPPED

## Naming Differences vs DDL / Documents / Code

| UI term | Other source term | Difference |
| --- | --- | --- |
| Task ID | `approval_id` | UI workflow term vs database record ID |
| Target No | `target_id` | UI displays document number; DDL stores numeric target ID |
| Finance Review | Finance Manager Approval | Step label vs role/rule description |
| Source Document | Purchase Request / Contract / Payment Request | Generic UI label for polymorphic target |
| Return | not explicit in core gold actions | UI-only workflow action candidate needing confirmation |

## Evidence Source Locations

- `screen:approval_task.page`: approval workbench supports approval task concept.
- `screen:approval_task.field.target_type`: target_type supports polymorphic approval target.
- `screen:approval_task.button.approve`: approve button supports approval actions.
- `screen:approval_task.button.reject`: reject button supports rejection action and comment rule.
- `screen:approval_task.status.pending`: PENDING badge supports approval status.

## Limitations

The UI shows a generic Target Type / Target No pattern. It supports polymorphic approval semantics but does not by itself prove all backend target types. Return action is screenshot-only evidence and should be marked candidate or uncertainty unless supported elsewhere.
