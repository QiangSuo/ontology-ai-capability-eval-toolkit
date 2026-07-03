-- Generic Procurement Contract MVP schema
-- Fictional input dataset. PostgreSQL-style DDL for ontology extraction tests.

CREATE TABLE pc_department (
    department_id BIGINT PRIMARY KEY,
    department_code VARCHAR(30) NOT NULL UNIQUE,
    department_name VARCHAR(120) NOT NULL,
    cost_center VARCHAR(30) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE pc_user (
    user_id BIGINT PRIMARY KEY,
    user_name VARCHAR(120) NOT NULL,
    role_code VARCHAR(40) NOT NULL,
    department_id BIGINT NOT NULL REFERENCES pc_department(department_id),
    email VARCHAR(160) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL,
    CHECK (role_code IN ('REQUESTER','DEPT_MANAGER','PROCUREMENT_SPECIALIST','FINANCE_MANAGER','LEGAL_REVIEWER','WAREHOUSE_CLERK','AP_CLERK','PROCUREMENT_ADMIN'))
);

CREATE TABLE pc_supplier (
    supplier_id BIGINT PRIMARY KEY,
    supplier_code VARCHAR(40) NOT NULL UNIQUE,
    supplier_name VARCHAR(160) NOT NULL,
    supplier_status VARCHAR(30) NOT NULL,
    risk_rating VARCHAR(20) NOT NULL,
    contact_email VARCHAR(160),
    onboarded_at TIMESTAMP,
    CHECK (supplier_status IN ('ACTIVE','SUSPENDED','PENDING_REVIEW')),
    CHECK (risk_rating IN ('LOW','MEDIUM','HIGH'))
);

CREATE TABLE pc_purchase_request (
    request_id BIGINT PRIMARY KEY,
    request_no VARCHAR(40) NOT NULL UNIQUE,
    request_title VARCHAR(180) NOT NULL,
    requester_user_id BIGINT NOT NULL REFERENCES pc_user(user_id),
    department_id BIGINT NOT NULL REFERENCES pc_department(department_id),
    preferred_supplier_id BIGINT REFERENCES pc_supplier(supplier_id),
    estimated_amount NUMERIC(14,2) NOT NULL,
    currency_code CHAR(3) NOT NULL DEFAULT 'CNY',
    request_status VARCHAR(30) NOT NULL,
    business_justification TEXT NOT NULL,
    required_by_date DATE,
    submitted_at TIMESTAMP,
    approved_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL,
    CHECK (estimated_amount >= 0),
    CHECK (request_status IN ('DRAFT','SUBMITTED','APPROVED','REJECTED','CANCELLED'))
);
COMMENT ON COLUMN pc_purchase_request.estimated_amount IS 'PR amount >= 50000 requires finance manager approval.';

CREATE TABLE pc_purchase_request_line (
    line_id BIGINT PRIMARY KEY,
    request_id BIGINT NOT NULL REFERENCES pc_purchase_request(request_id),
    item_description VARCHAR(220) NOT NULL,
    category_code VARCHAR(40) NOT NULL,
    quantity NUMERIC(12,2) NOT NULL,
    unit_of_measure VARCHAR(20) NOT NULL,
    estimated_unit_price NUMERIC(14,2) NOT NULL,
    line_amount NUMERIC(14,2) NOT NULL,
    CHECK (quantity > 0),
    CHECK (line_amount >= 0)
);

CREATE TABLE pc_approval_record (
    approval_id BIGINT PRIMARY KEY,
    target_type VARCHAR(40) NOT NULL,
    target_id BIGINT NOT NULL,
    step_name VARCHAR(80) NOT NULL,
    approver_user_id BIGINT NOT NULL REFERENCES pc_user(user_id),
    approval_status VARCHAR(30) NOT NULL,
    approval_comment VARCHAR(500),
    submitted_at TIMESTAMP NOT NULL,
    decided_at TIMESTAMP,
    CHECK (target_type IN ('PURCHASE_REQUEST','CONTRACT','PAYMENT_REQUEST')),
    CHECK (approval_status IN ('PENDING','APPROVED','REJECTED','SKIPPED'))
);

CREATE TABLE pc_contract (
    contract_id BIGINT PRIMARY KEY,
    contract_no VARCHAR(40) NOT NULL UNIQUE,
    request_id BIGINT NOT NULL REFERENCES pc_purchase_request(request_id),
    supplier_id BIGINT NOT NULL REFERENCES pc_supplier(supplier_id),
    contract_title VARCHAR(180) NOT NULL,
    contract_amount NUMERIC(14,2) NOT NULL,
    contract_status VARCHAR(30) NOT NULL,
    start_date DATE,
    end_date DATE,
    legal_reviewer_id BIGINT REFERENCES pc_user(user_id),
    legal_approved_at TIMESTAMP,
    activated_at TIMESTAMP,
    termination_reason VARCHAR(300),
    created_at TIMESTAMP NOT NULL,
    CHECK (contract_amount >= 0),
    CHECK (contract_status IN ('DRAFT','LEGAL_REVIEW','ACTIVE','EXPIRED','TERMINATED'))
);

CREATE TABLE pc_purchase_order (
    po_id BIGINT PRIMARY KEY,
    po_no VARCHAR(40) NOT NULL UNIQUE,
    contract_id BIGINT NOT NULL REFERENCES pc_contract(contract_id),
    request_id BIGINT NOT NULL REFERENCES pc_purchase_request(request_id),
    supplier_id BIGINT NOT NULL REFERENCES pc_supplier(supplier_id),
    po_amount NUMERIC(14,2) NOT NULL,
    po_status VARCHAR(30) NOT NULL,
    released_at TIMESTAMP,
    closed_at TIMESTAMP,
    CHECK (po_status IN ('RELEASED','PARTIALLY_RECEIVED','CLOSED','CANCELLED'))
);

CREATE TABLE pc_goods_receipt (
    receipt_id BIGINT PRIMARY KEY,
    receipt_no VARCHAR(40) NOT NULL UNIQUE,
    po_id BIGINT NOT NULL REFERENCES pc_purchase_order(po_id),
    receipt_status VARCHAR(30) NOT NULL,
    received_by BIGINT NOT NULL REFERENCES pc_user(user_id),
    received_at TIMESTAMP,
    inspection_result VARCHAR(40),
    remarks VARCHAR(500),
    CHECK (receipt_status IN ('PENDING','PARTIAL','COMPLETE','REJECTED')),
    CHECK (inspection_result IN ('PASS','FAIL','NOT_REQUIRED'))
);

CREATE TABLE pc_invoice (
    invoice_id BIGINT PRIMARY KEY,
    invoice_no VARCHAR(40) NOT NULL UNIQUE,
    supplier_id BIGINT NOT NULL REFERENCES pc_supplier(supplier_id),
    po_id BIGINT NOT NULL REFERENCES pc_purchase_order(po_id),
    receipt_id BIGINT REFERENCES pc_goods_receipt(receipt_id),
    invoice_amount NUMERIC(14,2) NOT NULL,
    invoice_date DATE NOT NULL,
    invoice_status VARCHAR(30) NOT NULL,
    match_variance_amount NUMERIC(14,2),
    matched_at TIMESTAMP,
    CHECK (invoice_amount >= 0),
    CHECK (invoice_status IN ('PENDING_MATCH','MATCHED','EXCEPTION','CANCELLED'))
);

CREATE TABLE pc_payment_request (
    payment_request_id BIGINT PRIMARY KEY,
    payment_no VARCHAR(40) NOT NULL UNIQUE,
    invoice_id BIGINT NOT NULL REFERENCES pc_invoice(invoice_id),
    payment_amount NUMERIC(14,2) NOT NULL,
    payment_status VARCHAR(30) NOT NULL,
    due_date DATE NOT NULL,
    approved_by BIGINT REFERENCES pc_user(user_id),
    approved_at TIMESTAMP,
    paid_at TIMESTAMP,
    CHECK (payment_amount >= 0),
    CHECK (payment_status IN ('REQUESTED','APPROVED','PAID','HELD','CANCELLED'))
);
