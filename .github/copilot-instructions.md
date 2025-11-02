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

- La información sobre las aplicaciones esta en la carpeta mcp y en el servidor de mcp de bitbucket.
- El servidor mcp de bitbucket contiene todos los archivos de las aplicaciones que se utilizan al analizar repositorios de Bitbucket (código fuente).
- Cada aplicación en bitbucket tiene múltiples proyectos con repositorios distintos para diferentes componentes.
- Cada repositorio bitbucket dentro de la aplicación es un componente de la aplicación y contiene archivos y recursos relacionados de ese componente.
- La carpeta mcp/config-manager contiene todos los archivos de configuración de los componentes para referencias cruzadas cuando sea necesario.
- La carpeta docs contiene todos los archivos de documentación.
- La documentación de una aplicación deberá contener la información de todos los repositorios que componen la aplicación.


### Security considerations

- El proyecto puede manejar datos sensibles y confidenciales, por lo que la privacidad y la seguridad son importantes.
- No proporciones ejemplos que animen al usuario a codificar directamente secretos, contraseñas u otra información sensible.
- Si se requieren credenciales u otra información sensible, agrega funciones al programa para solicitarlas, almacenarlas localmente y cerrar sesión. Por ejemplo, un cuadro de diálogo de inicio de sesión.

### Steps to generate a document
1. Analiza la plantilla de documento "As-Is" en la carpeta docs para entender su estructura y la informacion necesarios.
2. Identifica los repositorios a analizar usando el servidor de mcp para bitbucket. Esta servidor contiene todos los repositorios de Bitbucket a analizar.
3. Identifica todos los componentes dentro de la aplicación que se vaya a documentar.
4. Identifica la configuración relevante en la carpeta mcp/config-manager para cada componente.
5. Utiliza los archivos de configuración de Openshift y Kubernetes en los repositorios para obtener información adicional sobre la configuración de cada componente (para rellenar la sección UBICACIÓN DE COMPONENTES del As-Is).
6. Crea una copia de la plantilla del documento "As-Is" en la carpeta docs.
7. Rellena la información relevante sobre el estado actual de la aplicación.
