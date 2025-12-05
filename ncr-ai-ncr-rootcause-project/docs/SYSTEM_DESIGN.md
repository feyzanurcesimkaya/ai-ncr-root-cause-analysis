
# System Design

This document describes the proposed technical design for the **AI-Powered Construction NCR & Root Cause Analysis System**.

## 1. Actors and Roles

- **Site Engineer / Foreman**
  - Creates NCRs from the field
  - Uploads photos and comments
  - Proposes corrective actions

- **Quality Engineer / QA-QC**
  - Reviews NCRs and root cause analysis
  - Approves or rejects NCRs and CAPA
  - Monitors KPIs on dashboards

- **Project Manager**
  - Reviews status of NCRs and critical risks
  - Approves high-impact actions
  - Uses reports for progress and risk meetings

- **ISO / Internal Auditor**
  - Checks documentation, traceability, and effectiveness
  - Samples NCRs for compliance review

## 2. Core Modules

### 2.1 NCR Management Service

Responsibilities:

- Create / update / close NCRs
- Enforce state machine (Draft → Under Review → Corrective Actions → Closed)
- Attach photos, documents, and EDMS links
- Expose REST/GraphQL APIs to the clients

Key fields:

- NCR ID, title, description
- Project, location, discipline, subcontractor
- Severity (low, medium, high)
- Status, owner, deadlines
- Root cause text and category
- Corrective & preventive actions

### 2.2 AI Assistant Service

Responsibilities:

- Receive NCR text and photos
- Run image clarity check and optional defect detection
- Generate suggestions:
  - Defect type
  - Potential root causes
  - Required tests or inspections based on rules

Implementation ideas:

- Python service with FastAPI
- OpenCV for image pre-processing
- A small CNN model or integration with a hosted vision API
- TF-IDF / embedding-based similarity search over previous NCRs
- Rule engine (e.g. simple JSON rule definitions) for domain rules

### 2.3 Semantic Search Engine

- Indexes:
  - NCR titles and descriptions
  - Root cause texts
  - CAPA descriptions and tags
- Enables:
  - "Show similar NCRs" functionality
  - Benchmarking and best-practice lookup

Possible technologies:

- Elasticsearch / OpenSearch
- PostgreSQL full-text search for smaller deployments

### 2.4 CAPA Tracking

- Each NCR can have multiple **Corrective** and **Preventive** actions
- Fields:
  - Description, responsible person, due date
  - Status (Open / In Progress / Done / Verified)
  - Links to EDMS documents and checklists
- Workflow support:
  - Email / in-app notifications
  - Escalation rules for overdue items

### 2.5 Reporting & Analytics

- Standard reports:
  - Open NCRs by status, project, subcontractor
  - Top recurring root causes
  - CAPA overdue rates
- Export formats:
  - PDF, Excel, and EDMS-friendly formats

## 3. Data Model (High Level)

```text
Project (1) ---- (N) NCR ---- (N) Photo
                  |
                  +---- (N) CAPA
                  |
                  +---- (1) RootCause
```

- **Project**
  - id, name, code, location

- **NCR**
  - id, project_id, title, description, category, severity
  - status, created_at, closed_at
  - created_by, owner_id
  - edms_object_id (link to EDMS)

- **Photo**
  - id, ncr_id, url/path
  - gps_lat, gps_lng, captured_at
  - clarity_score, ai_findings (JSON)

- **RootCause**
  - id, ncr_id
  - text (>= 200 characters)
  - category (design, material, workmanship, planning, etc.)

- **CAPA**
  - id, ncr_id
  - type (corrective / preventive)
  - description
  - responsible_id
  - due_date, completed_at
  - status
  - verification_result

## 4. Non-Functional Requirements

- **Performance**
  - Handle typical NCR volumes for a large construction project
  - Fast responses for search and listing

- **Reliability**
  - Regular backups
  - Graceful degradation if AI services are not available

- **Security & Compliance**
  - TLS everywhere
  - OAuth2 / SAML SSO integration
  - Fine-grained RBAC based on project and role
  - Immutable audit logs for critical actions

- **Scalability**
  - Microservice-friendly design
  - Containerized deployment (Docker/Kubernetes)

## 5. Prototype Scope

The internship prototype focuses on:

- Basic NCR creation and listing
- Image clarity check
- Simple semantic search (e.g. TF-IDF)
- Rule-based suggestions for root cause and checks
- Example report generation for audits

The design allows further extension to full production grade.
