# Issue Template Examples

This document provides example use cases for each issue template to help you understand when and how to use them.

## Example 1: New Project Analysis Request

**Scenario:** You're an architect who needs to analyze a legacy microservices project called "Order Processing System" (code: OPS-001) currently hosted on Bitbucket. The project uses Java Spring Boot and connects to Oracle database and RabbitMQ.

**Template to use:** 🔍 Request New Project Analysis (As-Is Document)

**How to fill it out:**
- **Project Code:** OPS-001
- **Project Name:** Order Processing System
- **Current Repository Location:** Bitbucket
- **Repository URL:** https://bitbucket.org/company/order-processing
- **Project Owner:** John Smith (john.smith@company.com)
- **Tech Lead:** Sarah Johnson (sarah.j@company.com)
- **Project Description:** Handles order processing workflow including validation, inventory checks, payment processing, and fulfillment coordination. Main use cases: new order creation, order status updates, refund processing.
- **Known Technologies:** Java 11, Spring Boot 2.7, Oracle DB 19c, RabbitMQ 3.9
- **Known Dependencies:** 
  - Oracle Database (server: db-prod-01:1521)
  - RabbitMQ (server: mq-prod-01:5672, queues: orders, notifications)
  - Payment Gateway API (external)
- **Priority:** High - Needed soon for migration planning
- **Migration Target Timeline:** Within 3 months
- **Additional Context:** Project has ~50K lines of code, processes 10K orders/day, critical business system

**Expected Outcome:** A comprehensive As-Is document at `docs/OPS-001-as-is.md` with current architecture, dependencies, and communication flows.

---

## Example 2: To-Be Document Request

**Scenario:** After reviewing the As-Is document for OPS-001, you want to plan the migration to Azure with a preference for containerization and serverless where appropriate.

**Template to use:** 🎯 Request To-Be Document Generation

**How to fill it out:**
- **Project Code:** OPS-001
- **Project Name:** Order Processing System
- **As-Is Document Reference:** docs/OPS-001-as-is.md
- **Preferred Migration Approach:** Replatform - Optimize for cloud without full rewrite
- **Target Azure Services:** (select multiple)
  - Azure Kubernetes Service (AKS)
  - Azure SQL Database
  - Azure Service Bus
  - Azure Key Vault
  - Azure Application Insights
- **GitHub Features Needed:**
  - GitHub Actions (CI/CD)
  - GitHub Security (Dependabot, Code Scanning)
  - Branch Protection Rules
- **Migration Constraints:**
  - Must maintain backward compatibility with existing APIs
  - Zero downtime migration required
  - Must complete within 3 months
  - Budget: $50K for migration effort
- **Success Criteria:**
  - Same or better performance (< 200ms response time)
  - 99.9% uptime SLA
  - Automated deployments within 30 minutes
  - Reduced operational costs by 30%
- **Target Migration Timeline:** Within 3 months
- **Risk Tolerance:** Medium - Balance between innovation and stability
- **Current Pain Points:**
  - Manual deployments take 4+ hours
  - Limited monitoring and alerting
  - Database scaling challenges during peak times
  - Difficult to roll back failed deployments

**Expected Outcome:** A detailed To-Be document at `docs/OPS-001-to-be.md` with Azure architecture, migration phases, risk assessment, and timeline.

---

## Example 3: Migration Strategy Question

**Scenario:** You're unsure whether to use Azure SQL Database or keep using containers with PostgreSQL for your project.

**Template to use:** 💡 Migration Strategy Question

**How to fill it out:**
- **Question Category:** Azure Services Selection
- **Related Project Code:** OPS-001 (optional)
- **Your Question:** Should I migrate from Oracle to Azure SQL Database or use PostgreSQL in containers on AKS for better cost control?
- **Current Situation:**
  - Using Oracle 19c (expensive licensing)
  - 500GB database size
  - OLTP workload with ~1000 transactions/second
  - Need ACID compliance
  - Team has PostgreSQL experience
- **Desired Outcome:**
  - Reduce database licensing costs
  - Maintain or improve performance
  - Flexibility to scale
  - Minimize migration effort
- **Urgency:** Medium - Needed for upcoming work
- **Research Done:** (check all that apply)
  - Searched existing documentation
  - Reviewed Azure documentation
  - Consulted with team members

**Expected Outcome:** Detailed comparison of options with pros/cons, cost analysis, migration effort, and recommendation.

---

## Example 4: Document Update Request

**Scenario:** The OPS-001 project recently added a new integration with a shipping provider API, and the As-Is document needs to be updated.

**Template to use:** 📝 Update Existing Document

**How to fill it out:**
- **Project Code:** OPS-001
- **Document Type:** As-Is Document
- **Document Location:** docs/OPS-001-as-is.md
- **Reason for Update:** Project changes (new features, architecture changes)
- **Changes Needed:**
  - Add new dependency: ShipFast API integration
  - Update communication matrix with new API endpoint
  - Add authentication details (API key via Azure Key Vault)
  - Update architecture diagram to show new integration
- **Current Content:** (copy relevant section)
  ```
  Dependencies:
  - Oracle Database (server: db-prod-01:1521)
  - RabbitMQ (server: mq-prod-01:5672)
  - Payment Gateway API (https://api.payments.com)
  ```
- **Desired Content:**
  ```
  Dependencies:
  - Oracle Database (server: db-prod-01:1521)
  - RabbitMQ (server: mq-prod-01:5672)
  - Payment Gateway API (https://api.payments.com)
  - ShipFast Shipping API (https://api.shipfast.com/v2)
    - Authentication: API Key (stored in Azure Key Vault)
    - Used for: Real-time shipping quotes and label generation
  ```
- **Priority:** Medium - Important for accuracy
- **Context:** Integration went live last week, need documentation updated before migration planning continues
- **Verification:** (check all)
  - ✓ I have reviewed the current document
  - ✓ I have provided specific details about the needed changes
  - ✓ I have indicated which sections need updates

**Expected Outcome:** Updated As-Is document with new integration properly documented.

---

## Tips for Success

### General Best Practices
1. **Be Specific:** The more detail you provide, the better the outcome
2. **Use Standard Format:** Always use XXX-NNN format for project codes
3. **Check Existing Issues:** Search for similar issues before creating new ones
4. **Provide Context:** Explain why the analysis/question is important
5. **Set Realistic Timelines:** Be honest about urgency and deadlines

### For Project Analysis Requests
- Include links to any existing documentation
- List all known dependencies, even if uncertain
- Provide access credentials locations (don't include actual credentials!)
- Mention any special considerations or constraints

### For Questions
- Show what you've already researched
- Include specific scenarios or examples
- Ask one focused question rather than multiple unrelated questions
- Provide context about your project's unique requirements

### For Document Updates
- Reference specific sections that need changes
- Provide both current and desired content when possible
- Explain why the update is needed
- Indicate urgency relative to other work

---

## Common Scenarios

### Scenario A: Starting a New Migration
1. Create issue with "New Project Analysis" template → Get As-Is document
2. Create issue with "To-Be Document" template → Get migration plan
3. Use "Migration Strategy Question" for specific technical decisions
4. Use "Update Document" as project evolves

### Scenario B: Quick Question
1. Use "Migration Strategy Question" template directly
2. Provide context about your situation
3. Get expert guidance without full analysis

### Scenario C: Maintaining Documentation
1. Use "Update Document" template when project changes
2. Keep As-Is and To-Be documents synchronized
3. Document new integrations and dependencies promptly

### Scenario D: Multiple Projects
1. Create separate issues for each project code
2. Use labels to filter and organize
3. Reference related projects in "Additional Context" fields
4. Cross-reference documents when projects have dependencies

---

## Getting Help

If you're unsure which template to use:
- **New project, need documentation** → New Project Analysis
- **Planning migration strategy** → To-Be Document  
- **Have a question** → Migration Strategy Question
- **Need to update docs** → Update Existing Document
- **Something else** → Create a blank issue or use Migration Strategy Question

For more information:
- [Issue Templates Guide](README.md)
- [Documentation Guide](../../docs/how-to-document.md)
- [GitHub Discussions](https://github.com/Master-Oliveira/ProjectAnalysisAI/discussions)
