# Documento AS-IS: 2WQ-000 - Demo copilot

> **Propósito del documento**: Este documento captura el estado actual del proyecto tal como existe hoy. Sirve como punto de referencia para comprender lo que tenemos antes de planificar cualquier migración o cambio.

---

## 1. Descripción

### 1.1 Resumen del proyecto
**Código de proyecto**: 2WQ-000

**Nombre del proyecto**: Demo copilot

**Descripción del proyecto**:
Este proyecto es una colección de ejemplos educativos que muestran diferentes formas de construir arquitecturas de microservicios en Java. El proyecto contiene cinco ejemplos diferentes que demuestran distintas tecnologías y enfoques para crear sistemas basados en microservicios. Cada ejemplo es independiente y sirve como material de referencia para comprender cómo implementar microservicios con diferentes combinaciones de tecnologías.

El proyecto incluye ejemplos básicos con Spring Boot y Spring Cloud, ejemplos generados con JHipster (una herramienta para generar aplicaciones), ejemplos de microservicios reactivos (que responden de manera más eficiente a las peticiones), y ejemplos de despliegue en Kubernetes (una plataforma para ejecutar aplicaciones en contenedores).

**Tecnologías principales utilizadas en el proyecto:**
- Java 11
- Spring Boot 2.2.5
- Spring Cloud (versión Hoxton.SR10)
- Spring Cloud Config
- Spring Cloud Gateway
- Spring WebFlux (programación reactiva)
- Netflix Eureka (para registro de servicios)
- Netflix Zuul (para enrutamiento de peticiones)
- JHipster 7
- OAuth 2.0 / OIDC con Okta (autenticación segura)
- PostgreSQL (base de datos relacional)
- MongoDB (base de datos de documentos)
- Neo4j (base de datos de grafos)
- H2 Database (base de datos en memoria)
- Docker y Docker Compose
- Kubernetes
- Maven (herramienta de construcción)
- Gradle (herramienta de construcción)

### 1.2 Funcionalidades principales

Este proyecto es educativo y contiene ejemplos de las siguientes funcionalidades:

1. **Registro y descubrimiento de servicios**: Los microservicios se registran automáticamente y pueden encontrarse entre sí sin configuración manual de direcciones.

2. **Enrutamiento de peticiones (API Gateway)**: Un punto de entrada único que dirige las peticiones a los microservicios correspondientes.

3. **Configuración centralizada**: La configuración de todos los servicios se gestiona desde un lugar central, facilitando los cambios.

4. **Autenticación y autorización seguras**: Integración con sistemas de autenticación externos (Okta) usando estándares de seguridad OAuth 2.0 y OpenID Connect.

5. **Gestión de blogs**: Ejemplo de microservicio que permite crear y gestionar blogs y publicaciones.

6. **Gestión de productos**: Ejemplo de microservicio que maneja un catálogo de productos en una tienda.

7. **Gestión de automóviles**: Ejemplo básico de microservicio que proporciona información sobre automóviles.

8. **Programación reactiva**: Ejemplos que muestran cómo construir servicios que responden de manera más eficiente usando Spring WebFlux.

9. **Despliegue en contenedores**: Configuraciones para ejecutar los microservicios en Docker y Kubernetes.

10. **Monitorización**: Integración con Prometheus para recopilar métricas y Grafana para visualizarlas.

### 1.3 Usuarios

No hay información suficiente sobre usuarios específicos del sistema. Este proyecto es de naturaleza educativa y sirve como material de referencia para desarrolladores que desean aprender sobre arquitecturas de microservicios.

| Usuario o sistema | Descripción del uso general que el usuario da al sistema o las interacciones importantes de este |
|------------|---------|
| Desarrolladores | Utilizan este proyecto como referencia y ejemplo para aprender a construir arquitecturas de microservicios con Spring Boot y Spring Cloud |
| Okta (Sistema de autenticación) | Sistema externo que proporciona servicios de autenticación y autorización para los ejemplos |

---

## 2. Arquitectura técnica

### 2.1 Diseño de la solución

El proyecto contiene 5 arquitecturas de ejemplo independientes:

| Componente | Descripción | 
|------------|---------|
| **spring-boot+cloud/discovery-service** | Java 11 con Spring Boot 2.2.5. Servidor de registro Eureka que permite a los microservicios registrarse y descubrirse entre sí. No utiliza bases de datos. Expone interfaz web en puerto 8761. Utiliza Spring Cloud Netflix Eureka Server. |
| **spring-boot+cloud/car-service** | Java 11 con Spring Boot 2.2.5. Microservicio REST que gestiona información de automóviles. Utiliza base de datos H2 en memoria con Spring Data JPA. Expone APIs REST. Se registra con Eureka. Autenticación con Okta OAuth 2.0. Expone métricas con Spring Boot Actuator. Utiliza Lombok para reducir código repetitivo. |
| **spring-boot+cloud/api-gateway** | Java 11 con Spring Boot 2.2.5. Puerta de enlace API que enruta peticiones a los microservicios usando Netflix Zuul. Autenticación con Okta OAuth 2.0. Utiliza Hystrix para tolerancia a fallos y OpenFeign para comunicación entre servicios. Se registra con Eureka. Puerto 8080. |
| **jhipster/gateway** | Java 11 generado con JHipster. Puerta de enlace usando Netflix Zuul. Base de datos PostgreSQL. Autenticación OAuth 2.0/OIDC. Configuración centralizada con Spring Cloud Config desde JHipster Registry. Expone métricas Prometheus. Incluye Swagger para documentación de APIs. Puerto 8080. |
| **jhipster/blog** | Java 11 generado con JHipster. Microservicio para gestión de blogs. Base de datos PostgreSQL. Autenticación OAuth 2.0/OIDC. Se registra en JHipster Registry. Expone métricas Prometheus. Incluye Swagger. |
| **jhipster/store** | Java 11 generado con JHipster. Microservicio para gestión de tienda/productos. Base de datos MongoDB. Autenticación OAuth 2.0/OIDC. Se registra en JHipster Registry. Expone métricas Prometheus. Incluye Swagger. |
| **spring-cloud-gateway/discovery-service** | Java 11 con Spring Boot 2.2.5. Servidor de registro Eureka (igual que spring-boot+cloud). Puerto 8761. |
| **spring-cloud-gateway/car-service** | Java 11 con Spring Boot 2.2.5. Microservicio reactivo con Spring WebFlux. Base de datos H2 en memoria. Autenticación con Okta. Se registra con Eureka. Expone APIs REST reactivas. |
| **spring-cloud-gateway/api-gateway** | Java 11 con Spring Boot 2.2.5. Puerta de enlace reactiva usando Spring Cloud Gateway (reemplazo moderno de Zuul). Spring WebFlux para procesamiento reactivo. Autenticación con Okta OAuth 2.0. Se registra con Eureka. Puerto 8080. |
| **reactive-jhipster/gateway** | Java 11 generado con JHipster usando Gradle. Puerta de enlace reactiva con Spring Cloud Gateway y Spring WebFlux. Base de datos PostgreSQL con R2DBC (acceso reactivo). Autenticación OAuth 2.0/OIDC. Configuración desde JHipster Registry. Expone métricas Prometheus. Puerto 8080. |
| **reactive-jhipster/blog** | Java 11 generado con JHipster usando Gradle. Microservicio reactivo para blogs. Base de datos Neo4j (base de datos de grafos). Spring WebFlux. Autenticación OAuth 2.0/OIDC. Se registra en JHipster Registry. Expone métricas Prometheus. |
| **reactive-jhipster/store** | Java 11 generado con JHipster usando Gradle. Microservicio reactivo para tienda. Base de datos MongoDB con acceso reactivo. Spring WebFlux. Autenticación OAuth 2.0/OIDC. Se registra en JHipster Registry. Expone métricas Prometheus. |
| **jhipster-k8s/gateway** | Java 11 generado con JHipster 7 usando Gradle. Puerta de enlace reactiva con Spring Cloud Gateway. Base de datos PostgreSQL. Autenticación OAuth 2.0/OIDC. Configuración desde JHipster Registry. Configuraciones Kubernetes incluidas. Puerto 8080. |
| **jhipster-k8s/blog** | Java 11 generado con JHipster 7 usando Gradle. Microservicio reactivo para blogs. Base de datos Neo4j. Configuraciones Kubernetes incluidas. Autenticación OAuth 2.0/OIDC. |
| **jhipster-k8s/store** | Java 11 generado con JHipster 7 usando Gradle. Microservicio reactivo para tienda. Base de datos MongoDB con clustering. Configuraciones Kubernetes incluidas. Autenticación OAuth 2.0/OIDC. |

**Diagrama de arquitectura**:

```mermaid
graph TB
    subgraph "Ejemplo 1: spring-boot+cloud"
        User1[Usuario] -->|HTTP| GW1[api-gateway:8080<br/>Zuul]
        GW1 -->|Descubre servicios| Eureka1[discovery-service:8761<br/>Eureka Server]
        GW1 -->|Enruta a| Car1[car-service:8090]
        Car1 --> H2_1[(H2 Database<br/>En memoria)]
        Car1 -->|Se registra| Eureka1
        GW1 -->|Autenticación| Okta1[Okta OAuth 2.0]
        Car1 -->|Autenticación| Okta1
    end
    
    subgraph "Ejemplo 2: jhipster"
        User2[Usuario] -->|HTTP| GW2[gateway:8080<br/>Zuul]
        GW2 -->|Config| Registry2[JHipster Registry<br/>Eureka + Config Server]
        GW2 -->|Enruta a| Blog2[blog]
        GW2 -->|Enruta a| Store2[store]
        GW2 --> PG2[(PostgreSQL)]
        Blog2 --> PG2B[(PostgreSQL)]
        Store2 --> Mongo2[(MongoDB)]
        Blog2 -->|Se registra| Registry2
        Store2 -->|Se registra| Registry2
        GW2 -->|Autenticación| Okta2[Okta/Keycloak]
    end
    
    subgraph "Ejemplo 3: spring-cloud-gateway"
        User3[Usuario] -->|HTTP| GW3[api-gateway:8080<br/>Spring Cloud Gateway<br/>Reactivo]
        GW3 -->|Descubre| Eureka3[discovery-service:8761]
        GW3 -->|Enruta a| Car3[car-service:8090<br/>WebFlux Reactivo]
        Car3 --> H2_3[(H2 Database)]
        Car3 -->|Se registra| Eureka3
        GW3 -->|Autenticación| Okta3[Okta OAuth 2.0]
    end
    
    subgraph "Ejemplo 4: reactive-jhipster"
        User4[Usuario] -->|HTTP| GW4[gateway:8080<br/>Spring Cloud Gateway<br/>Reactivo]
        GW4 -->|Config| Registry4[JHipster Registry]
        GW4 -->|Enruta a| Blog4[blog<br/>Reactivo]
        GW4 -->|Enruta a| Store4[store<br/>Reactivo]
        GW4 --> PG4[(PostgreSQL<br/>R2DBC)]
        Blog4 --> Neo4j4[(Neo4j)]
        Store4 --> Mongo4[(MongoDB<br/>Reactivo)]
        GW4 -->|Autenticación| Okta4[Okta]
    end
    
    subgraph "Ejemplo 5: jhipster-k8s"
        User5[Usuario] -->|HTTP| Ingress[Kubernetes Ingress]
        Ingress --> GW5[gateway:8080<br/>Spring Cloud Gateway]
        GW5 -->|Config| Registry5[JHipster Registry<br/>Kubernetes Service]
        GW5 -->|Enruta a| Blog5[blog<br/>Kubernetes Pod]
        GW5 -->|Enruta a| Store5[store<br/>Kubernetes Pod]
        GW5 --> PG5[(PostgreSQL<br/>Kubernetes Service)]
        Blog5 --> Neo4j5[(Neo4j<br/>Kubernetes Service)]
        Store5 --> Mongo5[(MongoDB<br/>StatefulSet)]
        GW5 -->|Autenticación| Okta5[Okta]
    end
    
    Prometheus[Prometheus] -.->|Métricas| GW2
    Prometheus -.->|Métricas| Blog2
    Prometheus -.->|Métricas| Store2
    Prometheus -.->|Métricas| GW4
    Prometheus -.->|Métricas| GW5
```

### 2.2 Requisitos principales

<br/>

**DATOS**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Clasificación de datos | Non-Sensitive. El proyecto es educativo y de demostración. No maneja datos de producción reales. Los datos son de ejemplo para pruebas. | 
| Tiempo de datos | Temporal. Los datos son para propósitos de demostración y pueden eliminarse en cualquier momento. Algunos componentes usan bases de datos en memoria (H2) que se pierden al reiniciar. | 
| Protección de datos | Los datos de ejemplo no requieren protección especial. La autenticación con OAuth 2.0 y OIDC está implementada para demostrar buenas prácticas de seguridad. Las credenciales de Okta están configuradas en archivos de propiedades (application.properties). Spring Security protege los endpoints. |

<br/>
<br/>

**SEGURIDAD**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Autenticación | **Fuente de autenticación**: Usuarios externos mediante Okta (proveedor de identidad cloud). **Proveedor de identidad (IdP)**: Okta Developer Account. **Tipo de credenciales**: OAuth 2.0 / OpenID Connect (OIDC) con tokens JWT. **Protocolos de autenticación**: OAuth 2.0, OpenID Connect (OIDC), JWT. **Servicios de tokens de seguridad (STS)**: Okta proporciona los tokens de acceso y tokens de ID. En algunos ejemplos también se configura Keycloak como alternativa. | 
| Autorización | Spring Security con roles basados en grupos de Okta (ROLE_ADMIN, ROLE_USER). Los grupos se incluyen en el token JWT como claims. JHipster utiliza autorización basada en roles para controlar acceso a endpoints y funcionalidades. | 
| Conectividad | **Red corporativa**: No. Este es un proyecto de demostración que se ejecuta localmente. **Internet - Salida**: Sí. Se requiere conexión saliente a Internet para autenticación con Okta (issuer URI: https://{yourOktaDomain}/oauth2/default) y para descargar dependencias durante la construcción. **Internet - Entrada**: No aplica para el entorno de demostración local. Si se despliega en cloud (como en el ejemplo de Kubernetes), se expondría a través de un Ingress o LoadBalancer. |

<br/>
<br/>

**OPERACIÓN / MONITORIZACIÓN**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Estrategia de monitorización | **Herramientas**: Spring Boot Actuator para exponer métricas de salud y estado. Prometheus para recolección de métricas (configurado en ejemplos JHipster con `MANAGEMENT_METRICS_EXPORT_PROMETHEUS_ENABLED=true`). JHipster Control Center para monitorización centralizada de aplicaciones JHipster. **KPIs monitorizados**: Métricas JVM (memoria, hilos), métricas HTTP (peticiones, tiempos de respuesta), métricas de base de datos, métricas personalizadas expuestas en endpoint `/management/prometheus`. **Logs**: Los logs se gestionan con Logback (configuración estándar de Spring Boot). **Dashboards**: JHipster Control Center proporciona dashboards para visualizar el estado de los microservicios. | 
| Acuerdo de Nivel de Servicio (SLA) | No hay información suficiente sobre este dato. El proyecto es de demostración y no tiene SLAs definidos. |
| Estrategia de disaster recovery | No hay información suficiente sobre este dato. El proyecto es de demostración y no incluye estrategias de disaster recovery. |

<br/>
<br/>

**DEVOPS**
| Tipo de requerimiento | Descripción del requerimiento | Detalle | 
|------------|---------|---|
| Petición On-Boarding (SIAYA) | No hay información suficiente sobre este dato | El proyecto es de código abierto y educativo, no está integrado con plataformas corporativas | 
| Componente - spring-boot+cloud/discovery-service | discovery-service | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud | 
| Componente - spring-boot+cloud/car-service | car-service | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - spring-boot+cloud/api-gateway | api-gateway | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster/gateway | gateway | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster/blog | blog | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster/store | store | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - spring-cloud-gateway/discovery-service | discovery-service | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - spring-cloud-gateway/car-service | car-service | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - spring-cloud-gateway/api-gateway | api-gateway | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - reactive-jhipster/gateway | gateway | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - reactive-jhipster/blog | blog | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - reactive-jhipster/store | store | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster-k8s/gateway | gateway | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster-k8s/blog | blog | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Componente - jhipster-k8s/store | store | Repositorio origen: Bitbucket - Java Microservices examples with Spring Boot & Spring Cloud |
| Uso de Tests Automatizados | Se incluyen tests unitarios usando JUnit y Spring Boot Test | Los componentes incluyen dependencia spring-boot-starter-test. Se ejecutan con Maven (./mvnw test) o Gradle (./gradlew test) |
| No Code (Kafka / Couch / Alertas) | No se utiliza | No hay referencias a Kafka, CouchDB o sistemas de alertas en la configuración |
| Entornos / Plataformas de despliegue | Local (desarrollo), Docker Compose, Kubernetes | **Local**: Ejecución con Maven o Gradle. **Docker**: Configuraciones docker-compose.yml para despliegue en contenedores. **Kubernetes**: Manifiestos K8s en jhipster-k8s/k8s/ para despliegue en clústeres Kubernetes (probado con Minikube y Google Cloud). |

<br/>
<br/>

**REQUISITOS TECNICOS**
| Tipo de requerimiento | Descripción del requerimiento | 
|------------|---------|
| Arquitectura | Arquitectura de microservicios con patrón API Gateway. Registro y descubrimiento de servicios con Netflix Eureka. Configuración centralizada con Spring Cloud Config. Ejemplos de arquitectura tradicional (blocking) y reactiva (non-blocking con Spring WebFlux). |
| Lenguaje y librerías | **Java 11** como lenguaje principal. **Spring Boot 2.2.5** para crear aplicaciones. **Spring Cloud Hoxton.SR10** para microservicios. **Netflix OSS** (Eureka, Zuul, Hystrix, Ribbon) para patrones de microservicios. **Spring Cloud Gateway** para gateway reactivo. **Spring WebFlux** para programación reactiva. **Spring Data JPA** para acceso a datos relacionales. **Spring Data MongoDB** para MongoDB. **Spring Data Neo4j** para Neo4j. **Okta Spring Boot Starter 1.4.0** para autenticación. **Lombok** para reducir código boilerplate. **JHipster 7** para generación de código. Librerías propietarias: Okta Spring Boot Starter (open source pero específico de proveedor). No se identifican librerías deprecadas. |  
| Configuración | **Archivos de configuración**: application.properties y application.yml en src/main/resources/config/. **Configuración por entorno**: Perfiles de Spring (dev, prod) definidos con application-dev.yml, application-prod.yml. **Spring Cloud Config**: En ejemplos JHipster, la configuración se centraliza en JHipster Registry y se distribuye desde archivos en docker-compose/central-server-config/application.yml. **Configuración Kubernetes**: ConfigMaps en k8s/registry-k8s/application-configmap.yml. **Secretos**: Las credenciales de Okta están en archivos de configuración en texto plano (no recomendado para producción). En Kubernetes se usan Sealed Secrets para encriptar secretos. |
| Despliegue | **Maven**: Construcción con ./mvnw clean package. Ejecución con ./mvnw spring-boot:run. **Gradle**: Construcción con ./gradlew build. Ejecución con ./gradlew bootRun. **Docker**: Construcción de imágenes con Jib (mvn -Pprod verify com.google.cloud.tools:jib-maven-plugin:dockerBuild o ./gradlew bootJar -Pprod jib). **Docker Compose**: Archivos docker-compose.yml para orquestar múltiples servicios. **Kubernetes**: Manifiestos YAML generados con jhipster k8s. Despliegue con kubectl apply. Script kubectl-apply.sh para aplicar todos los manifiestos. Soporte para Minikube (desarrollo local) y Google Cloud Platform. **Namespace**: demo (en configuración Kubernetes). |

### 2.3 Servicios y Jobs

No hay información suficiente sobre despliegues en entornos específicos (PRO/NFT/UAT). El proyecto es de demostración y está diseñado para ejecutarse localmente o en entornos de desarrollo. Las configuraciones Docker Compose y Kubernetes definen la estructura de despliegue pero no especifican entornos corporativos, namespaces productivos, tallas de recursos ni quotas.

**UBICACIÓN DE COMPONENTES**
| Entorno | Namespace | Componentes | Tipo | Réplicas  | Talla  | Quota Máxima Namespace  |  
|------------|---------|---|---|---|---|---|
| Desarrollo local | No aplica | discovery-service, car-service, api-gateway, gateway, blog, store | Aplicación Java | No aplica | No aplica | No aplica |
| Docker Compose | No aplica | gateway-app, blog-app, store-app, jhipster-registry, keycloak, gateway-postgresql, blog-postgresql, store-mongodb | Contenedor Docker | 1 por servicio | _JAVA_OPTIONS=-Xmx512m -Xms256m (configurado para apps Java) | No aplica |
| Kubernetes (demo) | demo | gateway, blog, store, jhipster-registry, postgresql, neo4j, mongodb | Deployment/StatefulSet | No hay información suficiente sobre número específico de réplicas | No hay información suficiente sobre tallas específicas | No hay información suficiente |

### 2.4 Matriz de comunicación

**MATRIZ DE COMUNICACIONES CON SISTEMAS EXTERNOS**
| Origen | Destino | FQDN/IP Destino | Protocolo L7 | Puerto  | Autenticación  | Propósito  | 
|------------|---------|---|---|---|---|--|
| api-gateway (spring-boot+cloud) | Okta | https://dev-133320.okta.com/oauth2/default | HTTPS | 443 | Client ID y Client Secret OAuth 2.0 | Autenticación de usuarios mediante OpenID Connect |
| car-service (spring-boot+cloud) | Okta | https://dev-133320.okta.com/oauth2/default | HTTPS | 443 | Client ID y Client Secret OAuth 2.0 | Validación de tokens de acceso |
| api-gateway (spring-boot+cloud) | Eureka Server | http://localhost:8761/eureka | HTTP | 8761 | Sin autenticación | Registro y descubrimiento de servicios |
| car-service (spring-boot+cloud) | Eureka Server | http://localhost:8761/eureka | HTTP | 8761 | Sin autenticación | Registro del servicio en Eureka |
| api-gateway (spring-boot+cloud) | car-service | http://localhost:8090 | HTTP | 8090 | OAuth 2.0 Bearer Token | Enrutamiento de peticiones a través de Zuul |
| gateway (jhipster) | JHipster Registry | http://admin:{password}@jhipster-registry:8761/eureka | HTTP | 8761 | Basic Auth (usuario: admin) | Registro de servicios |
| gateway (jhipster) | JHipster Registry Config Server | http://admin:{password}@jhipster-registry:8761/config | HTTP | 8761 | Basic Auth (usuario: admin) | Obtención de configuración centralizada |
| blog (jhipster) | JHipster Registry | http://admin:{password}@jhipster-registry:8761/eureka | HTTP | 8761 | Basic Auth (usuario: admin) | Registro de servicios |
| store (jhipster) | JHipster Registry | http://admin:{password}@jhipster-registry:8761/eureka | HTTP | 8761 | Basic Auth (usuario: admin) | Registro de servicios |
| gateway (jhipster) | PostgreSQL | jdbc:postgresql://gateway-postgresql:5432/gateway | JDBC | 5432 | Usuario/contraseña PostgreSQL | Almacenamiento de datos del gateway |
| blog (jhipster) | PostgreSQL | jdbc:postgresql://blog-postgresql:5432/blog | JDBC | 5432 | Usuario/contraseña PostgreSQL | Almacenamiento de datos de blogs |
| store (jhipster) | MongoDB | mongodb://store-mongodb:27017 | MongoDB Protocol | 27017 | Sin autenticación (desarrollo) | Almacenamiento de datos de productos |
| gateway (jhipster) | Keycloak | http://keycloak:9080/auth/realms/jhipster | HTTP | 9080 | Client ID y Client Secret | Autenticación OAuth 2.0 / OIDC (alternativa a Okta) |
| gateway (spring-cloud-gateway) | Okta | https://{yourOktaDomain}/oauth2/default | HTTPS | 443 | Client ID y Client Secret OAuth 2.0 | Autenticación de usuarios |
| gateway (spring-cloud-gateway) | Eureka Server | http://localhost:8761/eureka | HTTP | 8761 | Sin autenticación | Descubrimiento de servicios |
| gateway (reactive-jhipster) | Okta | https://{yourOktaDomain}/oauth2/default | HTTPS | 443 | Client ID y Client Secret OAuth 2.0 | Autenticación OIDC |
| gateway (reactive-jhipster) | PostgreSQL | r2dbc:postgresql://localhost:5432/gateway | R2DBC | 5432 | Usuario/contraseña | Acceso reactivo a base de datos |
| blog (reactive-jhipster) | Neo4j | neo4j://localhost:7687 | Bolt Protocol | 7687 | Usuario/contraseña Neo4j | Almacenamiento de grafos (blogs y posts) |
| store (reactive-jhipster) | MongoDB | mongodb://localhost:27017/store | MongoDB Protocol | 27017 | Sin autenticación (desarrollo) | Almacenamiento reactivo de productos |
| gateway (jhipster-k8s) | Okta | https://{yourOktaDomain}/oauth2/default | HTTPS | 443 | Client ID y Client Secret OAuth 2.0 | Autenticación en Kubernetes |
| gateway (jhipster-k8s) | JHipster Registry (K8s Service) | http://admin:{password}@jhipster-registry:8761 | HTTP | 8761 | Basic Auth | Configuración y registro en Kubernetes |
| Todos los servicios JHipster | Prometheus | No aplica (Prometheus scrapea endpoints) | HTTP | Management port | Sin autenticación | Exposición de métricas en /management/prometheus |

### 2.5 APIs y consumidores

No hay información suficiente sobre un API Gateway corporativo (WSO2) ni sobre publicación formal de APIs. El proyecto es de demostración y las APIs se exponen directamente desde los microservicios sin pasar por un gateway empresarial.

Las APIs expuestas son:

| WSO API Name | Contexto | Versiones desplegadas | Gateways | Microservicio  | Endpoint  | 
|------------|---------|---|---|---|---|
| No aplica | /cars | No aplica | api-gateway (Zuul) en localhost:8080 | car-service | http://localhost:8090 (desarrollo local) | 
| No aplica | /home | No aplica | api-gateway (Zuul) en localhost:8080 | car-service | http://localhost:8090 (desarrollo local) |
| No aplica | /services/** | No aplica | gateway (JHipster Zuul) en localhost:8080 | blog, store | Rutas dinámicas descubiertas vía Eureka |
| No aplica | /api/** | No aplica | gateway (Spring Cloud Gateway) en localhost:8080 | car-service | Rutas dinámicas (desarrollo local) |
| No aplica | /api/** | No aplica | gateway (reactive-jhipster) en localhost:8080 | blog, store | Rutas reactivas descubiertas vía Eureka |
| No aplica | /api/** | No aplica | gateway (jhipster-k8s) en Kubernetes | blog, store | Rutas en Kubernetes con Ingress |

**Detalle de los consumidores**

No hay información suficiente sobre consumidores específicos. El proyecto es de demostración y está diseñado para ser accedido por navegadores web o herramientas de prueba de APIs como Postman o curl. Los usuarios finales interactúan con las aplicaciones a través de interfaces web generadas por JHipster.

| WSO API Name | App WSO - Subscriptores | Llamadas últimos 30 días | Notas | 
|------------|---------|---|---|
| No aplica | Navegadores web, herramientas de prueba (Postman, curl) | No aplica | Proyecto educativo sin métricas de uso productivo |

### 2.6 Comunicaciones asíncronas

No se identifica uso de plataformas de mensajería asíncrona como Kafka, RabbitMQ o ActiveMQ en este proyecto. La comunicación entre microservicios es síncrona mediante llamadas HTTP REST.

**TÓPICOS DE KAFKA CONSUMIDORES**

No hay información suficiente. No se utiliza Kafka en este proyecto.

| Servicio | Nombre | 
|------------|---------|
| No aplica | No aplica | 

**TÓPICOS DE KAFKA PRODUCTORES**

No hay información suficiente. No se utiliza Kafka en este proyecto.

| Servicio | Nombre | 
|------------|---------|
| No aplica | No aplica | 

### 2.7 Bases de datos

**BASE DE DATOS**
| Componente | Base de Datos | URL/Dirección completa | Tipo       | Entorno(s) | Propósito | Tablas/Colecciones | Notas (TTL e índices) |
|-------------|---------------|---------------|------------|------------|-----------|---------------------|--------|
| car-service (spring-boot+cloud) | H2 | jdbc:h2:mem:testdb | Relacional en memoria | Desarrollo | Almacenamiento temporal de datos de automóviles para demostración | Car (tabla de automóviles) | Base de datos en memoria, los datos se pierden al reiniciar |
| car-service (spring-cloud-gateway) | H2 | jdbc:h2:mem:testdb | Relacional en memoria | Desarrollo | Almacenamiento temporal de datos de automóviles | Car (tabla de automóviles) | Base de datos en memoria |
| gateway (jhipster) | PostgreSQL | jdbc:postgresql://gateway-postgresql:5432/gateway | Relacional | Desarrollo, Docker Compose | Almacenamiento de usuarios, autoridades y configuración del gateway | jhi_user, jhi_authority, jhi_user_authority, y otras tablas generadas por JHipster | Imagen Docker: postgres:11.2 |
| blog (jhipster) | PostgreSQL | jdbc:postgresql://blog-postgresql:5432/blog | Relacional | Desarrollo, Docker Compose | Almacenamiento de blogs, posts y tags | blog, post, tag, y tablas de relación | Imagen Docker: postgres:11.2 |
| store (jhipster) | MongoDB | mongodb://store-mongodb:27017/store | NoSQL (Documentos) | Desarrollo, Docker Compose | Almacenamiento de productos | products (colección de productos) | Imagen Docker: mongo:4.0.9 |
| gateway (reactive-jhipster) | PostgreSQL | r2dbc:postgresql://localhost:5432/gateway | Relacional (Acceso reactivo R2DBC) | Desarrollo | Almacenamiento reactivo de datos del gateway | Tablas JHipster (usuarios, autoridades) | Acceso reactivo con R2DBC en lugar de JDBC tradicional |
| blog (reactive-jhipster) | Neo4j | neo4j://localhost:7687 | Base de datos de grafos | Desarrollo | Almacenamiento de blogs y posts como grafos de nodos y relaciones | Nodos: Blog, Post, Tag. Relaciones entre ellos | Base de datos de grafos para modelar relaciones complejas |
| store (reactive-jhipster) | MongoDB | mongodb://localhost:27017/store | NoSQL (Documentos, acceso reactivo) | Desarrollo | Almacenamiento reactivo de productos | products (colección) | Acceso reactivo con Spring Data MongoDB Reactive |
| gateway (jhipster-k8s) | PostgreSQL | Configurado en Kubernetes Service | Relacional | Kubernetes | Almacenamiento de datos del gateway | Tablas JHipster | Desplegado como servicio en Kubernetes |
| blog (jhipster-k8s) | Neo4j | Configurado en Kubernetes Service | Base de datos de grafos | Kubernetes | Almacenamiento de blogs | Nodos de grafos | Desplegado como servicio en Kubernetes |
| store (jhipster-k8s) | MongoDB | Configurado en Kubernetes StatefulSet | NoSQL (Documentos) | Kubernetes | Almacenamiento de productos con clustering | products (colección) | Desplegado con StatefulSet para persistencia. Soporte para clustering (configurado en Kubernetes) |

---

## 3. Información adicional

### Desafíos o problemas actuales

1. **Credenciales en texto plano**: Las credenciales de Okta (client-id y client-secret) están configuradas directamente en archivos application.properties sin encriptación. Esto no es recomendable para entornos productivos. Recomendación: Utilizar variables de entorno, sistemas de gestión de secretos (como HashiCorp Vault, Azure Key Vault) o Sealed Secrets en Kubernetes.

2. **Tecnologías deprecadas**: 
   - Netflix Zuul está en modo de mantenimiento y Netflix recomienda migrar a Spring Cloud Gateway.
   - Netflix Hystrix también está deprecado y se recomienda usar Resilience4j como alternativa.
   - Estos componentes se utilizan en los ejemplos spring-boot+cloud y jhipster (no reactivo) para fines educativos.

3. **Bases de datos en memoria**: El uso de H2 en memoria en los servicios de automóviles es adecuado solo para desarrollo y demostración. No es apropiado para entornos productivos donde se requiere persistencia.

4. **Diversidad de tecnologías**: El proyecto contiene 5 arquitecturas diferentes con distintas combinaciones de tecnologías (Maven/Gradle, Zuul/Spring Cloud Gateway, blocking/reactive), lo que puede generar confusión sobre cuál es el enfoque recomendado. Esto es intencional ya que el propósito es educativo.

5. **Configuración de entornos**: Las configuraciones están optimizadas para desarrollo local. La migración a entornos corporativos requerirá ajustes significativos en:
   - URLs y endpoints de servicios
   - Configuración de bases de datos
   - Gestión de secretos
   - Configuración de redes y firewalls
   - Integración con sistemas de monitorización corporativos

6. **Dependencia de Okta**: El proyecto está fuertemente acoplado a Okta como proveedor de autenticación. La migración a otros proveedores de identidad corporativos requerirá modificaciones en la configuración.

### Notas importantes

1. **Naturaleza educativa**: Este proyecto no es una aplicación productiva, sino una colección de ejemplos de referencia para aprender arquitecturas de microservicios. No debe utilizarse tal cual en producción sin adaptaciones significativas.

2. **Múltiples ejemplos independientes**: Las 5 arquitecturas son completamente independientes entre sí. Cada una puede ejecutarse por separado. No es necesario ejecutar todos los ejemplos al mismo tiempo.

3. **Requisitos de Java 11**: Todos los componentes requieren Java 11. Esto debe tenerse en cuenta para la estrategia de migración a Azure Cloud.

4. **Integración con GitHub**: El proyecto original proviene de un repositorio público de GitHub (https://github.com/oktadev/java-microservices-examples) mantenido por Okta Developer Relations. La migración desde Bitbucket puede requerir considerar la sincronización con el repositorio original o su fork.

5. **Documentación disponible**: El proyecto incluye documentación extensa en archivos README.md y referencias a artículos de blog en developer.okta.com que explican cada ejemplo en detalle.

6. **Soporte de Kubernetes**: El ejemplo jhipster-k8s demuestra cómo desplegar microservicios en Kubernetes y puede servir como referencia para la migración a Azure Kubernetes Service (AKS).

7. **Librerías referenciadas pero no utilizadas en código activo**:
   - Keycloak: Está configurado en archivos Docker Compose como alternativa a Okta, pero los ejemplos por defecto usan Okta. Keycloak aparece en configuraciones pero puede no estar activo en todas las ejecuciones.
   - Spring Cloud Sleuth / Zipkin: Hay referencias en algunos archivos gradle (gradle/zipkin.gradle) pero no está configurado por defecto en las aplicaciones.

8. **Versiones de software**: Las versiones utilizadas (Spring Boot 2.2.5, Spring Cloud Hoxton.SR10) son de 2020-2021 y pueden requerir actualización antes de la migración a producción para incluir parches de seguridad y nuevas funcionalidades.

9. **Compatibilidad con Azure**: 
   - Las aplicaciones Spring Boot son compatibles con Azure App Service o Azure Spring Apps
   - Las configuraciones Kubernetes son compatibles con Azure Kubernetes Service (AKS)
   - Las bases de datos pueden migrarse a Azure Database for PostgreSQL, Azure Cosmos DB (para MongoDB), o bases de datos gestionadas equivalentes

10. **Estrategia de migración recomendada**: Dado que este es un proyecto educativo, la migración a GitHub y Azure Cloud podría enfocarse en:
    - Migrar el código fuente a GitHub manteniendo la estructura modular
    - Crear pipelines CI/CD en GitHub Actions
    - Desplegar el ejemplo más moderno (jhipster-k8s o reactive-jhipster) en Azure Kubernetes Service como prueba de concepto
    - Utilizar Azure Active Directory B2C como reemplazo de Okta para demostrar integración con servicios de identidad de Azure
