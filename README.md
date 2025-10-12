# ProjectAnalysisAI
Analyze and help define migration strategies for moving projects to GitHub and Azure Cloud.

## Quick Start

### Request a Project Analysis

To analyze a project and generate documentation for migration planning:

1. **[Create a New Issue](../../issues/new/choose)** using one of our templates:
   - 🔍 **New Project Analysis** - Generate an As-Is document for a project
   - 🎯 **To-Be Document** - Create a migration plan and target architecture
   - 💡 **Migration Strategy Question** - Get guidance on migration approaches
   - 📝 **Update Document** - Revise existing documentation

2. **Provide the project code** in format XXX-NNN (e.g., `PRJ-000`, `ABC-123`)

3. **Fill in the required details** - The more information you provide, the better the analysis

4. **Submit** - A Copilot AI agent can be assigned to complete the task

### Project Code Format

All projects are identified by a code: **3 letters - 3 numbers**
- Examples: `PRJ-000`, `ABC-123`, `MIG-001`

## Repository Structure

```
ProjectAnalysisAI/
├── .github/
│   └── ISSUE_TEMPLATE/       # Issue templates for requesting analysis
├── docs/                      # Generated documentation
│   └── how-to-document.md    # Documentation guide
├── mcp/                      # Project data for analysis
│   ├── bitbucket/            # Bitbucket project repositories
│   │   └── prj-000/          # Example project
│   └── config-manager/       # Configuration cross-references
└── README.md                 # This file
```

## Documentation

- **[Issue Templates Guide](.github/ISSUE_TEMPLATE/README.md)** - How to request analyses
- **[Document Generation Guide](docs/how-to-document.md)** - Structure of As-Is documents
- **[MCP Folder](mcp/README.md)** - How project data is organized

## Generated Documents

The analysis process generates two types of documents:

### As-Is Documents
Capture the current state of a project:
- Project information and ownership
- Technical stack and architecture
- Dependencies and integrations
- Communication matrix

### To-Be Documents
Outline the target state after migration:
- Azure Cloud architecture
- GitHub setup and workflows
- Migration strategy and phases
- Risk assessment and timeline

Both documents are written in Markdown format suitable for business audiences and Confluence portals.

## Contributing

See the [Issue Templates README](.github/ISSUE_TEMPLATE/README.md) for guidelines on using and contributing to issue templates
