## Overview

The application is designed as a multi-tenant ESG ingestion and review platform that accepts emissions-related activity data from multiple enterprise systems, normalizes the data into a consistent emissions model, and supports analyst review and auditability before records are finalized.

The core design goal was to separate raw imported data from normalized emissions records so that:
- original source fidelity is preserved
- transformations are traceable
- audit workflows are possible
- suspicious records can be reviewed before approval

---

# Core Data Model

## Organization

Represents a tenant/customer using the platform.

Fields:
- id
- name
- industry
- created_at

Purpose:
- Supports multi-tenancy
- Separates emissions data between enterprises
- Enables future organization-specific emission factors or workflows

---

## DataSource

Represents a single ingestion event or uploaded dataset.

Fields:
- organization
- source_type
- original_filename
- uploaded_by
- uploaded_at

Supported source types:
- SAP
- Utility
- Corporate Travel

Purpose:
- Tracks provenance of uploaded data
- Preserves source-of-truth metadata
- Enables audit traceability to ingestion events

---

## RawRecord

Stores the original imported row exactly as received.

Fields:
- data_source
- raw_data (JSON)
- status
- error_message
- created_at

Statuses:
- pending
- processed
- suspicious
- failed

Purpose:
- Preserve original source fidelity
- Allow debugging of ingestion issues
- Support future parser improvements
- Maintain auditability of imported records

The raw imported structure is intentionally stored separately from normalized emissions data.

---

## EmissionRecord

Represents normalized and reviewable ESG activity data.

Fields:
- organization
- data_source
- scope
- category
- activity_value
- original_unit
- normalized_unit
- co2e_emissions
- review_status
- suspicious
- approved_by
- approved_at

Scopes:
- Scope 1
- Scope 2
- Scope 3

Purpose:
- Centralized normalized emissions model
- Consistent structure across heterogeneous sources
- Supports analyst review workflow
- Enables future emissions calculations and reporting

---

## AuditLog

Tracks modifications and analyst actions on emission records.

Fields:
- emission_record
- action
- old_data
- new_data
- changed_by
- timestamp

Tracked actions:
- created
- updated
- approved
- rejected

Purpose:
- Preserve audit trail
- Support external audit workflows
- Record review decisions and data changes

---

# Normalization Strategy

The ingestion layer converts source-specific data into a normalized emissions structure.

Examples:
- Fuel volumes normalized into standard units
- Electricity consumption normalized into kWh
- Travel activity normalized into distance-based calculations

Emission factors are currently prototype-level static mappings for demonstration purposes.

---

# Review Workflow

The platform intentionally introduces a review stage before records are finalized.

Workflow:
1. Source uploaded
2. Raw rows stored
3. Rows normalized
4. Suspicious rows flagged
5. Analyst reviews records
6. Records approved/rejected
7. Audit log generated

This mirrors realistic ESG operational workflows where analyst validation is required before auditor sign-off.

---

# Suspicious Record Detection

Prototype validation rules flag records as suspicious if:
- activity values are negative
- activity values exceed expected thresholds
- units are invalid or inconsistent

The goal is not automated anomaly detection, but surfacing potentially incorrect enterprise data for analyst review.

---

# Why Separate Raw and Normalized Data

This was the most important architectural decision in the project.

Reasons:
- Imported enterprise data is often inconsistent and incomplete
- Analysts may need to reference original uploaded values
- Audit workflows require preservation of source records
- Future parsers and normalization logic may evolve
- Raw data should remain immutable while normalized data can be reviewed and corrected

This separation improves auditability, traceability, and operational safety.