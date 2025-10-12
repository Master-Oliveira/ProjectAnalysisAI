# Document generation instructions
- All documents are generated in Markdown format to be added to a Confluence documentation portal

# As-Is documents
The As-Is document contains information about the current state of a project 
It includes the following sections
1. Project informations
- current project owner 
- current tech lead
- projetc description with purpose and main use cases
2. Technical detail
- Technologies user with versions
- Solution architecture
3. Dependencies
- list of dependencies, like databases, kafka server and queues, external integrations
4. Communication matrix
- Matrix with source and destination servers, ports and any additional information relative to a current communication need

## Using the AS-IS Template

To create a new AS-IS document:
1. Copy the template file: `as-is-template.md`
2. Replace all placeholder text in [brackets] with actual project information
3. Follow the example document `as-is-prj-000-example.md` for reference
4. Use simple, non-technical language suitable for business audiences
5. Save the document with naming convention: `as-is-[project-code].md`
