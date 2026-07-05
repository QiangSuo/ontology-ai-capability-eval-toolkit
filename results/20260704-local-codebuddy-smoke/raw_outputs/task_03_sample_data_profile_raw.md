{
  "task_id": "TASK-03",
  "title": "Procurement Contract MVP Sample Data Profile",
  "source_system": "sample_data_csv",
  "sample_is_partial": true,
  "table_profiles": [
    {
      "file_name": "pc_department.csv",
      "row_count": 6,
      "candidate_concept": "Department",
      "columns": [
        {
          "column_name": "department_id",
          "inferred_type": "integer",
          "sample_values": [
            10,
            20,
            30
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Department identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_department#column:department_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "department_code",
          "inferred_type": "string_code",
          "sample_values": [
            "OPS",
            "IT",
            "FIN",
            "LEGAL",
            "WH",
            "ADMIN"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Short department code.",
          "candidate_enum_values": [
            "OPS",
            "IT",
            "FIN",
            "LEGAL",
            "WH",
            "ADMIN"
          ],
          "evidence_refs": [
            "csv:pc_department#column:department_code"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "department_name",
          "inferred_type": "string",
          "sample_values": [
            "Operations",
            "Information Technology",
            "Finance"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Department display name.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_department#column:department_name"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "cost_center",
          "inferred_type": "string_code",
          "sample_values": [
            "CC-100",
            "CC-200",
            "CC-300"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Cost center code associated with department.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_department#column:cost_center"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "is_active",
          "inferred_type": "boolean",
          "sample_values": [
            "true"
          ],
          "null_observation": "No nulls observed in sample; only true appears.",
          "candidate_attribute": "Active flag.",
          "candidate_enum_values": [
            "true"
          ],
          "evidence_refs": [
            "csv:pc_department#column:is_active"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "created_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-01-02 09:00:00",
            "2026-01-02 09:05:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Record creation timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_department#column:created_at"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "pc_user.department_id, pc_purchase_request.department_id may reference pc_department.department_id"
      ],
      "data_quality_notes": [
        "No duplicate department_id observed in sample.",
        "is_active has no false examples, so inactive department behavior is not observable."
      ],
      "evidence_refs": [
        "csv:pc_department"
      ]
    },
    {
      "file_name": "pc_user.csv",
      "row_count": 9,
      "candidate_concept": "User",
      "columns": [
        {
          "column_name": "user_id",
          "inferred_type": "integer",
          "sample_values": [
            1001,
            1002,
            1003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "User identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_user#column:user_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "user_name",
          "inferred_type": "string",
          "sample_values": [
            "Avery Lin",
            "Blair Chen",
            "Casey Wu"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "User display name.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_user#column:user_name"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "role_code",
          "inferred_type": "enum_string",
          "sample_values": [
            "REQUESTER",
            "DEPT_MANAGER",
            "PROCUREMENT_SPECIALIST"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "User role code.",
          "candidate_enum_values": [
            "REQUESTER",
            "DEPT_MANAGER",
            "PROCUREMENT_SPECIALIST",
            "FINANCE_MANAGER",
            "LEGAL_REVIEWER",
            "WAREHOUSE_CLERK",
            "AP_CLERK",
            "PROCUREMENT_ADMIN"
          ],
          "evidence_refs": [
            "csv:pc_user#column:role_code"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "department_id",
          "inferred_type": "integer",
          "sample_values": [
            20,
            60,
            30
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Department identifier for user; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_user#column:department_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "email",
          "inferred_type": "string_email",
          "sample_values": [
            "avery.lin@example.test",
            "blair.chen@example.test"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "User email.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_user#column:email"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "is_active",
          "inferred_type": "boolean",
          "sample_values": [
            "true"
          ],
          "null_observation": "No nulls observed in sample; only true appears.",
          "candidate_attribute": "Active flag.",
          "candidate_enum_values": [
            "true"
          ],
          "evidence_refs": [
            "csv:pc_user#column:is_active"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "created_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-01-03 08:00:00",
            "2026-01-03 08:05:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Record creation timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_user#column:created_at"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "pc_user.department_id appears to reference pc_department.department_id",
        "pc_purchase_request.requester_user_id, pc_contract.legal_reviewer_id, pc_approval_record.approver_user_id, pc_goods_receipt.received_by, pc_payment_request.approved_by may reference pc_user.user_id"
      ],
      "data_quality_notes": [
        "No duplicate user_id observed in sample.",
        "is_active has no false examples."
      ],
      "evidence_refs": [
        "csv:pc_user"
      ]
    },
    {
      "file_name": "pc_supplier.csv",
      "row_count": 7,
      "candidate_concept": "Supplier",
      "columns": [
        {
          "column_name": "supplier_id",
          "inferred_type": "integer",
          "sample_values": [
            2001,
            2002,
            2003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_supplier#column:supplier_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "supplier_code",
          "inferred_type": "string_code",
          "sample_values": [
            "SUP-ASTER",
            "SUP-BRAVO",
            "SUP-CEDAR"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier code.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_supplier#column:supplier_code"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "supplier_name",
          "inferred_type": "string",
          "sample_values": [
            "Aster Office Supply Co.",
            "Bravo Industrial Services"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier legal or display name.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_supplier#column:supplier_name"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "supplier_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "ACTIVE",
            "SUSPENDED",
            "PENDING_REVIEW"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier lifecycle/status.",
          "candidate_enum_values": [
            "ACTIVE",
            "SUSPENDED",
            "PENDING_REVIEW"
          ],
          "evidence_refs": [
            "csv:pc_supplier#column:supplier_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "risk_rating",
          "inferred_type": "enum_string",
          "sample_values": [
            "LOW",
            "MEDIUM",
            "HIGH"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier risk rating.",
          "candidate_enum_values": [
            "LOW",
            "MEDIUM",
            "HIGH"
          ],
          "evidence_refs": [
            "csv:pc_supplier#column:risk_rating"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "contact_email",
          "inferred_type": "string_email",
          "sample_values": [
            "contact@aster-supply.example.test",
            "service@bravo-industrial.example.test"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier contact email.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_supplier#column:contact_email"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "onboarded_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2025-09-01 10:00:00",
            "2025-09-15 10:00:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier onboarding timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_supplier#column:onboarded_at"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "pc_purchase_request.preferred_supplier_id, pc_contract.supplier_id, pc_purchase_order.supplier_id, pc_invoice.supplier_id may reference pc_supplier.supplier_id"
      ],
      "data_quality_notes": [
        "No duplicate supplier_id observed in sample.",
        "SUSPENDED supplier appears in terminated contract and cancelled PO/invoice/payment rows; candidate lifecycle linkage only."
      ],
      "evidence_refs": [
        "csv:pc_supplier"
      ]
    },
    {
      "file_name": "pc_purchase_request.csv",
      "row_count": 10,
      "candidate_concept": "Purchase Request",
      "columns": [
        {
          "column_name": "request_id",
          "inferred_type": "integer",
          "sample_values": [
            3001,
            3002,
            3003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase request identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:request_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "request_no",
          "inferred_type": "string_code",
          "sample_values": [
            "PR-2026-0001",
            "PR-2026-0002"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase request number; PR abbreviation candidate.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:request_no"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "request_title",
          "inferred_type": "string",
          "sample_values": [
            "Laptop refresh for analytics team",
            "Warehouse barcode scanner purchase"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Request title.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:request_title"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "requester_user_id",
          "inferred_type": "integer",
          "sample_values": [
            1001,
            1009
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Requester user identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:requester_user_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "department_id",
          "inferred_type": "integer",
          "sample_values": [
            20,
            10
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Requesting department identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:department_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "preferred_supplier_id",
          "inferred_type": "integer",
          "sample_values": [
            2003,
            2005,
            2001
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Preferred supplier identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:preferred_supplier_id"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "estimated_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            72500,
            8900
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Estimated request amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:estimated_amount"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "currency_code",
          "inferred_type": "string_code",
          "sample_values": [
            "CNY"
          ],
          "null_observation": "No nulls observed in sample; only CNY appears.",
          "candidate_attribute": "Currency code.",
          "candidate_enum_values": [
            "CNY"
          ],
          "evidence_refs": [
            "csv:pc_purchase_request#column:currency_code"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "request_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "APPROVED",
            "SUBMITTED",
            "REJECTED",
            "DRAFT",
            "CANCELLED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase request status.",
          "candidate_enum_values": [
            "APPROVED",
            "SUBMITTED",
            "REJECTED",
            "DRAFT",
            "CANCELLED"
          ],
          "evidence_refs": [
            "csv:pc_purchase_request#column:request_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "business_justification",
          "inferred_type": "string",
          "sample_values": [
            "Replace aging laptops for data analytics work",
            "Improve receiving accuracy for warehouse operations"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Business justification text.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:business_justification"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "required_by_date",
          "inferred_type": "date",
          "sample_values": [
            "2026-03-15",
            "2026-03-20"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Required-by date.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:required_by_date"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "submitted_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-01 09:10:00",
            "2026-02-02 10:20:00"
          ],
          "null_observation": "Null/blank observed for DRAFT row 3005.",
          "candidate_attribute": "Submission timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:submitted_at",
            "csv:pc_purchase_request#row:6"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "approved_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-01 14:30:00",
            "2026-02-03 11:15:00"
          ],
          "null_observation": "Null/blank observed for SUBMITTED, REJECTED, DRAFT and CANCELLED sample rows.",
          "candidate_attribute": "Approval timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:approved_at",
            "csv:pc_purchase_request#row:4",
            "csv:pc_purchase_request#row:5",
            "csv:pc_purchase_request#row:6",
            "csv:pc_purchase_request#row:8"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "created_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-01 08:50:00",
            "2026-02-02 09:40:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Record creation timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request#column:created_at"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "request_id is referenced by pc_purchase_request_line.request_id, pc_contract.request_id, pc_purchase_order.request_id and pc_approval_record.target_id where target_type is PURCHASE_REQUEST",
        "requester_user_id appears to reference pc_user.user_id",
        "department_id appears to reference pc_department.department_id",
        "preferred_supplier_id appears to reference pc_supplier.supplier_id"
      ],
      "data_quality_notes": [
        "No duplicate request_id observed in sample.",
        "approved_at is blank for multiple non-APPROVED states.",
        "submitted_at is blank for DRAFT row 3005.",
        "Contracts and POs reference request_id values 2990 and 2988 that are absent from this sample file."
      ],
      "evidence_refs": [
        "csv:pc_purchase_request"
      ]
    },
    {
      "file_name": "pc_purchase_request_line.csv",
      "row_count": 15,
      "candidate_concept": "Purchase Request Line",
      "columns": [
        {
          "column_name": "line_id",
          "inferred_type": "integer",
          "sample_values": [
            4001,
            4002,
            4003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase request line identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:line_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "request_id",
          "inferred_type": "integer",
          "sample_values": [
            3001,
            3002,
            3003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Parent purchase request identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:request_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "item_description",
          "inferred_type": "string",
          "sample_values": [
            "Standard business laptop",
            "Wireless barcode scanner"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Requested item or service description.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:item_description"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "category_code",
          "inferred_type": "enum_string",
          "sample_values": [
            "IT_HARDWARE",
            "WAREHOUSE_EQUIP",
            "OFFICE_SUPPLY"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Item/service category code.",
          "candidate_enum_values": [
            "IT_HARDWARE",
            "WAREHOUSE_EQUIP",
            "OFFICE_SUPPLY",
            "FACILITY_SERVICE",
            "LOGISTICS_SERVICE",
            "SAFETY_SUPPLY",
            "TRAINING_SERVICE"
          ],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:category_code"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "quantity",
          "inferred_type": "decimal_or_integer",
          "sample_values": [
            12,
            10,
            30
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Requested quantity.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:quantity"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "unit_of_measure",
          "inferred_type": "enum_string",
          "sample_values": [
            "EA",
            "BOX",
            "SET",
            "JOB"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Unit of measure.",
          "candidate_enum_values": [
            "EA",
            "BOX",
            "SET",
            "JOB",
            "DAY",
            "VISIT"
          ],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:unit_of_measure"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "estimated_unit_price",
          "inferred_type": "decimal",
          "sample_values": [
            3900,
            6800,
            450
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Estimated unit price.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:estimated_unit_price"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "line_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            68000,
            4500
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Line amount; appears compatible with quantity times estimated_unit_price in sample.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_request_line#column:line_amount"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "request_id appears to reference pc_purchase_request.request_id",
        "Multiple line rows can share one request_id, indicating candidate one-to-many relation from request to lines"
      ],
      "data_quality_notes": [
        "No duplicate line_id observed in sample.",
        "For visible sample rows, line_amount appears to equal quantity multiplied by estimated_unit_price; candidate rule only."
      ],
      "evidence_refs": [
        "csv:pc_purchase_request_line"
      ]
    },
    {
      "file_name": "pc_contract.csv",
      "row_count": 7,
      "candidate_concept": "Contract",
      "columns": [
        {
          "column_name": "contract_id",
          "inferred_type": "integer",
          "sample_values": [
            6001,
            6002,
            6003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:contract_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "contract_no",
          "inferred_type": "string_code",
          "sample_values": [
            "CT-2026-0001",
            "CT-2026-0002"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract number.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:contract_no"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "request_id",
          "inferred_type": "integer",
          "sample_values": [
            3001,
            3002,
            3006,
            2990
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related purchase request identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:request_id"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "supplier_id",
          "inferred_type": "integer",
          "sample_values": [
            2003,
            2005,
            2002
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:supplier_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "contract_title",
          "inferred_type": "string",
          "sample_values": [
            "Laptop refresh supply contract",
            "Warehouse scanner supply contract"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract title.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:contract_title"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "contract_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            72500,
            12600
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:contract_amount"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "contract_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "ACTIVE",
            "LEGAL_REVIEW",
            "DRAFT",
            "EXPIRED",
            "TERMINATED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract status.",
          "candidate_enum_values": [
            "ACTIVE",
            "LEGAL_REVIEW",
            "DRAFT",
            "EXPIRED",
            "TERMINATED"
          ],
          "evidence_refs": [
            "csv:pc_contract#column:contract_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "start_date",
          "inferred_type": "date",
          "sample_values": [
            "2026-02-14",
            "2026-02-15"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract start date.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:start_date"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "end_date",
          "inferred_type": "date",
          "sample_values": [
            "2026-05-31",
            "2026-06-30"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Contract end date.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:end_date"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "legal_reviewer_id",
          "inferred_type": "integer",
          "sample_values": [
            1005
          ],
          "null_observation": "Blank observed for DRAFT contract row 6004.",
          "candidate_attribute": "Legal reviewer user identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:legal_reviewer_id",
            "csv:pc_contract#row:5"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "legal_approved_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-13 16:30:00",
            "2026-02-14 17:00:00"
          ],
          "null_observation": "Blank observed for LEGAL_REVIEW and DRAFT rows.",
          "candidate_attribute": "Legal approval timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:legal_approved_at",
            "csv:pc_contract#row:4",
            "csv:pc_contract#row:5"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "activated_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-14 09:00:00",
            "2026-02-15 09:10:00"
          ],
          "null_observation": "Blank observed for LEGAL_REVIEW and DRAFT rows.",
          "candidate_attribute": "Activation timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:activated_at",
            "csv:pc_contract#row:4",
            "csv:pc_contract#row:5"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "termination_reason",
          "inferred_type": "string_nullable",
          "sample_values": [
            "Supplier suspended after risk review"
          ],
          "null_observation": "Mostly blank; populated for TERMINATED row 6007.",
          "candidate_attribute": "Termination reason text.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:termination_reason",
            "csv:pc_contract#row:8"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "created_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-12 10:00:00",
            "2026-02-13 10:00:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Record creation timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_contract#column:created_at"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "contract_id is referenced by pc_purchase_order.contract_id",
        "request_id appears to reference pc_purchase_request.request_id, but 2990 and 2988 are absent from the visible purchase request sample",
        "supplier_id appears to reference pc_supplier.supplier_id",
        "legal_reviewer_id appears to reference pc_user.user_id"
      ],
      "data_quality_notes": [
        "No duplicate contract_id observed in sample.",
        "request_id values 2990 and 2988 lack matching pc_purchase_request rows in the sample.",
        "LEGAL_REVIEW and DRAFT contracts have blank legal_approved_at and activated_at.",
        "DRAFT contract 6004 has a related released PO 7004 in sample, which may be a lifecycle inconsistency candidate."
      ],
      "evidence_refs": [
        "csv:pc_contract"
      ]
    },
    {
      "file_name": "pc_purchase_order.csv",
      "row_count": 8,
      "candidate_concept": "Purchase Order",
      "columns": [
        {
          "column_name": "po_id",
          "inferred_type": "integer",
          "sample_values": [
            7001,
            7002,
            7003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase order identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:po_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "po_no",
          "inferred_type": "string_code",
          "sample_values": [
            "PO-2026-0001",
            "PO-2026-0002"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase order number; PO abbreviation candidate.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:po_no"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "contract_id",
          "inferred_type": "integer",
          "sample_values": [
            6001,
            6002,
            6003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related contract identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:contract_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "request_id",
          "inferred_type": "integer",
          "sample_values": [
            3001,
            3002,
            3006,
            2990
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related purchase request identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:request_id"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "supplier_id",
          "inferred_type": "integer",
          "sample_values": [
            2003,
            2005,
            2002
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:supplier_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "po_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            72500,
            12600
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase order amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:po_amount"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "po_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "CLOSED",
            "PARTIALLY_RECEIVED",
            "RELEASED",
            "CANCELLED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Purchase order status.",
          "candidate_enum_values": [
            "CLOSED",
            "PARTIALLY_RECEIVED",
            "RELEASED",
            "CANCELLED"
          ],
          "evidence_refs": [
            "csv:pc_purchase_order#column:po_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "released_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-14 10:00:00",
            "2026-02-15 10:30:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "PO release timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:released_at"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "closed_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-24 17:00:00",
            "2025-02-10 17:30:00"
          ],
          "null_observation": "Blank observed for non-CLOSED statuses in sample.",
          "candidate_attribute": "PO close timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_purchase_order#column:closed_at",
            "csv:pc_purchase_order#row:3",
            "csv:pc_purchase_order#row:4",
            "csv:pc_purchase_order#row:5",
            "csv:pc_purchase_order#row:6",
            "csv:pc_purchase_order#row:8",
            "csv:pc_purchase_order#row:9"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "po_id is referenced by pc_goods_receipt.po_id and pc_invoice.po_id",
        "contract_id appears to reference pc_contract.contract_id",
        "request_id appears to reference pc_purchase_request.request_id, but 2990 and 2988 are absent from the visible purchase request sample",
        "supplier_id appears to reference pc_supplier.supplier_id"
      ],
      "data_quality_notes": [
        "No duplicate po_id observed in sample.",
        "contract_id 6002 appears on two PO rows, indicating possible one contract to many POs.",
        "PO amounts for contract_id 6002 are 72500.00 and 12000.00; combined amount exceeds the contract_amount 72500.00 in sample, candidate amount anomaly.",
        "PO 7003 references contract 6003 with LEGAL_REVIEW status; lifecycle sequencing may need validation.",
        "PO 7004 references contract 6004 with DRAFT status; lifecycle sequencing may need validation."
      ],
      "evidence_refs": [
        "csv:pc_purchase_order"
      ]
    },
    {
      "file_name": "pc_goods_receipt.csv",
      "row_count": 8,
      "candidate_concept": "Goods Receipt",
      "columns": [
        {
          "column_name": "receipt_id",
          "inferred_type": "integer",
          "sample_values": [
            8001,
            8002,
            8003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Goods receipt identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:receipt_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "receipt_no",
          "inferred_type": "string_code",
          "sample_values": [
            "GRN-2026-0001",
            "GRN-2026-0002"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Goods receipt note number; GRN abbreviation candidate.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:receipt_no"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "po_id",
          "inferred_type": "integer",
          "sample_values": [
            7001,
            7002,
            7003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related purchase order identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:po_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "receipt_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "COMPLETE",
            "PARTIAL",
            "PENDING",
            "REJECTED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Receipt status.",
          "candidate_enum_values": [
            "COMPLETE",
            "PARTIAL",
            "PENDING",
            "REJECTED"
          ],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:receipt_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "received_by",
          "inferred_type": "integer",
          "sample_values": [
            1006
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Receiving user identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:received_by"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "received_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-22 15:30:00",
            "2026-02-24 11:20:00"
          ],
          "null_observation": "Blank observed for PENDING receipt rows.",
          "candidate_attribute": "Receipt timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:received_at",
            "csv:pc_goods_receipt#row:4",
            "csv:pc_goods_receipt#row:5",
            "csv:pc_goods_receipt#row:6"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "inspection_result",
          "inferred_type": "enum_string",
          "sample_values": [
            "PASS",
            "NOT_REQUIRED",
            "FAIL"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Inspection result.",
          "candidate_enum_values": [
            "PASS",
            "NOT_REQUIRED",
            "FAIL"
          ],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:inspection_result"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "remarks",
          "inferred_type": "string",
          "sample_values": [
            "Laptops received and tagged",
            "Seven scanners received first batch"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Receipt remarks.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_goods_receipt#column:remarks"
          ],
          "confidence": 0.85
        }
      ],
      "candidate_relations": [
        "po_id appears to reference pc_purchase_order.po_id",
        "receipt_id is referenced by pc_invoice.receipt_id when present",
        "received_by appears to reference pc_user.user_id"
      ],
      "data_quality_notes": [
        "No duplicate receipt_id observed in sample.",
        "PENDING receipts have blank received_at and NOT_REQUIRED inspection_result in sample.",
        "REJECTED receipt 8007 has inspection_result FAIL."
      ],
      "evidence_refs": [
        "csv:pc_goods_receipt"
      ]
    },
    {
      "file_name": "pc_invoice.csv",
      "row_count": 9,
      "candidate_concept": "Invoice",
      "columns": [
        {
          "column_name": "invoice_id",
          "inferred_type": "integer",
          "sample_values": [
            8501,
            8502,
            8503
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Invoice identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:invoice_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "invoice_no",
          "inferred_type": "string_code",
          "sample_values": [
            "INV-2026-0101",
            "INV-2026-0102"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Invoice number.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:invoice_no"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "supplier_id",
          "inferred_type": "integer",
          "sample_values": [
            2003,
            2005,
            2002
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Supplier identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:supplier_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "po_id",
          "inferred_type": "integer",
          "sample_values": [
            7001,
            7002,
            7003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related purchase order identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:po_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "receipt_id",
          "inferred_type": "integer_nullable",
          "sample_values": [
            8001,
            8002,
            8006
          ],
          "null_observation": "Blank observed for invoice rows 8503, 8504 and 8505.",
          "candidate_attribute": "Related goods receipt identifier; candidate nullable foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:receipt_id",
            "csv:pc_invoice#row:4",
            "csv:pc_invoice#row:5",
            "csv:pc_invoice#row:6"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "invoice_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            72500,
            12600
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Invoice amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:invoice_amount"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "invoice_date",
          "inferred_type": "date",
          "sample_values": [
            "2026-02-23",
            "2026-02-25"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Invoice date.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:invoice_date"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "invoice_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "MATCHED",
            "PENDING_MATCH",
            "EXCEPTION",
            "CANCELLED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Invoice matching/status.",
          "candidate_enum_values": [
            "MATCHED",
            "PENDING_MATCH",
            "EXCEPTION",
            "CANCELLED"
          ],
          "evidence_refs": [
            "csv:pc_invoice#column:invoice_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "match_variance_amount",
          "inferred_type": "decimal_nullable",
          "sample_values": [
            0,
            650,
            150,
            300
          ],
          "null_observation": "Blank observed for PENDING_MATCH and CANCELLED rows.",
          "candidate_attribute": "Invoice matching variance amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:match_variance_amount",
            "csv:pc_invoice#row:3",
            "csv:pc_invoice#row:4",
            "csv:pc_invoice#row:6",
            "csv:pc_invoice#row:8"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "matched_at",
          "inferred_type": "datetime_nullable",
          "sample_values": [
            "2026-02-24 09:20:00",
            "2026-02-27 16:00:00"
          ],
          "null_observation": "Blank observed for PENDING_MATCH and CANCELLED rows.",
          "candidate_attribute": "Invoice match timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_invoice#column:matched_at",
            "csv:pc_invoice#row:3",
            "csv:pc_invoice#row:4",
            "csv:pc_invoice#row:6",
            "csv:pc_invoice#row:8"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "supplier_id appears to reference pc_supplier.supplier_id",
        "po_id appears to reference pc_purchase_order.po_id",
        "receipt_id appears to reference pc_goods_receipt.receipt_id when not blank",
        "invoice_id is referenced by pc_payment_request.invoice_id"
      ],
      "data_quality_notes": [
        "No duplicate invoice_id observed in sample.",
        "Invoice 8509 shares supplier_id, po_id and receipt_id with invoice 8501 and has small amount 300.00 with EXCEPTION status; candidate duplicate/additional-charge anomaly.",
        "Invoice 8504 amount 19050.00 differs from PO 7004 amount 18400.00 by 650.00 and has EXCEPTION status.",
        "MATCHED invoice 8508 has non-zero match_variance_amount 150.00, so MATCHED does not necessarily imply zero variance in sample.",
        "PENDING_MATCH rows have blank matched_at and blank match_variance_amount."
      ],
      "evidence_refs": [
        "csv:pc_invoice"
      ]
    },
    {
      "file_name": "pc_payment_request.csv",
      "row_count": 8,
      "candidate_concept": "Payment Request",
      "columns": [
        {
          "column_name": "payment_request_id",
          "inferred_type": "integer",
          "sample_values": [
            9001,
            9002,
            9003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Payment request identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:payment_request_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "payment_no",
          "inferred_type": "string_code",
          "sample_values": [
            "PAY-2026-0001",
            "PAY-2026-0002"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Payment request/application number; Payment Application alias candidate.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:payment_no"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "invoice_id",
          "inferred_type": "integer",
          "sample_values": [
            8501,
            8502,
            8503
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Related invoice identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:invoice_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "payment_amount",
          "inferred_type": "decimal",
          "sample_values": [
            46800,
            72500,
            12600
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Requested payment amount.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:payment_amount"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "payment_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "PAID",
            "REQUESTED",
            "HELD",
            "CANCELLED",
            "APPROVED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Payment request status.",
          "candidate_enum_values": [
            "PAID",
            "REQUESTED",
            "HELD",
            "CANCELLED",
            "APPROVED"
          ],
          "evidence_refs": [
            "csv:pc_payment_request#column:payment_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "due_date",
          "inferred_type": "date",
          "sample_values": [
            "2026-03-10",
            "2026-03-20"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Payment due date.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:due_date"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "approved_by",
          "inferred_type": "integer_nullable",
          "sample_values": [
            1004
          ],
          "null_observation": "Blank observed for REQUESTED, HELD without approval, and CANCELLED rows.",
          "candidate_attribute": "Approving user identifier; candidate nullable foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:approved_by",
            "csv:pc_payment_request#row:3",
            "csv:pc_payment_request#row:4",
            "csv:pc_payment_request#row:6",
            "csv:pc_payment_request#row:8"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "approved_at",
          "inferred_type": "datetime_nullable",
          "sample_values": [
            "2026-02-25 15:00:00",
            "2026-02-26 16:20:00"
          ],
          "null_observation": "Blank observed for REQUESTED, HELD without approval, and CANCELLED rows.",
          "candidate_attribute": "Payment approval timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:approved_at",
            "csv:pc_payment_request#row:3",
            "csv:pc_payment_request#row:4",
            "csv:pc_payment_request#row:6",
            "csv:pc_payment_request#row:8"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "paid_at",
          "inferred_type": "datetime_nullable",
          "sample_values": [
            "2026-03-01 10:00:00",
            "2025-02-20 10:00:00"
          ],
          "null_observation": "Blank observed for all non-PAID rows in sample.",
          "candidate_attribute": "Payment completion timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_payment_request#column:paid_at",
            "csv:pc_payment_request#row:3",
            "csv:pc_payment_request#row:4",
            "csv:pc_payment_request#row:5",
            "csv:pc_payment_request#row:6",
            "csv:pc_payment_request#row:8",
            "csv:pc_payment_request#row:9"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "invoice_id appears to reference pc_invoice.invoice_id",
        "approved_by appears to reference pc_user.user_id when not blank",
        "payment_request_id is referenced by pc_approval_record.target_id where target_type is PAYMENT_REQUEST"
      ],
      "data_quality_notes": [
        "No duplicate payment_request_id observed in sample.",
        "Payment request 9004 has payment_status HELD with approved_by and approved_at populated while approval record 5014 is REJECTED; status/approval semantics need validation.",
        "Non-PAID rows have blank paid_at in sample."
      ],
      "evidence_refs": [
        "csv:pc_payment_request"
      ]
    },
    {
      "file_name": "pc_approval_record.csv",
      "row_count": 14,
      "candidate_concept": "Approval Record",
      "columns": [
        {
          "column_name": "approval_id",
          "inferred_type": "integer",
          "sample_values": [
            5001,
            5002,
            5003
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approval record identifier; candidate primary key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:approval_id"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "target_type",
          "inferred_type": "enum_string",
          "sample_values": [
            "PURCHASE_REQUEST",
            "CONTRACT",
            "PAYMENT_REQUEST"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Type of object being approved.",
          "candidate_enum_values": [
            "PURCHASE_REQUEST",
            "CONTRACT",
            "PAYMENT_REQUEST"
          ],
          "evidence_refs": [
            "csv:pc_approval_record#column:target_type"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "target_id",
          "inferred_type": "integer",
          "sample_values": [
            3001,
            3002,
            6001,
            9001
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Identifier of target object; polymorphic foreign key candidate.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:target_id"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "step_name",
          "inferred_type": "enum_or_string",
          "sample_values": [
            "Department approval",
            "Finance approval",
            "Legal review",
            "Payment approval"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approval step name.",
          "candidate_enum_values": [
            "Department approval",
            "Finance approval",
            "Legal review",
            "Payment approval"
          ],
          "evidence_refs": [
            "csv:pc_approval_record#column:step_name"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "approver_user_id",
          "inferred_type": "integer",
          "sample_values": [
            1002,
            1004,
            1005
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approver user identifier; candidate foreign key.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:approver_user_id"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "approval_status",
          "inferred_type": "enum_string",
          "sample_values": [
            "APPROVED",
            "PENDING",
            "REJECTED"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approval decision/status.",
          "candidate_enum_values": [
            "APPROVED",
            "PENDING",
            "REJECTED"
          ],
          "evidence_refs": [
            "csv:pc_approval_record#column:approval_status"
          ],
          "confidence": 0.95
        },
        {
          "column_name": "approval_comment",
          "inferred_type": "string",
          "sample_values": [
            "Approved for planned laptop refresh",
            "Warehouse need confirmed"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approval comment text.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:approval_comment"
          ],
          "confidence": 0.85
        },
        {
          "column_name": "submitted_at",
          "inferred_type": "datetime",
          "sample_values": [
            "2026-02-01 09:10:00",
            "2026-02-02 10:20:00"
          ],
          "null_observation": "No nulls observed in sample.",
          "candidate_attribute": "Approval submission timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:submitted_at"
          ],
          "confidence": 0.9
        },
        {
          "column_name": "decided_at",
          "inferred_type": "datetime_nullable",
          "sample_values": [
            "2026-02-01 14:30:00",
            "2026-02-02 15:10:00"
          ],
          "null_observation": "Blank observed for PENDING approval rows.",
          "candidate_attribute": "Decision timestamp.",
          "candidate_enum_values": [],
          "evidence_refs": [
            "csv:pc_approval_record#column:decided_at",
            "csv:pc_approval_record#row:5",
            "csv:pc_approval_record#row:12"
          ],
          "confidence": 0.9
        }
      ],
      "candidate_relations": [
        "target_type plus target_id appears to form polymorphic reference to pc_purchase_request.request_id, pc_contract.contract_id, or pc_payment_request.payment_request_id",
        "approver_user_id appears to reference pc_user.user_id",
        "Multiple approval rows can share the same target_id for multi-step approval, e.g. purchase request 3002 and 3009"
      ],
      "data_quality_notes": [
        "No duplicate approval_id observed in sample.",
        "PENDING approvals have blank decided_at in sample.",
        "Payment approval record 5014 is REJECTED for target 9004 while payment request 9004 has approved_by and approved_at populated; interpretation uncertain."
      ],
      "evidence_refs": [
        "csv:pc_approval_record"
      ]
    }
  ],
  "candidate_states": [
    {
      "field": "role_code",
      "values": [
        "REQUESTER",
        "DEPT_MANAGER",
        "PROCUREMENT_SPECIALIST",
        "FINANCE_MANAGER",
        "LEGAL_REVIEWER",
        "WAREHOUSE_CLERK",
        "AP_CLERK",
        "PROCUREMENT_ADMIN"
      ],
      "evidence_refs": [
        "csv:pc_user#column:role_code"
      ]
    },
    {
      "field": "supplier_status",
      "values": [
        "ACTIVE",
        "SUSPENDED",
        "PENDING_REVIEW"
      ],
      "evidence_refs": [
        "csv:pc_supplier#column:supplier_status"
      ]
    },
    {
      "field": "risk_rating",
      "values": [
        "LOW",
        "MEDIUM",
        "HIGH"
      ],
      "evidence_refs": [
        "csv:pc_supplier#column:risk_rating"
      