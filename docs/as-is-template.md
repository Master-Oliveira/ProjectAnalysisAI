# Documento AS-IS: [Código de aplicación - Nombre de la aplicación]

> **Propósito del documento**: Este documento captura el estado actual del proyecto tal como existe hoy. Sirve como punto de referencia para comprender lo que tenemos antes de planificar cualquier migración o cambio.
>
> **Instrucciones**: Reemplaza todo el texto entre [corchetes] con la información real del proyecto. Elimina esta sección de instrucciones al finalizar el documento. No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración. Si no hubiera información suficiente de un dato, indícalo: "No hay información suficiente".

---

## 1. Descripción

### 1.1 Resumen del proyecto
**Código de proyecto**: [e.g., PRJ-000]

**Nombre del proyecto**: [Nombre de la aplicación completo]

**Descripción del proyecto**:
[Realizar una breve descripción de la aplicación basándote en la información que puedas encontrar en el código fuente, ficheros de configuración y documentación asociada al proyecto. Explica su propósito en términos que un usuario de negocio pueda entender. Evita jerga técnica. Añade una lista con las tecnologías principales utilizadas en el proyecto. Si alguna de las tecnologías está solamente referenciada pero no se utiliza en el código, indícalo como tal en la sección "Información adicional".]

### 1.2 Funcionalidades principales

[Identificar funcionalidades primarias, escenarios clave y/o casos de uso.]


### 1.3 Usuarios
[Describir a los principales usuarios que utilizarán el sistema o la solución (empleados, usuarios finales, socios, etc.). Devuelve una tabla con el siguiente formato. No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración. ]


| Usuario o sistema | Descripción del uso general que el usuario da al sistema o las interacciones importantes de este |
|------------|---------|
| [e.g., BI / Snowflake] | [e.g., Consumo analítico corporativo de datos/feeds para reporting.] |

---

## 2. Arquitectura técnica

### 2.1 Diseño de la solución

[Lista todos los componentes de la aplicación, añadiendo un resumen sobre éste.]

| Componente | Descripción | 
|------------|---------|
| Nombre o código del componente | Funcionalidad general del componente. Añade el lenguage de programación y versión, descripción, conexiones con terceros, base de datos, librerías utilizadas, si usa mensajería kafka, si expone APIs, observabilidad o testing. | 

**Diagram de arquitectura**:

[Incluye un diagrama en formato Mermaid que muestre los componentes principales y sus conexiones. Los componentes principales son cada uno de los microservicios, las bases de datos y la mensajería Kafka. Evita integraciones con monitorización. Un ejemplo de diagrama con formato mermaid:]
```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

### 2.2 Requisitos principales

[Lista de requisitos técnicos de datos para la solución:

Clasificación de datos: ¿La solución maneja datos confidenciales?
- Sensitive data: Uso Interno, Confidencial, Altamente confidencial
- Non-sensible: Uso Público (o datos sensibles que estén anonimizados)
Tiempo de datos: ¿Cuál es la vida útil de los datos para la solución?
- Temporal data: Si los datos se pudieran eliminar en poco tiempo (por ejemplo, entorno de laboratorio)
- Indefinite time: Si los datos deben conservarse durante mucho tiempo (por ejemplo, entorno preproductivo o productivo)
Protección de datos: ¿Cómo protege su aplicación o solución los datos confidenciales? ¿y cómo estás manejando los secretos (confidencialidad)?
- Los datos confidenciales se refieren a la forma en que su aplicación maneja cualquier dato que deba protegerse, ya sea en la memoria, a través de la red o en almacenes persistentes.
- La criptografía se refiere a cómo su aplicación hace cumplir la confidencialidad y la integridad.

Intenta rellenar la tabla siguiente si puedes obtener la información. Si no puedes obtener la información  indícalo: "No hay información suficiente para este requerimiento". No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración.
Añade más filas a la tabla si dispones de información suficiente, por ejemplo:
Acceso/Autenticación, Auditoría y trazabilidad, bases de datos que se utilizan.

]

</br>

**DATOS**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Clasificación de datos | Sensitive/Non-Sensitive y descripción | 
| Tiempo de datos | Temporal / Indefinidos y descripción | 
| Protección de datos | Cómo se están protegiendo los datos | 





[Seguridad:
Lista de requisitos técnicos de seguridad para la solución:

- Autenticación: requisitos sobre cómo se autenticarán los usuarios y cómo se pasarán las identidades autenticadas a través de las capas. Identificar aspectos como:
   - Fuente de autenticación: usuarios de ECI, usuarios externos (socios, empresa extendida) o ambos.
   - Proveedor de identidad (IdP): directorio corporativo, servicio de directorio de aplicaciones, servicio de directorio local, servicios B2B/B2C.
   - Tipo de credenciales: HTTPS Basic, autenticación de formulario HTTPS, Federated-SSO, autenticación multifactor, etc.
   - Protocolos de autenticación: Kerberos, OpenID, OAuth, JWT, SAML, .
   - Servicios de tokens de seguridad (STS): Azure AD/Office 365, B2C (Microsoft, Facebook, Google, etc.), STS personalizado.
- Autorización: requisitos sobre cómo la solución proporcionará controles de acceso para recursos y operaciones.
- Conectividad: Requisitos sobre Intranet y/o Internet, ESB, vNets, etc.
   - Red corporativa - Sí: conexión directa a las redes locales de Repsol (p. ej. Máquinas virtuales en Azure IaaS).
   - Red corporativa - No: no hay conexión directa con las redes locales de ECI.
   - Internet - No: solo se permiten conexiones con redes internas de ECI.
   - Internet - Entrada: El entorno publica servicios en Internet.
   - Internet - Salida: El entorno requiere conexiones salientes a Internet.
   - Internet - Entrada/Salida: Se aplican las dos condiciones anteriores.

Si no obtienes alguno de estos datos, indícalo en la tabla: "No hay información suficiente sobre este dato"
]

</br>
</br>

**SEGURIDAD**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Autenticación |  | 
| Autorización |  | 
| Conectividad |  | 


[Operación y monitorización:
Lista de requisitos de monitorizacion para la solución:

- Estrategia de monitorización:
   - Qué herramientas se usan?
   - Qué KPIs servicios se monitorizan
   - Cómo se explotan y analizan los logs
   - Paneles de Grafana
- Acuerdo de Nivel de Servicio (SLA) 
- Estrategia de disaster recovery de la solución

Rellena la siguiente tabla con tantas filas como necesites, incluyendo alertas, métricas expuestas o qué dashboards se utilizan.

Si no obtienes alguno de estos datos, indícalo en la tabla: "No hay información suficiente sobre este dato"
]

</br>
</br>

**OPERACIÓN / MONITORIZACIÓN**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Estrategia de monitorización |  | 
|  |  | 


[DevOps:
Lista de requisitos técnicos de DevOps para los productos/aplicaciones dentro del alcance de la migración de la CMO:

- Petición On-Boarding (SIAYA): Identificar la petición de onboarding en la plataforma Corporativa.
- Repositorios de la solución. Identificar los repositorios asociados a los distintos componentes que la conforman.
- Uso de "Test Automatizados". ¿Hace uso de test automatizados proporcionados por la plataforma corporativa de CICD? ¿De qué tipo? Identificar repositorios asociados.
- "No Code". Hace uso de elementos no_code ( kafka, couch o alertas). ¿Cual de ellos?
- Entornos/Plataformas de despliegue. Identificar plataforma/sistemas de instalación y entornos.

Si no obtienes alguno de estos datos, indícalo en la tabla: "No hay información suficiente sobre este dato"
]

</br>
</br>

**DEVOPS**
| Tipo de requerimiento | Descripción del requerimiento | Detalle | 
|------------|---------|---|
| Petición On-Boarding (SIAYA) | Número de ticket  |  | 
| Componente | nombre del componente  |  url del repositorio origen | 
| Uso de Tests Automatizados | Información sobre los tests automatizados |  | 
| No Code (Kafka / Couch / Alertas) | Información sobre No Code |  | 
| Entornos / Plataformas de despliegue | Plataformas y entornos identificados |  | 




[

Identificar y describir los principales requisitos técnicos que se tendrán en cuenta para el diseño y desarrollo de la solución. Ayudarán a identificar las características básicas, las dependencias y los criterios de aceptación necesarios para la plataforma en la nube y los servicios proporcionados por la plataforma:

- Uso de librerías:
   - Librerías propietarias no open-source
   - Librerías internas de las que el aplicativo no es owner (ej, libs de ATG)
   - Librerías que por su naturaleza deben ser deprecadas en el Journey to Cloud
   - Entender la configuración de librerías utilizadas y su variabilidad por entorno

- Servicios del equipo de Visual Studio (Sí/No)
   - Nombre de la provisión del proyecto de equipo
   - Se requieren funciones de usuario (administradores de proyectos de equipo, editores de plantillas de procesos, colaboradores...
   - Se necesita una plantilla de proceso (Scrum/Agile)

- Acceso a los datos: Identifica las estrategias de acceso a los datos y cómo se almacenarán los datos. Esto incluye el diseño de la entidad de datos, la gestión de errores y la gestión de conexiones a la base de datos.

   - Indicar especialmente accesos directos a bases de datos externas al aplicativo (ej, Oracle de ATG)
   - Explicitar accesos a datos externos que no se hagan por canales estandarizados/gobernados como APIs o topics de Kafka
   - Indicar si las entidades cumplen con el Modelo Común de Información

- Almacenamiento en caché: determine qué tecnología de almacenamiento en caché se debe utilizar, qué datos almacenar en caché, dónde almacenar en caché los datos y una política de caducidad adecuada.

- Acuerdo de Nivel de Servicio (SLA) - si se necesita producción lista: (Sí / No)

- Tipo de entorno de producción - si es un entorno de misión crítica: (Sí / No)

- Gestión de la configuración: determine qué información será configurable, así como la ubicación y las técnicas para almacenar la información de configuración. Ten en cuenta cómo manejar la información de configuración confidencial.

- Peculiaridades de entornos preproductivos

Si no obtienes alguno de estos datos, indícalo en la tabla: "No hay información suficiente sobre este dato". Añade tantas filas a la tabla como necesites.

]

</br>
</br>

**REQUISITOS TECNICOS**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Arquitectura |   |
| Lenguage y librerías |  |  
| Configuración |   |
| Despliegue |   | 



### 2.3 Servicios y Jobs

[
- Identifica cada uno de los Servicios y Jobs que se despliegan y el entorno en el que se despliegan.
- Identifica el namespace, componente, así como el tipo (si es Deployment o es un Job), el número de réplicas, la talla y la Quota máxima del Namespace.
- No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración. Si no tienes datos suficientes para rellenar la tabla, indícalo: "No hay información suficiente" 
- Añade tantas filas a la tabla como necesites.
]

**UBICACIÓN DE COMPONENTES**
| Entorno | Namespace | Componentes | Tipo | Réplicas  | Talla  | Quota Máxima Namespace  |  
|------------|---------|---|---|---|---|---|
| PRO/NFT/UAT | namespace   | nombre del componente  | Deployment/Job  | 0x0  | M L XL S M2 | 0c0m x 0c0m | 
|  |  |  |  |  |  |  |  

### 2.4 Matriz de comunicación

[
- Identifica todas las comunicaciones de los componentes.
- Buscar en el código fuente y ficheros de configuración referencias a otros servicios o plataformas externas.
- Buscar en los ficheros de configuración dentro de la carpeta config-manager
- Identificar las URLs, endpoints o direcciones utilizados para interactuar con estas dependencias. 
- Identificar cualquier otra comunicación externa que utiliza cada componente.
- Añade una fila por destino (Kafka, MongoDB, etc)
- Añade tantas filas como necesites
- Indica el FQDN destino completo por entorno

]

**MATRIZ DE COMUNICACIONES CON SISTEMAS EXTERNOS**
| Origen | Destino | FQDN/IP Destino | Protocolo L7 | Puerto  | Autenticación  | Propósito  | 
|------------|---------|---|---|---|---|--|
| Listado de componentes | Sistema de destino (Kafka, IDP, MongoDB...)   | FQDN completo por entorno (UAT, NFT, PRO)  | HTTPS, HTTP, JDBC, Kafka... | Número de puerto	  | Tipo de autenticación (bearer, user/pass, certificado) | Explicación |
|  |  |  |  |  |  |  | 


### 2.5 APIs y consumidores

[
- Identifica cada una de las apis o sistemas expuestos por cada uno de los componentes de la aplicación y aquellos sistemas que lo consumen
- Por cada componente:
  - Buscar en el código fuente y ficheros de configuración referencias a APIs externas que utilice cada componente.
  - Buscar en los ficheros de configuración dentro de la carpeta config-manager
  - Identificar las URLs, endpoints y métodos HTTP utilizados para interactuar con estas APIs.
  - Si identificas el entorno (dev, uat, pro) en el que se exponen las APIs, indícalo.
- Añade tantas filas como necesites
- Si no tienes información del consumidor de la API, indícalo "No hay información suficiente sobre este dato"
]

| WSO API Name | Contexto | Versiones desplegadas | Gateways | Microservicio  | Endpoint  | 
|------------|---------|---|---|---|---|
| Nombre del api en WSO | /context/api-name | Version del api | ONPREM Internal, ONPREM External | Microservicio que expone la API | Destino final | 
| ms_eci_dataentry_middleware_v1 | /products/ms-eci-dataentry-middleware/v1 | 1.0.0 | ONPREM Internal | ms-eci-dataentry-stibo	 | https://ms-eci-dataentry-stibo.paas.uat.eci.geci/products/ms-eci-dataentry-middleware/v1 | 

**Detalle de los consumidores**

[Por cada una de las APIs expuestas identificadas en el apartado anterior, añade una fila e identifica qué servicio o aplicación consume esa API.
No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración. Si no tienes datos suficientes para rellenar la tabla, indícalo: "No hay información suficiente" ]

| WSO API Name | App WSO - Subscriptores | Llamadas últimos 30 días | Notas | 
|------------|---------|---|---|
| Nombre del api en WSO | Listado de servicios y/o aplicaciones que consumen el api: servicio A, servicio B, servicio C | Número de llamdas en los últimos 30 días | Notas adicionales | 
ms_eci_dataentry_middleware_v1 | servicio A | 40 | Notas adicionales |

### 2.6 Comunicaciones asíncronas

[
Por cada componente de la aplicación:
  - Identificar todas las plataformas de mensajería o eventing que utiliza.
  - Buscar en el código fuente y ficheros de configuración referencias a plataformas de mensajería como Kafka, RabbitMQ, ActiveMQ, etc.
  - Buscar en los ficheros de configuración dentro de la carpeta config-manager
  - Identificar los topics, colas o canales utilizados para enviar y recibir mensajes.
  - Identificar si es un consumidor o productor de la cola identificada.
  - Identificar los brokeres o servidores de mensajería configurados.
- Con toda esta información, rellena la siguiente tabla.
- Añade tantas filas como necesites
]



**TÓPICOS DE KAFKA CONSUMIDORES**
| Servicio | Nombre | 
|------------|---------|
| Servicio que consume el mensaje Kafka| Nombre de la cola de Kafka que consume ese servicio   | 
| por ejemplo: ms-eci-linguaserv-stibo | 2WP-000.PRODUCTS.MASTERDATA.TRANSLATIONS_GOB.TOP | 

**TÓPICOS DE KAFKA PRODUCTORES**
| Servicio | Nombre | 
|------------|---------|
| Servicio que produce el mensaje Kafka | Nombre de la cola de Kafka que produce ese servicio   | 
| por ejemplo: ms-eci-stibo-repocloud-tform | 2WQ-000.PIM.PRODUCTS.MIDDLEWAREREPOCLOUD_NGOB.TOP | 

### 2.7 Bases de datos

[
Identificar todas las bases de datos que utiliza la aplicación. Por cada componente:
- Buscar en el código fuente y ficheros de configuración referencias a bases de datos como MySQL, PostgreSQL, MongoDB, etc.
- Buscar en los ficheros de configuración dentro de la carpeta config-manager
- Identificar el nombre de los esquemas, tablas o colecciones utilizadas por la aplicación.
- Identificar el nombre de los servidores o instancias de bases de datos configuradas.
- Identifica Política de eliminación (TTL): si los datos se eliminarán después de un período de tiempo determinado. Indica la colección y el tiempo.
- Si identificas los índices definidos, indícalos.
- Si identificas el entorno (desarrollo, preproducción, producción, ...) en el que se utilizan las plataformas de mensajería, indícalo.

No hagas asunciones. Añade solamente información confirmada y usada en el código o en el fichero de configuración. Si ves una referencia a una base de datos, cerciórate de que se usa en el código fuente. Si solamente hay una referencia en las dependencias pero no se usa en el código, añádelo a la sección "Información Adicional"


Devuelve una lista con el nombre de la base de datos, su URL o dirección completa, el tipo de base de datos, entorno y una breve descripción de su propósito así como el nombre de las tablas o colecciones que utiliza la aplicación en forma de tabla siguiendo este formato:]

</br>
</br>

**BASE DE DATOS**
| Componente | Base de Datos | URL/Dirección completa | Tipo       | Entorno(s) | Propósito | Tablas/Colecciones | Notas (TTL e índices) |
|-------------|---------------|---------------|------------|------------|-----------|---------------------|--------|
| componente1 | MySQL         | mysql:3306    | Relacional | pro   | Almacenamiento de datos | Nombre de tabla1, tabla2       |  TTL       |
| componente2 | MongoDB       | mongo:27017   | NoSQL      | pro        | Almacenamiento de documentos | Nombre de coleccion1, coleccion2 | TTL |
| componente2 | MongoDB       | mongo:27017   | NoSQL      | dev, uat        | Almacenamiento de documentos | Nombre de coleccion1, coleccion2 | TTL |




---

## 3. Información adicional

### Desafíos o problemas actuales
[Opcional: Enumera cualquier problema conocido, limitaciones o áreas de preocupación con el sistema actual. Indica en esta sección si hay referencias que no se usan en el código.]

### Notas importantes
[Opcional: Agrega cualquier otra información relevante que no encaje en las secciones anteriores]


