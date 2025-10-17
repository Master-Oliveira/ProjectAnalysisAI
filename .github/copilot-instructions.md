### Project Overview
Este proyecto está diseñado para analizar repositorios de software, específicamente repositorios de Bitbucket, con el fin de extraer y gestionar datos de configuración. Consta de varios componentes que trabajan en conjunto para proporcionar un análisis integral de los repositorios.

El objetivo es generar 2 tipos de documentos:
1. Un documento "As-Is" que captura el estado actual del repositorio.
2. Un documento "To-Be" que describe el estado futuro deseado del repositorio con los cambios propuestos para permitir la migración a GitHub y Azure Cloud.

## Document generation
Para obtener instrucciones detalladas sobre la configuración y la generación de documentación, consulta la [Guía de Documentación.](../docs/how-to-document.md).

### User Interaction

Ten en cuenta lo siguiente al comunicarte con los lectores del documento:

- Los lectores no son técnicos. Explica en términos simples tanto como sea posible y evita jerga técnica.


## Folder structure

- La carpeta mcp contiene toda la información sobre las aplicaciones.
- La carpeta mcp/bitbucket contiene todos los archivos de las aplicaciones que se utilizan al analizar repositorios de Bitbucket.
- La carpeta mcp/config-manager contiene todos los archivos de configuración de las aplicaciones para referencias cruzadas cuando sea necesario.
- Cada aplicación tiene una carpeta raíz con subcarpetas para diferentes componentes.
- Cada subcarpeta dentro de la aplicación es un componente de la aplicación y contiene archivos y recursos relacionados de ese componente.
- La carpeta docs contiene todos los archivos de documentación.


### Security considerations

- El proyecto puede manejar datos sensibles y confidenciales, por lo que la privacidad y la seguridad son importantes.
- No proporciones ejemplos que animen al usuario a codificar directamente secretos, contraseñas u otra información sensible.
- Si se requieren credenciales u otra información sensible, agrega funciones al programa para solicitarlas, almacenarlas localmente y cerrar sesión. Por ejemplo, un cuadro de diálogo de inicio de sesión.

### Steps to generate a document
1. Identifica el repositorio a analizar en la carpeta mcp/bitbucket. Esta carpeta contiene todos los repositorios de Bitbucket a analizar, agrupados por nombre de aplicación.
2. Crea una copia de la plantilla del documento "As-Is" en la carpeta docs.
3. Rellena la información relevante sobre el estado actual del repositorio.
