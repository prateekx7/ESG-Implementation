## Overview

The assignment required researching realistic enterprise data sources and modeling ingestion workflows based on real-world operational patterns.

The implementation intentionally focused on realistic data shapes rather than toy examples.

---

# 1. SAP Fuel and Procurement Data

## Research Summary

Reviewed:
- SAP export formats
- enterprise ERP reporting workflows
- flat-file operational exports
- common SAP terminology and field naming conventions

Observed characteristics:
- inconsistent units
- plant/location codes
- multilingual column headers
- non-standard date formats
- operational rather than analytics-friendly structure

---

## Chosen Format

CSV flat-file export modeled after SAP operational exports.

Example characteristics included:
- German column names
- plant identifiers
- inconsistent activity values
- unit inconsistencies

---

## Why This Format Was Chosen

Although SAP supports:
- IDocs
- OData
- BAPIs

a flat-file export was chosen because:
- it is operationally common
- realistic for analyst workflows
- achievable within prototype scope
- still demonstrates ingestion normalization challenges

---

## What Would Break in Production

Real deployments would additionally require:
- authentication
- connector reliability
- ERP schema variation handling
- enterprise mapping tables
- unit conversion libraries
- retry workflows

---

# 2. Utility Electricity Data

## Research Summary

Reviewed:
- utility portal export workflows
- common electricity billing fields
- facilities management operational workflows

Observed characteristics:
- billing periods not aligned to calendar months
- tariff structures
- meter identifiers
- varying units and reporting conventions

---

## Chosen Format

CSV export modeled after utility portal downloads.

Included:
- billing periods
- tariff types
- meter IDs
- electricity consumption values

---

## Why This Format Was Chosen

Utility portal exports are operationally common and easier to validate manually than OCR-extracted PDF data.

PDF OCR workflows were intentionally excluded from the prototype scope.

---

## What Would Break in Production

Production systems would require:
- OCR handling
- utility-specific parsers
- billing reconciliation
- duplicate detection
- meter hierarchy management

---

# 3. Corporate Travel Data

## Research Summary

Reviewed:
- Concur-style travel exports
- Navan operational workflows
- travel activity categorization

Observed characteristics:
- partial trip information
- airport/location codes
- varying transport categories
- inconsistent distance availability

---

## Chosen Format

CSV export modeled after corporate travel platform exports.

Included:
- flight routes
- employee identifiers
- transport categories
- distance-based activity data

---

## Why This Format Was Chosen

Travel exports commonly arrive as:
- CSV reports
- finance exports
- operational spreadsheets

The prototype focused on category-based normalization rather than complete travel emissions modeling.

---

## What Would Break in Production

Production systems would require:
- airport distance lookups
- hotel emissions methodologies
- supplier-specific factors
- travel policy integration
- duplicate trip reconciliation

---

# General Research Approach

The implementation intentionally modeled:
- imperfect enterprise operational data
- incomplete records
- inconsistent values
- suspicious activity values
- heterogeneous source structures

rather than idealized toy datasets.

This better reflects real ESG data ingestion challenges.