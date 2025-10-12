# Issue Templates Guide

This directory contains issue templates to help architects and team members request project analyses and migration documentation.

## Available Templates

### 🔍 Request New Project Analysis (As-Is Document)
**File:** `01-new-project-analysis.yml`

Use this template to request a comprehensive analysis of a project. This generates an **As-Is document** that captures the current state including:
- Project information (owner, tech lead, description)
- Technical details (technologies, versions, architecture)
- Dependencies (databases, queues, external integrations)
- Communication matrix (servers, ports, connections)

**When to use:** When starting analysis of a new project for potential migration.

**Project Code Format:** XXX-NNN (e.g., PRJ-000, ABC-123)

---

### 🎯 Request To-Be Document Generation
**File:** `02-to-be-document.yml`

Use this template to request a **To-Be document** outlining the desired future state after migration to GitHub and Azure Cloud:
- Target Azure architecture
- Proposed technology stack
- Migration strategy and phases
- Risk assessment and mitigation
- Effort estimation and timeline

**When to use:** After an As-Is document exists, when planning the migration approach.

**Prerequisites:** As-Is document should typically exist first.

---

### 💡 Migration Strategy Question
**File:** `03-migration-strategy-question.yml`

Use this template to ask questions or request guidance on:
- Migration approaches and strategies
- Azure service selection
- GitHub setup and configuration
- CI/CD and DevOps practices
- Security, compliance, and cost optimization

**When to use:** When you need clarification or guidance on migration topics.

---

### 📝 Update Existing Document
**File:** `04-update-document.yml`

Use this template to request updates to existing documentation:
- Updating As-Is documents due to project changes
- Revising To-Be documents based on new requirements
- Adding missing information
- Correcting inaccuracies

**When to use:** When existing documentation needs to be updated or corrected.

---

## How to Use These Templates

1. **Go to the Issues tab** in the GitHub repository
2. **Click "New Issue"**
3. **Select the appropriate template** from the list
4. **Fill in all required fields** (marked with red asterisk *)
5. **Provide as much detail as possible** - this helps the AI Copilot agent to complete the task without additional questions
6. **Submit the issue**

## Template Structure

Each template is designed to collect:

### Clear Problem Description
- What needs to be analyzed or documented
- The project code and relevant identifiers
- Current state and context

### Clear Acceptance Criteria
- What the completed document should include
- Format and structure requirements
- Quality standards

### Hints, Tips, and Suggested Solutions
- Guidance for the AI agent on where to find information
- Steps to complete the task
- Document structure to follow

### Limitations and Context
- Known constraints or requirements
- Priority and timeline
- Additional relevant information

## For AI Copilot Agents

Each template includes a dedicated section at the bottom with:
- **Task description** - What needs to be done
- **Steps** - Detailed workflow to follow
- **Acceptance criteria** - Checklist for completion
- **Guidelines** - Standards and best practices to follow

Templates are designed so Copilot agents can be assigned without additional explanation.

## Project Code Format

All project codes follow the format: **XXX-NNN**
- 3 uppercase letters, dash, 3 numbers
- Examples: `PRJ-000`, `ABC-123`, `DEV-456`

## Document Locations

Generated documents are stored in:
- **As-Is documents:** `docs/<project-code>-as-is.md`
- **To-Be documents:** `docs/<project-code>-to-be.md`

## Related Documentation

- [Document Generation Guide](../../docs/how-to-document.md) - Structure and format for As-Is documents
- [MCP Folder README](../../mcp/README.md) - How project information is organized
- [Project Repository Structure](../../mcp/bitbucket/) - Example project structures

## Contributing

When creating new templates:
1. Follow the YAML schema for GitHub issue forms
2. Include clear descriptions and help text
3. Mark required fields appropriately
4. Provide examples and placeholders
5. Add validation where appropriate
6. Include AI agent instructions at the bottom
7. Test the template by creating a test issue

## Support

- For questions about using these templates, create an issue using the "Migration Strategy Question" template
- For template improvements, submit a pull request with proposed changes
- Review the [documentation guide](../../docs/how-to-document.md) for more information on document structure
