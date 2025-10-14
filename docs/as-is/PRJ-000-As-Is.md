# PRJ-000 Demo Microservices - As-Is Documentation

## 1. Project Information

### Project Details
- **Project Code**: PRJ-000
- **Project Name**: Demo Microservices
- **Current Repository Location**: Bitbucket
- **Current Project Owner**: To be determined
- **Current Tech Lead**: To be determined

### Project Description
This is a demo project showcasing a typical cloud-native architecture with Azure services. The project consists of 2 Python-based microservices that demonstrate common patterns for building cloud applications.

#### Purpose
The project serves as a demonstration of:
- Microservices architecture
- Integration with Azure cloud services
- Message-based communication patterns
- RESTful API design
- Containerized deployment

#### Main Use Cases
1. **Message Processing**: Handle asynchronous message processing using Azure Service Bus queues
2. **Data Operations**: Provide REST API for CRUD operations on user data stored in Azure Cosmos DB
3. **Cloud Integration**: Demonstrate integration patterns with Azure cloud services

## 2. Technical Details

### Technologies Used

#### Programming Language
- **Python 3.11** - Core programming language for both microservices

#### Web Framework
- **Flask 3.0.0** - Lightweight web framework for building REST APIs

#### Azure Cloud Services
- **Azure Service Bus 7.11.4** - Message broker for asynchronous communication
- **Azure Cosmos DB 4.5.1** - NoSQL database for data storage

#### Configuration Management
- **PyYAML 6.0.1** - YAML configuration file handling

#### Containerization
- **Docker** - Container platform for packaging applications
- **Docker Compose** - Multi-container orchestration

### Solution Architecture

The system consists of two independent microservices:

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

#### Microservice 1: Message Processor
- **Purpose**: Process messages from Azure Service Bus queues
- **Port**: 8001
- **Key Endpoints**:
  - `GET /health` - Health check endpoint
  - `POST /send-message` - Send message to queue
  - `GET /receive-messages` - Receive messages from queue
- **Technologies**: Python 3.11, Flask 3.0.0, Azure Service Bus 7.11.4

#### Microservice 2: Data API
- **Purpose**: CRUD operations for user data in Cosmos DB
- **Port**: 8002
- **Key Endpoints**:
  - `GET /health` - Health check endpoint
  - `GET /users` - Get all users
  - `GET /users/<id>` - Get specific user
  - `POST /users` - Create new user
  - `PUT /users/<id>` - Update user
  - `DELETE /users/<id>` - Delete user
- **Technologies**: Python 3.11, Flask 3.0.0, Azure Cosmos DB 4.5.1

### Environment Configuration

The project supports two environments:

#### Development Environment (dev)
- Configuration file: `config/dev.yaml`
- Service Bus endpoint: `sb://dev-servicebus.servicebus.windows.net/`
- Queue name: `dev-messages-queue`
- Cosmos DB endpoint: `https://dev-cosmosdb.documents.azure.com:443/`
- Database name: `dev-database`
- Container name: `users`
- Logging level: DEBUG
- Message Processor port: 8001
- Data API port: 8002

#### Production Environment (pro)
- Configuration file: `config/pro.yaml`
- Service Bus endpoint: `sb://pro-servicebus.servicebus.windows.net/`
- Queue name: `pro-messages-queue`
- Cosmos DB endpoint: `https://pro-cosmosdb.documents.azure.com:443/`
- Database name: `pro-database`
- Container name: `users`
- Logging level: INFO
- Message Processor port: 8001
- Data API port: 8002

### Deployment Options

The project supports three deployment approaches:

1. **Shell Scripts**: `run-dev.sh` and `run-pro.sh` for quick local deployment
2. **Manual Execution**: Individual service startup using Python directly
3. **Docker Compose**: Containerized deployment with `docker-compose.yml`

## 3. Dependencies

### External Service Dependencies

#### Azure Service Bus
- **Type**: Message Broker / Queue Service
- **Purpose**: Asynchronous message processing
- **Used By**: Message Processor microservice
- **Connection Type**: Connection string with shared access key
- **Queue Configuration**:
  - Development: `dev-messages-queue`
  - Production: `pro-messages-queue`
- **SDK Version**: azure-servicebus 7.11.4

#### Azure Cosmos DB
- **Type**: NoSQL Database
- **Purpose**: User data storage and retrieval
- **Used By**: Data API microservice
- **Connection Type**: Endpoint URL with access key
- **Database Structure**:
  - Development database: `dev-database`
  - Production database: `pro-database`
  - Container: `users`
- **SDK Version**: azure-cosmos 4.5.1

### Python Package Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| flask | 3.0.0 | Web framework for REST APIs |
| azure-servicebus | 7.11.4 | Azure Service Bus SDK |
| azure-cosmos | 4.5.1 | Azure Cosmos DB SDK |
| pyyaml | 6.0.1 | YAML configuration parsing |

### Infrastructure Dependencies

- **Python Runtime**: Python 3.11 or higher
- **Package Manager**: pip (Python package installer)
- **Container Platform**: Docker (optional)
- **Orchestration**: Docker Compose (optional)

## 4. Communication Matrix

### Internal Service Communication

| Source Service | Destination | Port | Protocol | Purpose |
|----------------|-------------|------|----------|---------|
| Message Processor | Message Processor | 8001 | HTTP | REST API endpoints |
| Data API | Data API | 8002 | HTTP | REST API endpoints |

### External Service Communication

#### Message Processor Service

| Source | Destination | Port | Protocol | Purpose | Environment |
|--------|-------------|------|----------|---------|-------------|
| Message Processor | Azure Service Bus (dev) | 5671 | AMQP | Send/receive messages | Development |
| Message Processor | Azure Service Bus (pro) | 5671 | AMQP | Send/receive messages | Production |

**Service Bus Details:**
- Development Endpoint: `sb://dev-servicebus.servicebus.windows.net/`
- Production Endpoint: `sb://pro-servicebus.servicebus.windows.net/`
- Queue Names: `dev-messages-queue` (dev), `pro-messages-queue` (pro)

#### Data API Service

| Source | Destination | Port | Protocol | Purpose | Environment |
|--------|-------------|------|----------|---------|-------------|
| Data API | Azure Cosmos DB (dev) | 443 | HTTPS | Database operations | Development |
| Data API | Azure Cosmos DB (pro) | 443 | HTTPS | Database operations | Production |

**Cosmos DB Details:**
- Development Endpoint: `https://dev-cosmosdb.documents.azure.com:443/`
- Production Endpoint: `https://pro-cosmosdb.documents.azure.com:443/`
- Database Names: `dev-database` (dev), `pro-database` (pro)
- Container: `users`

### Client Access

| Source | Destination Service | Port | Protocol | Purpose |
|--------|-------------------|------|----------|---------|
| External Clients | Message Processor | 8001 | HTTP | Message processing operations |
| External Clients | Data API | 8002 | HTTP | User data CRUD operations |

### Network Configuration

When deployed using Docker Compose, both services communicate over a bridge network named `prj-network`. This allows container-to-container communication using service names as hostnames.

## 5. Security Considerations

### Current Security Status

⚠️ **Note**: This is a demo project with mocked Azure connections. The following security considerations are documented for future production deployment:

#### Identified Security Gaps
1. Connection strings and keys are currently stored in configuration files (demo mode)
2. No authentication or authorization implemented on REST endpoints
3. Azure service connections are mocked and not functional
4. No encryption configuration for data in transit (beyond HTTPS to Azure)

#### Recommended Security Enhancements
1. Store sensitive data (connection strings, keys) in Azure Key Vault
2. Use environment variables for configuration instead of hardcoded values
3. Implement proper authentication and authorization for REST APIs
4. Use Azure Managed Identities for service-to-service authentication
5. Enable encryption for data at rest and in transit
6. Implement proper logging and monitoring with sensitive data masking
7. Add rate limiting and throttling to REST endpoints

## 6. Project Structure

```
prj-000/
├── config/
│   ├── dev.yaml           # Development environment configuration
│   └── pro.yaml           # Production environment configuration
├── message-processor/
│   ├── app.py             # Message processor application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration
├── data-api/
│   ├── app.py             # Data API application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration
├── docker-compose.yml     # Docker Compose orchestration
├── requirements.txt       # Shared dependencies
├── run-dev.sh            # Development environment startup script
├── run-pro.sh            # Production environment startup script
└── README.md             # Project documentation
```

## 7. Known Issues and Limitations

### Current Limitations
1. **Demo Mode**: Azure services are mocked; actual cloud connections are commented out
2. **No Testing**: No unit tests or integration tests implemented
3. **No CI/CD**: No continuous integration or deployment pipeline configured
4. **Limited Error Handling**: Basic error handling without retry logic or circuit breakers
5. **No Monitoring**: No health check monitoring or distributed tracing implemented
6. **No API Documentation**: No Swagger/OpenAPI specification available
7. **Security**: See Section 5 for security considerations

### Future Enhancements Needed
- Add comprehensive unit and integration tests
- Implement health check monitoring
- Add API documentation (Swagger/OpenAPI)
- Implement retry logic and circuit breakers
- Add distributed tracing
- Improve error handling and logging
- Add CI/CD pipeline configuration
- Implement proper security measures for production deployment

---

**Document Version**: 1.0  
**Last Updated**: 2025-10-12  
**Status**: Current State (As-Is)
