# AS-IS Document: PRJ-000 - Demo Microservices

> **Document Purpose**: This document captures the current state of the project as it exists today. It serves as a reference point for understanding what we have before planning any migrations or changes.

---

## 1. Project Information

### Project Overview
**Project Code**: PRJ-000

**Project Name**: Demo Microservices Project

**Project Description**:
This is a demonstration project that shows how modern applications are built using small, independent services that work together. The system consists of two services: one that handles message processing (like receiving and sending notifications), and another that manages user data (storing and retrieving user information). This architecture is designed to be reliable and easy to scale as the business grows.

**Main Use Cases**:
- **Message Processing**: The system can receive messages, queue them for processing, and retrieve them when needed. This is useful for handling notifications, alerts, or any asynchronous communications.
- **User Data Management**: The system provides a way to create, view, update, and delete user information, which is stored securely in a database.
- **Health Monitoring**: Both services provide health check endpoints to ensure they are running properly and can be monitored by operations teams.

### Project Team

**Current Project Owner**: [To be assigned]

**Current Technical Lead**: [To be assigned]

**Team Members**: 
This is a demonstration project for showcasing architecture patterns.

---

## 2. Technical Details

### Technologies Used

List all technologies, frameworks, and tools currently in use:

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11 | Primary programming language for building the services |
| Flask | 3.0.0 | Web framework used to create the REST APIs |
| Azure Service Bus | 7.11.4 | Cloud-based messaging system for handling message queues |
| Azure Cosmos DB | 4.5.1 | Cloud-based NoSQL database for storing user data |
| PyYAML | 6.0.1 | Configuration file management |
| Docker | Latest | Container technology for packaging and deploying services |

### Solution Architecture

**Architecture Overview**:
The system is built with a microservices approach, meaning it consists of two independent services that can operate separately but work together to provide complete functionality. The Message Processor service handles all message-related operations using Azure Service Bus, while the Data API service manages user data using Azure Cosmos DB. This separation allows each service to be updated, scaled, or maintained independently without affecting the other.

**Architecture Diagram**:
```
┌─────────────────────┐         ┌──────────────────┐
│  Message Processor  │         │    Data API      │
│   (Port 8001)       │         │   (Port 8002)    │
└──────────┬──────────┘         └────────┬─────────┘
           │                             │
           │                             │
    ┌──────▼──────┐              ┌──────▼──────┐
    │   Azure     │              │   Azure     │
    │ Service Bus │              │  Cosmos DB  │
    └─────────────┘              └─────────────┘
```

**Key Components**:
- **Message Processor (Port 8001)**: This service handles message operations. It can send messages to a queue, receive messages from the queue, and provides a health check endpoint. It connects to Azure Service Bus for message storage and processing.

- **Data API (Port 8002)**: This service provides a REST API for user data management. It supports operations like viewing all users, getting a specific user's details, creating new users, updating existing users, and deleting users. It connects to Azure Cosmos DB for data storage.

**Deployment Information**:
- **Environment(s)**: Development (dev) and Production (pro)
- **Hosting Location**: Currently designed for Azure Cloud (demo mode with mocked connections)
- **Number of Instances**: Typically 1 instance per environment in demo mode, can be scaled to multiple instances for production

---

## 3. Dependencies

This section lists all external systems, services, and resources that the project relies on to function properly.

### Databases

| Database Name | Type | Purpose | Connection Details |
|---------------|------|---------|-------------------|
| User Data Store | Azure Cosmos DB | Stores all user information including IDs, names, and email addresses | Endpoint configured in config/dev.yaml and config/pro.yaml |

### Message Queues / Event Systems

| Queue/Topic Name | System | Purpose |
|------------------|--------|---------|
| Message Queue | Azure Service Bus | Handles asynchronous message processing for the application |

### External Integrations

Currently, this is a demonstration project with no external third-party integrations beyond Azure services.

| Integration Name | Purpose | Type | Credentials Required |
|------------------|---------|------|---------------------|
| Azure Service Bus | Message queue hosting | Cloud Service | Yes - Connection String |
| Azure Cosmos DB | Database hosting | Cloud Service | Yes - Endpoint and Key |

### Other Dependencies

**Configuration Management**:
- YAML configuration files for managing environment-specific settings
- Separate configuration files for development (dev.yaml) and production (pro.yaml) environments

**Development Tools**:
- Docker for containerization
- Python pip for dependency management

---

## 4. Communication Matrix

This section documents all network communications between systems, including servers, ports, and protocols.

### Internal Communications

Communications between components within the project:

| Source Component | Destination Component | Protocol | Port | Direction | Purpose |
|------------------|----------------------|----------|------|-----------|---------|
| Message Processor | Azure Service Bus | AMQP/HTTPS | 5671/443 | Outbound | Send and receive messages from queue |
| Data API | Azure Cosmos DB | HTTPS | 443 | Outbound | Database queries and data operations |

### External Communications

Communications with external systems or services:

| Source | Destination | Protocol | Port | Direction | Purpose | Notes |
|--------|-------------|----------|------|-----------|---------|-------|
| Client Applications | Message Processor | HTTP/HTTPS | 8001 | Inbound | API requests for message operations | Health check, send/receive messages |
| Client Applications | Data API | HTTP/HTTPS | 8002 | Inbound | API requests for user data operations | CRUD operations for users |
| Message Processor | Azure Service Bus | HTTPS | 443 | Outbound | Queue operations | Requires connection string authentication |
| Data API | Azure Cosmos DB | HTTPS | 443 | Outbound | Database operations | Requires endpoint URL and access key |

### Firewall Requirements

Firewall rules that must be configured for the application to work properly:

| Rule Description | Source | Destination | Port | Protocol |
|------------------|--------|-------------|------|----------|
| Allow Message Processor API | Any (or specific IP range) | Message Processor Server | 8001 | HTTP/HTTPS |
| Allow Data API | Any (or specific IP range) | Data API Server | 8002 | HTTP/HTTPS |
| Allow Azure Service Bus | Message Processor Server | Azure Service Bus | 5671/443 | AMQP/HTTPS |
| Allow Azure Cosmos DB | Data API Server | Azure Cosmos DB | 443 | HTTPS |

---

## 5. Additional Information

### Current Challenges or Issues

**Demo Mode**: 
This project is currently in demonstration mode. The Azure service connections are mocked, meaning they simulate the behavior but don't actually connect to real Azure services. For production use, the following would need to be implemented:
- Real Azure Service Bus and Cosmos DB instances
- Proper credential management using Azure Key Vault or environment variables
- Authentication and authorization mechanisms
- Proper error handling and retry logic
- Monitoring and alerting systems

**Security Considerations**:
- Connection strings and keys should never be stored in configuration files in a real production environment
- Managed identities should be used when possible
- All data should be encrypted in transit and at rest

### Important Notes

**Future Enhancements Planned**:
- Unit and integration test coverage
- Health check monitoring integration
- API documentation using Swagger/OpenAPI
- Distributed tracing for debugging
- CI/CD pipeline implementation
- Circuit breakers and retry logic for resilience

**Configuration Files**:
- Development configuration: config/dev.yaml
- Production configuration: config/pro.yaml

---

**Document Version**: 1.0
**Last Updated**: October 12, 2024
**Updated By**: ProjectAnalysisAI System
