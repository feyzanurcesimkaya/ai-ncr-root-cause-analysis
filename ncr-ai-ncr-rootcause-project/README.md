
# AI-Powered Construction NCR & Root Cause Analysis System

This repository documents the design and prototype of an **AI-assisted Non-Conformance Report (NCR) and Root Cause Analysis system** for construction sites.  
It was prepared as an internship project and is intended to be shared on GitHub as a portfolio-quality, professional artifact.

## 1. Project Overview

In ISO 9001–compliant quality management systems, every Non-Conformance Report (NCR) must be analyzed, documented, and closed with a clear root cause and corrective actions.  
On real construction sites, however, this process is often:

- Paper-based or scattered across different tools
- Weak in photo and field evidence
- Slow in closing NCRs
- Difficult to audit and track over time

This project proposes a **mobile- and web-based NCR platform** with **AI support**, **workflow automation**, and **integration with the existing Electronic Document Management System (EDMS)**.

The goal is a **field‑ready, audit‑proof, and data-driven quality management workflow**.

## 2. Problem Statement

Traditional NCR handling on construction sites typically suffers from:

- **Low data quality**  
  - Blurry or incomplete photos
  - Missing or inconsistent metadata (location, time, related document, etc.)

- **Weak root cause analysis**  
  - Root causes are written as very short, generic text
  - Past similar cases are hard to find
  - Lessons learned are not reused

- **Limited follow-up and prevention**  
  - Corrective actions are not tracked end-to-end
  - Repeating issues are detected late
  - Preventive actions are rarely measured with KPIs

This project addresses these gaps with an **AI-augmented NCR lifecycle** and structured workflows.

## 3. Objectives

- Enforce **high-quality NCR records** (photo clarity, mandatory fields, EDMS linkage)
- Support engineers with **AI-based suggestions** for defect type and root cause
- Provide **semantic search** over past cases for better learning and benchmarking
- Track **corrective and preventive actions** in a structured and auditable way
- Enable **preventive scanning and early-warning reports** for repeating issues
- Align the whole process with **ISO 9001** and internal quality procedures

## 4. System Features

### 4.1 Smart NCR Creation

- Mobile/Web NCR creation with:
  - Photo upload from the construction site
  - **Image clarity check** (e.g. Laplacian variance)
  - Automatic metadata: GPS location & timestamp
  - Link to EDMS objects (project tree, drawings, method statements)
- AI proposes an initial **NCR category / defect type** to guide the user
- Validation rules ensure all critical fields are filled before submission

### 4.2 Root Cause Analysis & Approval

- Semantic search to list **similar historical NCRs** based on description and tags
- Rule-based suggestions for possible root causes and checks
- Mandatory **human-written root cause explanation (min. 200 characters)** to ensure real analysis, not just one-line text
- Workflow for **review and approval** by responsible engineers / quality managers

### 4.3 Corrective & Preventive Actions (CAPA)

- Structured registration of **corrective** and **preventive** actions
- Link to EDMS tasks and documents for full traceability
- Automatic reminders and deadlines
- Verification of effectiveness before NCR closure

### 4.4 Preventive Scanner & Reporting

- Early detection of repeating patterns (e.g. similar NCRs in the same area)
- Mandatory feedback loops from site teams
- One-click **management and audit reports** (PDF/Excel)
- Full traceability in the EDMS / DMS environment

## 5. High-Level Architecture

```text
+---------------------+        +---------------------+
|  Mobile / Web App   | <----> |    API Gateway      |
| - NCR creation      |        | - AuthN/AuthZ       |
| - Photo upload      |        | - Routing           |
+---------------------+        +---------------------+
                                       |
                                       v
      +--------------------------------+------------------------------+
      |                               Backend                         |
      |  - NCR service (CRUD, workflow)                               |
      |  - CAPA service                                                |
      |  - Reporting and KPI service                                  |
      +--------------------------------+------------------------------+
                                       |
            +--------------------------+--------------------------+
            |                                                     |
            v                                                     v
+-------------------------+                         +-------------------------+
|   AI & Analytics Layer  |                         |    EDMS / DMS System    |
| - Image clarity check   |                         | - Project tree          |
| - Defect detection      |                         | - NCR documents         |
| - Semantic search       |                         | - Version control       |
| - Rule engine           |                         | - Audit trail           |
+-------------------------+                         +-------------------------+

```

### 5.1 Client

- Mobile / web application for:
  - Capturing photos and metadata
  - Creating and updating NCRs
  - Viewing tasks, deadlines, and reports

### 5.2 AI Preprocessing & Analysis

- **OpenCV-based** image clarity and edge analysis
- **CNN-based** defect detection (e.g. cracks, surface issues) – optional / future work
- **Semantic search** with TF‑IDF / embeddings to find similar past NCRs
- **Rule engine** for company-specific quality rules (when additional tests are required, mandatory checks, etc.)

### 5.3 Integration with EDMS / DMS

- Reuse existing **project hierarchy and permissions**
- Store NCR documents and reports as part of the EDMS
- Ensure version control and auditability

### 5.4 Security & Compliance

- Transport security via **TLS**
- Authentication via **OAuth2 / SAML**
- Authorization via **role-based access control (RBAC)**
- Immutable audit logs (e.g. blockchain-backed log store) for critical events

## 6. Implementation Roadmap

The original internship work proposes a phased rollout:

1. **Core Module (≈ 4 weeks)**
   - NCR creation, photo upload, clarity check
   - EDMS integration (basic)
   - Basic NCR list and filters

2. **AI Root Cause & Mandatory Fields (≈ 3 weeks)**
   - AI pre-analysis and semantic search for similar cases
   - Rule-based suggestions
   - Enforcing minimum length for root cause text

3. **Preventive Scanner & Gamification (≈ 2 weeks)**
   - Early-warning dashboards for repeating NCR types
   - Simple point system to encourage proactive reporting

4. **Pilot Deployment (≈ 3 weeks)**
   - Pilot on a selected project
   - Collect feedback, tune thresholds, validate ROI

5. **Rollout & Audit Preparation (≈ 8 weeks)**
   - Extend to more sites
   - Prepare documentation and demo scenarios for ISO audits
   - Training and change management

## 7. KPIs and Expected Benefits

Key metrics to track:

- NCR **closure time** (average days to close)
- **Repeat rate** of similar NCRs after preventive actions
- Number of **photos and attachments** per NCR
- User satisfaction surveys (engineers, QA/QC, management)
- Estimated **ROI**: cost of defects and rework avoided vs. investment

Expected benefits:

- Faster, more consistent root cause analysis
- Stronger evidence and traceability for audits
- Better learning from past NCRs through semantic search
- More proactive, less reactive quality management

## 8. Repository Structure

```text
.
├── README.md              # High-level project overview
└── docs
    ├── SYSTEM_DESIGN.md   # Detailed system design & modules
    └── ROADMAP.md         # Phased implementation plan & KPIs
```

> Note: At this stage, the repository focuses on **design and architecture**.  
> You can later add actual source code (backend, mobile app, AI models) under `src/`.
