# Role Permission Matrix

## Roles

| Role | Description |
|---|---|
| Requester | Creates and submits Purchase Requests |
| Department Manager | Approves normal Purchase Requests for their department |
| Procurement Specialist | Reviews supplier, prepares contracts, releases purchase orders |
| Finance Manager | Approves high-value purchase requests and payment applications |
| Legal Reviewer | Reviews and approves contract legal terms |
| Warehouse Clerk | Records goods receipt or GRN |
| AP Clerk | Performs invoice matching and creates payment requests |
| Procurement Admin | Maintains master data and can override some workflow issues |

## Permissions

| Action | Requester | Department Manager | Procurement Specialist | Finance Manager | Legal Reviewer | Warehouse Clerk | AP Clerk | Procurement Admin |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Create Purchase Request | Yes | Yes | Yes | No | No | No | No | Yes |
| Submit Purchase Request | Yes | Yes | Yes | No | No | No | No | Yes |
| Approve normal Purchase Request | No | Yes | No | No | No | No | No | Yes |
| Approve high-value Purchase Request | No | No | No | Yes | No | No | No | Yes |
| Select Supplier | No | No | Yes | No | No | No | No | Yes |
| Draft Contract | No | No | Yes | No | No | No | No | Yes |
| Legal Review Contract | No | No | No | No | Yes | No | No | Yes |
| Activate Contract | No | No | Yes | No | No | No | No | Yes |
| Release Purchase Order | No | No | Yes | No | No | No | No | Yes |
| Record Goods Receipt | No | No | No | No | No | Yes | No | Yes |
| Match Invoice | No | No | No | No | No | No | Yes | Yes |
| Approve Payment Application | No | No | No | Yes | No | No | No | Yes |
| Mark Payment Paid | No | No | No | Yes | No | No | No | Yes |
