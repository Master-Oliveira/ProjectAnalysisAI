### Project Overview
This project is designed to analyze software repositories, specifically Bitbucket repositories, to extract and manage configuration data. It consists of several components that work together to provide a comprehensive analysis of the repositories.

The objective is to generate 2 types of documents:
1. A "As-Is" document that captures the current state of the repository.
2. A "To-Be" document that outlines the desired future state of the repository with proposed changes to allow migration to Git-Hub and Azure Cloud.

## Document generation
For detailed setup and documentation generation instructions, please refer to our [Documentation Guide](../docs/how-to-document.md).

### User Interaction

Consider the following when communicating with the document readers.

- The readers are not technical. Explain in simple terms as much as possible and avoid software jargon.


## Folder structure

- The project has a root folder with subfolders for different components.
- Each subfolder contains related files and resources.
- The folder mcp contains all the information about the projects.
- The folder mcp/bitbucket contains all the projects files to use when analyzing Bitbucket repositories.
- The folder mcp/config-manager contains all the projects configuration files to cross-reference when needed.
- The folder docs contains all the documentation files.


### Security considerations

- Personal information might be processed so privacy and security are important.
- Do not provide examples that encourage the user to hardcode secrets, passwords, or other sensitive information.
- If credentials or other sensitive information is required, add features to the program to prompt for it, store it locally, and logout. For example a login dialog box.

### Steps to generate a document
1. Identify the repository to analyze from the mcp/bitbucket folder. This folder contains all the Bitbucket repositories to analyze grouped by project name.
2. Create a copy of the "As-Is" document template in the docs folder.
3. Fill in the relevant information about the current state of the repository.
4. 
