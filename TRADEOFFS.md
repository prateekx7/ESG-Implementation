## Overview

This prototype intentionally excluded several production-grade features in order to prioritize:
- realistic ingestion workflows
- auditability
- clean data modeling
- analyst review workflows

The goal was depth in core architecture rather than breadth of features.

---

# 1. No Real SAP/API Integrations

## Not Built
Direct SAP integrations through:
- BAPIs
- OData
- IDocs
- middleware connectors

## Why
Real SAP integrations require:
- enterprise credentials
- ERP access
- middleware configuration
- complex transformation logic

Instead, the prototype focused on realistic exported data shapes using flat-file CSV ingestion.

---

# 2. No OCR Pipeline for Utility Bills

## Not Built
PDF ingestion and OCR extraction for utility bills.

## Why
Production OCR systems require:
- document classification
- vendor-specific templates
- extraction validation
- retry workflows

This would dominate the implementation scope and distract from the ingestion/review architecture.

The prototype instead handled utility portal CSV exports, which are also common operational workflows.

---

# 3. No Advanced Emissions Engine

## Not Built
A production-grade emissions calculation engine.

## Why
Real ESG calculation systems involve:
- region-specific emission factors
- temporal factor changes
- supplier-specific calculations
- standards alignment
- regulatory methodologies

The prototype intentionally used simplified static emission factors to focus on ingestion architecture and review workflows.

---

# Additional Simplifications

Additional intentionally simplified areas:
- authentication and RBAC
- async ingestion queues
- background workers
- file storage systems
- anomaly detection models
- multi-region deployment
- real-time collaboration

These were excluded to keep the implementation focused, explainable, and achievable within the assignment timeframe.

---

# Why These Tradeoffs Were Acceptable

The assignment emphasized:
- engineering judgment
- architecture quality
- realistic operational modeling
- defensible implementation decisions

The prototype therefore prioritized:
- auditability
- traceability
- normalized data modeling
- review workflows
- realistic enterprise data handling

over infrastructure complexity or feature volume.