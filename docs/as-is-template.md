# AS-IS Document: [Project Code - Project Name]

> **Document Purpose**: This document captures the current state of the project as it exists today. It serves as a reference point for understanding what we have before planning any migrations or changes.
>
> **Instructions**: Replace all placeholder text in [brackets] with actual project information. Remove this instruction section when finalizing the document.

---

## 1. Project Information

### Project Overview
**Project Code**: [e.g., PRJ-000]

**Project Name**: [Full project name]

**Project Description**:
[Provide a clear, simple description of what this project does. Explain its purpose in terms that a business user would understand. Avoid technical jargon.]

**Main Use Cases**:
- [Use Case 1: Describe what users do with this system]
- [Use Case 2: Describe another key functionality]
- [Use Case 3: Add more as needed]

### Project Team

**Current Project Owner**: [Name and contact information]

**Current Technical Lead**: [Name and contact information]

**Team Members**: 
[Optional: List other key team members if relevant]

---

## 2. Technical Details

### Technologies Used

List all technologies, frameworks, and tools currently in use:

| Technology | Version | Purpose |
|------------|---------|---------|
| [e.g., Python] | [e.g., 3.11] | [e.g., Primary programming language] |
| [e.g., Flask] | [e.g., 3.0.0] | [e.g., Web framework for building APIs] |
| [Add more rows] | | |

### Solution Architecture

**Architecture Overview**:
[Provide a high-level description of how the system is structured. Explain the main components and how they work together. Use simple language.]

**Architecture Diagram**:
```
[Include a simple text-based or ASCII diagram showing the main components and their connections]
[Example:
┌─────────────────┐         ┌─────────────────┐
│   Component A   │────────▶│   Component B   │
│   (Purpose)     │         │   (Purpose)     │
└─────────────────┘         └─────────────────┘
         │                           │
         └───────────┬───────────────┘
                     │
              ┌──────▼──────┐
              │  Database   │
              └─────────────┘
]
```

**Key Components**:
- **[Component 1 Name]**: [Brief description of what it does]
- **[Component 2 Name]**: [Brief description of what it does]
- [Add more components as needed]

**Deployment Information**:
- **Environment(s)**: [e.g., Development, Production]
- **Hosting Location**: [e.g., On-premises servers, specific data center]
- **Number of Instances**: [e.g., 2 servers for redundancy]

---

## 3. Dependencies

This section lists all external systems, services, and resources that the project relies on to function properly.

### Databases

| Database Name | Type | Purpose | Connection Details |
|---------------|------|---------|-------------------|
| [e.g., UserDB] | [e.g., SQL Server] | [e.g., Stores user account information] | [e.g., Server: db-server-01, Port: 1433] |
| [Add more] | | | |

### Message Queues / Event Systems

| Queue/Topic Name | System | Purpose |
|------------------|--------|---------|
| [e.g., order-queue] | [e.g., RabbitMQ] | [e.g., Processes customer orders] |
| [Add more] | | |

### External Integrations

List any third-party services or external systems the project connects to:

| Integration Name | Purpose | Type | Credentials Required |
|------------------|---------|------|---------------------|
| [e.g., Payment Gateway] | [e.g., Process customer payments] | [e.g., REST API] | [e.g., Yes - API Key] |
| [Add more] | | | |

### Other Dependencies

[List any other dependencies such as:
- Shared network drives
- File storage systems
- Authentication services (LDAP, Active Directory, etc.)
- Monitoring tools
- Logging systems]

---

## 4. Communication Matrix

This section documents all network communications between systems, including servers, ports, and protocols.

### Internal Communications

Communications between components within the project:

| Source Component | Destination Component | Protocol | Port | Direction | Purpose |
|------------------|----------------------|----------|------|-----------|---------|
| [e.g., Web API] | [e.g., Database Server] | [e.g., TCP] | [e.g., 5432] | [e.g., Outbound] | [e.g., Database queries] |
| [Add more rows] | | | | | |

### External Communications

Communications with external systems or services:

| Source | Destination | Protocol | Port | Direction | Purpose | Notes |
|--------|-------------|----------|------|-----------|---------|-------|
| [e.g., App Server] | [e.g., External API] | [e.g., HTTPS] | [e.g., 443] | [e.g., Outbound] | [e.g., Fetch customer data] | [e.g., Authentication required] |
| [Add more rows] | | | | | | |

### Firewall Requirements

[Document any firewall rules that must be configured for the application to work properly. This is important for migration planning.]

| Rule Description | Source | Destination | Port | Protocol |
|------------------|--------|-------------|------|----------|
| [e.g., Allow web traffic] | [e.g., Any] | [e.g., Web Server] | [e.g., 443] | [e.g., HTTPS] |
| [Add more rows] | | | | |

---

## 5. Additional Information

### Current Challenges or Issues
[Optional: List any known issues, limitations, or areas of concern with the current system]

### Important Notes
[Optional: Add any other relevant information that doesn't fit in the sections above]

---

**Document Version**: 1.0
**Last Updated**: [Date]
**Updated By**: [Name]
