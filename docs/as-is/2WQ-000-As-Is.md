# AS-IS Document: 2WQ-000 - Demo para Cesar

> **Document Purpose**: This document captures the current state of the project as it exists today. It serves as a reference point for understanding what we have before planning any migrations or changes.

---

## 1. Project Information

### Project Overview
**Project Code**: 2WQ-000

**Project Name**: Demo para Cesar

**Project Description**:
This is a demonstration project that showcases modern microservices architecture using JHipster 7. The system demonstrates how to build cloud-native, reactive applications with a microservice architecture pattern. It consists of three main services: a Gateway that acts as the entry point for all client requests, a Blog service for managing blog posts and tags, and a Store service for managing products. These services work together to provide a complete e-commerce and blogging platform that can scale independently based on demand.

**Main Use Cases**:
- **API Gateway**: The gateway serves as the central entry point, routing requests to appropriate microservices, handling authentication, and providing a unified interface for client applications. It includes a Vue.js web interface for user interactions.
- **Blog Management**: The blog service allows users to create, read, update, and delete blog posts, tags, and blog entries. This demonstrates content management capabilities in a microservices environment.
- **Product Catalog**: The store service manages product information, allowing users to browse and manage product data. This showcases how to handle different data storage needs across microservices.

### Project Team

**Current Project Owner**: To be assigned

**Current Technical Lead**: To be assigned

**Team Members**: 
This is a demonstration project for showcasing JHipster 7 microservices architecture patterns.

---

## 2. Technical Details

### Technologies Used

List all technologies, frameworks, and tools currently in use:

| Technology | Version | Purpose |
|------------|---------|---------|
| Java | 11 | Primary programming language for all microservices |
| JHipster | 7.0.1 | Full-stack development platform for generating microservices |
| Spring Boot | 2.4.4 | Framework for building production-ready applications |
| Spring Cloud | 2020.x | Provides tools for building distributed systems and microservices |
| Spring Cloud Gateway | Latest | API Gateway for routing and filtering requests |
| Spring WebFlux | Latest | Reactive web framework for building non-blocking applications |
| Gradle | Latest | Build automation tool |
| PostgreSQL | 13.2 | Relational database for Gateway service |
| MongoDB | Latest | NoSQL database for Store service (clustered) |
| Neo4j | 4.2.4 | Graph database for Blog service |
| Eureka Server | Latest | Service discovery and registry |
| OAuth2/OIDC | Latest | Authentication and authorization protocol |
| Keycloak | Latest | Identity and access management solution |
| Docker | Latest | Container platform for packaging applications |
| Kubernetes | Latest | Container orchestration platform |
| Vue.js | 3.x | Frontend framework for Gateway UI |
| JIB | 2.8.0 | Container image builder for Java applications |

### Solution Architecture

**Architecture Overview**:
The system follows a reactive microservices architecture pattern where all services are built using reactive programming principles for better scalability and resource utilization. The Gateway service acts as the single entry point, authenticating users and routing requests to the appropriate microservices. Each microservice is responsible for its own data storage and uses different database technologies optimized for their specific needs - PostgreSQL for structured data in the Gateway, MongoDB for flexible product data in the Store, and Neo4j for relationship-rich blog content.

All services register themselves with a Eureka service registry, enabling dynamic service discovery. Configuration is centralized through Spring Cloud Config, allowing for consistent settings across all services. The system uses OAuth2 and OpenID Connect for secure authentication, with Keycloak managing user identities and access control. The architecture is designed to be deployed on Kubernetes, supporting horizontal scaling and cloud-native operations.

**Architecture Diagram**:
```
┌─────────────────────────────────────────────────────────────┐
│                    Client Applications                        │
│                     (Web Browsers)                           │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS (8080)
                         ▼
┌────────────────────────────────────────────────────────────┐
│                    API Gateway                              │
│                  (Spring Cloud Gateway)                      │
│                   Port: 8080                                │
│                   UI: Vue.js                                │
└──────┬──────────────────┬──────────────────────┬───────────┘
       │                  │                      │
       │                  │                      │
       ▼                  ▼                      ▼
┌─────────────┐    ┌─────────────┐      ┌─────────────┐
│   Blog      │    │   Store     │      │  Eureka     │
│ Service     │    │  Service    │      │  Registry   │
│ Port: 8081  │    │ Port: 8082  │      │ Port: 8761  │
└──────┬──────┘    └──────┬──────┘      └─────────────┘
       │                  │                      │
       │                  │                      │
       ▼                  ▼                      ▼
┌─────────────┐    ┌─────────────┐      ┌─────────────┐
│   Neo4j     │    │  MongoDB    │      │Spring Cloud │
│  Database   │    │  (Cluster)  │      │   Config    │
│ Port: 7687  │    │ Port: 27017 │      └─────────────┘
└─────────────┘    └─────────────┘
                                                 │
       ┌─────────────────────────────────────────┘
       │
       ▼
┌─────────────┐         ┌─────────────┐
│PostgreSQL   │         │  Keycloak   │
│  Database   │         │   (Auth)    │
│ Port: 5432  │         │ Port: 9080  │
└─────────────┘         └─────────────┘
```

**Key Components**:
- **API Gateway (Port 8080)**: The central entry point for all client requests. Built with Spring Cloud Gateway and Spring WebFlux for reactive, non-blocking request handling. Includes a Vue.js single-page application for the user interface. Handles authentication, authorization, and routing to microservices. Connected to PostgreSQL database for storing gateway-specific data.

- **Blog Service (Port 8081)**: A reactive microservice managing blog-related entities including blogs, posts, and tags. Uses Neo4j graph database to efficiently handle relationships between blog entities. Designed to handle complex content relationships and hierarchies.

- **Store Service (Port 8082)**: A reactive microservice for product catalog management. Uses MongoDB with clustering support (3 peer nodes) for high availability and scalability. Handles product information with flexible schema support.

- **Eureka Registry (Port 8761)**: Netflix Eureka-based service discovery server. All microservices register themselves here, enabling dynamic service discovery and load balancing without hardcoded service locations.

- **Spring Cloud Config**: Centralized configuration management system. Stores and distributes configuration to all microservices, ensuring consistent settings across the environment.

- **Keycloak (Port 9080)**: Identity and access management server. Handles user authentication, authorization, and manages OAuth2/OIDC flows. Pre-configured with JHipster realm and user groups.

**Deployment Information**:
- **Environment(s)**: Development and Production profiles supported
- **Hosting Location**: Designed for Kubernetes deployment on cloud platforms (Google Cloud GKE demonstrated). Can run locally using Docker Compose or Minikube.
- **Number of Instances**: 
  - Gateway: 1 instance (scalable)
  - Blog: 1 instance (scalable)
  - Store: 1 instance with 3 MongoDB replicas
  - Supporting services: 1 instance each for development
- **Container Registry**: Docker Hub (images: mraible/gateway, mraible/blog, mraible/store)

---

## 3. Dependencies

This section lists all external systems, services, and resources that the project relies on to function properly.

### Databases

| Database Name | Type | Purpose | Connection Details |
|---------------|------|---------|-------------------|
| Gateway PostgreSQL | PostgreSQL 13.2 | Stores gateway service data, user sessions, and application state | JDBC: jdbc:postgresql://gateway-postgresql:5432/gateway, R2DBC: r2dbc:postgresql://gateway-postgresql:5432/gateway |
| Blog Neo4j | Neo4j 4.2.4 | Graph database storing blog posts, tags, and their relationships | Bolt: bolt://blog-neo4j:7687, No authentication in dev mode |
| Store MongoDB | MongoDB (Clustered) | Document database for product catalog with 3-node replica set | Connection string configured per environment, Port: 27017 |

### Message Queues / Event Systems

Currently, this project does not use message queues. The architecture uses synchronous REST API communication between services through the API Gateway.

| Queue/Topic Name | System | Purpose |
|------------------|--------|---------|
| N/A | N/A | No message queue system currently implemented |

### External Integrations

List any third-party services or external systems the project connects to:

| Integration Name | Purpose | Type | Credentials Required |
|------------------|---------|------|---------------------|
| Keycloak | Identity and access management, OAuth2 authentication provider | Authentication Server (HTTP) | Yes - Client ID and Client Secret per service |
| Okta (Optional) | Alternative OAuth2/OIDC provider for production deployments | Cloud Authentication Service | Yes - Client ID, Client Secret, Issuer URI |
| Docker Hub | Container image repository for storing and distributing Docker images | Container Registry | Yes - Docker Hub credentials |
| Eureka Service Registry | Service discovery and registration for microservices | Service Registry | Yes - Registry admin password |

### Other Dependencies

**Service Discovery**:
- Eureka Server for service registration and discovery
- Each microservice registers automatically on startup
- Health checks and heartbeat monitoring enabled

**Configuration Management**:
- Spring Cloud Config Server integrated with JHipster Registry
- Configuration files stored in `docker-compose/central-server-config/` directory
- Environment-specific configurations (dev, prod, kubernetes profiles)

**Build and Development Tools**:
- Gradle build system with wrapper
- JIB for building containerized images without Docker daemon
- Node.js and npm for frontend build (Gateway only)
- Liquibase for database migrations (Gateway and Blog)

**Monitoring and Observability**:
- Prometheus metrics export enabled on all services
- Management endpoints exposed for health checks
- Optional Zipkin integration for distributed tracing

**Security**:
- OAuth2/OIDC authentication across all services
- JWT token-based authorization
- Spring Security for endpoint protection
- Client credentials flow for service-to-service communication

---

## 4. Communication Matrix

This section documents all network communications between systems, including servers, ports, and protocols.

### Internal Communications

Communications between components within the project:

| Source Component | Destination Component | Protocol | Port | Direction | Purpose |
|------------------|----------------------|----------|------|-----------|---------|
| Gateway | Eureka Registry | HTTP | 8761 | Outbound | Service registration and discovery |
| Gateway | Spring Cloud Config | HTTP | 8761 | Outbound | Fetch centralized configuration |
| Gateway | PostgreSQL Database | R2DBC/TCP | 5432 | Outbound | Reactive database queries and transactions |
| Gateway | Keycloak | HTTP | 9080 | Outbound | OAuth2 token validation and user authentication |
| Gateway | Blog Service | HTTP | 8081 | Outbound | Proxy blog-related API requests |
| Gateway | Store Service | HTTP | 8082 | Outbound | Proxy store-related API requests |
| Blog Service | Eureka Registry | HTTP | 8761 | Outbound | Service registration and discovery |
| Blog Service | Spring Cloud Config | HTTP | 8761 | Outbound | Fetch centralized configuration |
| Blog Service | Neo4j Database | Bolt | 7687 | Outbound | Graph database queries for blog data |
| Blog Service | Keycloak | HTTP | 9080 | Outbound | OAuth2 token validation |
| Store Service | Eureka Registry | HTTP | 8761 | Outbound | Service registration and discovery |
| Store Service | Spring Cloud Config | HTTP | 8761 | Outbound | Fetch centralized configuration |
| Store Service | MongoDB Cluster | MongoDB Protocol | 27017 | Outbound | Document database operations |
| Store Service | Keycloak | HTTP | 9080 | Outbound | OAuth2 token validation |

### External Communications

Communications with external systems or services:

| Source | Destination | Protocol | Port | Direction | Purpose | Notes |
|--------|-------------|----------|------|-----------|---------|-------|
| Client Applications | Gateway | HTTP/HTTPS | 8080 | Inbound | User interface access and API requests | Main entry point for all external traffic |
| Administrators | Eureka Registry | HTTP/HTTPS | 8761 | Inbound | Monitor service health and registrations | Requires OAuth2 authentication |
| Gateway | Okta (Optional) | HTTPS | 443 | Outbound | OAuth2 authentication (production) | Alternative to Keycloak for production |
| Build System | Docker Hub | HTTPS | 443 | Outbound | Push/pull container images | Required for image distribution |
| Kubernetes Cluster | Container Registry | HTTPS | 443 | Outbound | Pull container images for deployment | Can be Docker Hub or private registry |

### Firewall Requirements

Firewall rules that must be configured for the application to work properly:

| Rule Description | Source | Destination | Port | Protocol |
|------------------|--------|-------------|------|----------|
| Allow Gateway API Access | Client Networks/Internet | Gateway Server | 8080 | HTTP/HTTPS |
| Allow Registry Admin Access | Administrator Networks | Eureka Registry | 8761 | HTTP/HTTPS |
| Allow Gateway to PostgreSQL | Gateway Server | PostgreSQL Server | 5432 | TCP |
| Allow Blog to Neo4j | Blog Service Server | Neo4j Server | 7687 | TCP (Bolt) |
| Allow Store to MongoDB | Store Service Server | MongoDB Cluster | 27017 | TCP |
| Allow Services to Eureka | All Microservices | Eureka Registry | 8761 | HTTP |
| Allow Services to Keycloak | All Microservices | Keycloak Server | 9080 | HTTP |
| Allow Gateway to Microservices | Gateway Server | Blog & Store Services | 8081, 8082 | HTTP |
| Allow Kubernetes API Access | Kubernetes Cluster | Pod Network | Various | TCP |
| Allow Container Image Pull | Kubernetes Nodes | Docker Hub/Registry | 443 | HTTPS |

### Kubernetes-Specific Requirements

When deployed on Kubernetes, additional networking considerations:

| Rule Description | Source | Destination | Port | Protocol |
|------------------|--------|-------------|------|----------|
| LoadBalancer Service | External Traffic | Gateway Service | 8080 | HTTP/HTTPS |
| Service Discovery | Pods | Kubernetes DNS | 53 | UDP/TCP |
| Pod-to-Pod Communication | All Pods | Pod Network | Various | TCP |
| Health Check Probes | Kubelet | All Pods | Various | HTTP |

---

## 5. Additional Information

### Current Challenges or Issues

**Demonstration Environment**:
This project is currently configured as a demonstration of JHipster 7 capabilities and microservices architecture patterns. Key considerations for moving to production:

- **Authentication Configuration**: Currently configured with Keycloak for development. For production, integration with Okta or enterprise identity providers is supported and recommended.
- **Database Security**: Development environments use simplified authentication (Neo4j without authentication, PostgreSQL with trust mode). Production deployments require proper authentication, encryption, and access controls.
- **Secret Management**: Connection strings and credentials are currently stored in configuration files. Production deployments should use Kubernetes secrets, sealed secrets, or cloud-native secret management services.
- **Resource Limits**: Container resource limits need to be tuned based on actual production load patterns.
- **High Availability**: Current development setup runs single instances. Production should implement:
  - Multiple instances of Gateway, Blog, and Store services
  - Database replication and backups
  - Redis or Hazelcast caching layer for session management
  - Circuit breakers and retry logic for resilience

**Technology Considerations**:
- **Reactive Programming**: All services use Spring WebFlux and reactive programming models, which requires understanding of reactive patterns for developers.
- **Complex Architecture**: Microservices architecture adds operational complexity compared to monolithic applications. Requires expertise in distributed systems, service mesh, and observability.
- **Multiple Databases**: Managing three different database technologies (PostgreSQL, MongoDB, Neo4j) increases operational overhead and requires specialized knowledge.

### Important Notes

**Architecture Patterns Demonstrated**:
- Reactive microservices with Spring WebFlux
- Service discovery with Netflix Eureka
- Centralized configuration with Spring Cloud Config
- API Gateway pattern with Spring Cloud Gateway
- OAuth2/OIDC authentication
- Database per service pattern
- Container-based deployment
- Kubernetes orchestration

**Deployment Options**:
The project supports multiple deployment strategies:
1. **Local Development**: Docker Compose for running all services on a development machine
2. **Local Kubernetes**: Minikube for testing Kubernetes deployments locally
3. **Cloud Kubernetes**: Google Cloud GKE, Azure AKS, or AWS EKS for production deployments
4. **Service Mesh**: Ready for Istio integration if advanced traffic management is needed

**Configuration Files**:
- Gateway configuration: `gateway/.yo-rc.json`, `gateway/gradle.properties`
- Blog configuration: `blog/.yo-rc.json`, `blog/gradle.properties`
- Store configuration: `store/.yo-rc.json`, `store/gradle.properties`
- Docker Compose: `docker-compose/docker-compose.yml`
- Kubernetes manifests: `k8s/` directory
- Central config: `docker-compose/central-server-config/application.yml`

**Entity Models**:
- Gateway manages: Tag, Product, Blog, Post (as entities proxied to microservices)
- Blog service manages: Tag, Blog, Post entities
- Store service manages: Product entity

**Testing**:
- Gateway includes Cypress end-to-end tests
- All services configured for JUnit testing
- JaCoCo code coverage enabled
- SonarQube integration for code quality

**Source Code Location**:
This is a clone/fork of the oktadev/java-microservices-examples repository, specifically the jhipster-k8s example. Original source demonstrates best practices for JHipster 7 microservices with Kubernetes deployment.

---

**Document Version**: 1.0
**Last Updated**: October 16, 2025
**Updated By**: ProjectAnalysisAI System
