# Instrucciones para la generación de documentos
- Todos los documentos se generan en formato Markdown para ser añadidos a un portal de documentación en Confluence.

# Documentos As-Is
El documento As-Is contiene información sobre el estado actual de un proyecto.
Incluye las siguientes secciones:
1. Información del proyecto
- Descripción del proyecto con su propósito y principales casos de uso
2. Detalles técnicos
- Tecnologías utilizadas con sus versiones
- Arquitectura de la solución
3. Dependencias
- Lista de dependencias, como bases de datos, servidores y colas de Kafka, integraciones externas
4. Matriz de comunicaciones
- Matriz con servidores de origen y destino, puertos y cualquier información adicional relacionada con una necesidad de comunicación actual

## Uso de la plantilla AS-IS

Para crear un nuevo documento AS-IS:

1. Copia el archivo de plantilla: as-is-template.md
2. Reemplaza todo el texto entre [corchetes] con la información real del proyecto
3. Usa un lenguaje simple y no técnico, adecuado para audiencias de negocio
4. Guarda el documento con la convención de nombres: as-is-[código-del-proyecto].md