## Overview

This document captures the major ambiguities and engineering decisions made during implementation.

The assignment intentionally leaves many architectural and operational details unspecified. The goal of this prototype was to make realistic and defensible choices while keeping the implementation small enough to complete within the assignment timeframe.

---

# Backend Framework

## Decision
Used Django REST Framework.

## Why
- Strong admin tooling
- Rapid API development
- Mature ORM
- Good fit for structured enterprise workflows
- Easy audit/admin visibility during development

---

# Frontend Framework

## Decision
Used Next.js with App Router.

## Why
- Fast frontend development
- Simple deployment on Vercel
- Clean routing structure
- Good developer ergonomics

---

# Database

## Decision
Used PostgreSQL.

## Why
- Better production realism than SQLite
- Strong JSON support for raw ingestion records
- Better alignment with enterprise SaaS architectures

---

# SAP Ingestion Format

## Decision
Handled flat-file CSV exports modeled after SAP exports.

## Why
Real SAP integrations involve:
- IDocs
- BAPIs
- OData services
- proprietary enterprise middleware

For a 4-day prototype, flat-file exports were the most realistic subset to implement while still representing real operational workflows.

The sample data intentionally includes:
- German column names
- plant codes
- inconsistent values
- unit inconsistencies

---

# Utility Data Ingestion

## Decision
Handled CSV exports from utility portals.

## Why
Many facilities teams still retrieve utility data through:
- portal exports
- emailed spreadsheets
- manually maintained reports

PDF OCR ingestion was intentionally excluded because:
- OCR pipelines would dominate implementation scope
- parsing utility bill layouts is highly utility-specific

---

# Travel Data Ingestion

## Decision
Modeled CSV exports after platforms like Concur or Navan.

## Why
Travel systems commonly expose:
- flight routes
- hotel bookings
- transport categories
- partial distance information

The prototype simplified emissions calculations to distance-based assumptions.

---

# Review Workflow

## Decision
Introduced explicit analyst approval before records are finalized.

## Why
ESG reporting workflows usually require:
- analyst review
- finance validation
- audit sign-off

The review queue was prioritized over advanced ingestion complexity.

---

# Suspicious Record Handling

## Decision
Flagged:
- negative activity values
- extremely large activity values

## Why
Enterprise operational data is frequently incomplete or incorrect.

The goal was not machine learning anomaly detection, but surfacing potentially invalid rows for human review.

---

# Authentication

## Decision
Used simplified prototype authentication.

## Why
The assignment emphasized:
- ingestion
- normalization
- review workflows
- auditability

rather than production-grade identity management.

---

# Deployment

## Decision
Used:
- Render for backend
- Vercel for frontend
- Neon for PostgreSQL

## Why
- Free-tier friendly
- Fast setup
- Easy GitHub integration
- Realistic cloud deployment workflow

---

# Scope Limitation Strategy

The implementation intentionally prioritized:
- auditability
- data modeling
- review workflows
- realistic ingestion shapes

over:
- advanced integrations
- enterprise scalability
- infrastructure complexity

This was done to keep the implementation understandable and defensible within the assignment timeframe.