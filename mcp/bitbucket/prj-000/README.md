# PRJ-000 Demo Microservices

This is a demo project with 2 microservices showcasing a typical cloud-native architecture with Azure services.

## Project Overview

This project contains two Python-based microservices:

1. **Message Processor** - Handles message processing using Azure Service Bus
2. **Data API** - Provides REST API for data operations with Azure Cosmos DB

## Architecture

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

## Microservices

### 1. Message Processor
- **Purpose**: Process messages from Azure Service Bus queues
- **Port**: 8001
- **Endpoints**:
  - `GET /health` - Health check
  - `POST /send-message` - Send message to queue
  - `GET /receive-messages` - Receive messages from queue

### 2. Data API
- **Purpose**: CRUD operations for user data in Cosmos DB
- **Port**: 8002
- **Endpoints**:
  - `GET /health` - Health check
  - `GET /users` - Get all users
  - `GET /users/<id>` - Get specific user
  - `POST /users` - Create new user
  - `PUT /users/<id>` - Update user
  - `DELETE /users/<id>` - Delete user

## Configuration

The project supports two environments:

- **dev** - Development environment (config/dev.yaml)
- **pro** - Production environment (config/pro.yaml)

Each configuration file contains:
- Service-specific settings
- Azure connection strings
- Logging levels
- Port configurations

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

Optional:
- Docker and Docker Compose (for containerized deployment)

## Installation

1. Navigate to the project directory:
```bash
cd mcp/bitbucket/prj-000
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Services

### Option 1: Using Shell Scripts (Recommended)

**Development Environment:**
```bash
./run-dev.sh
```

**Production Environment:**
```bash
./run-pro.sh
```

### Option 2: Manual Execution

**Terminal 1 - Message Processor:**
```bash
export ENV=dev
cd message-processor
python app.py
```

**Terminal 2 - Data API:**
```bash
export ENV=dev
cd data-api
python app.py
```

### Option 3: Using Docker Compose

**Development Environment:**
```bash
ENV=dev docker-compose up --build
```

**Production Environment:**
```bash
ENV=pro docker-compose up --build
```

## Testing the Services

### Message Processor

**Health Check:**
```bash
curl http://localhost:8001/health
```

**Send Message:**
```bash
curl -X POST http://localhost:8001/send-message \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from demo!"}'
```

**Receive Messages:**
```bash
curl http://localhost:8001/receive-messages
```

### Data API

**Health Check:**
```bash
curl http://localhost:8002/health
```

**Get All Users:**
```bash
curl http://localhost:8002/users
```

**Get Specific User:**
```bash
curl http://localhost:8002/users/1
```

**Create User:**
```bash
curl -X POST http://localhost:8002/users \
  -H "Content-Type: application/json" \
  -d '{"id": "3", "name": "Alice Johnson", "email": "alice@example.com"}'
```

**Update User:**
```bash
curl -X PUT http://localhost:8002/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

**Delete User:**
```bash
curl -X DELETE http://localhost:8002/users/1
```

## Technologies

- **Language**: Python 3.11
- **Web Framework**: Flask 3.0.0
- **Azure Services**:
  - Azure Service Bus (azure-servicebus 7.11.4)
  - Azure Cosmos DB (azure-cosmos 4.5.1)
- **Configuration**: YAML (pyyaml 6.0.1)

## Project Structure

```
prj-000/
├── config/
│   ├── dev.yaml           # Development configuration
│   └── pro.yaml           # Production configuration
├── message-processor/
│   ├── app.py             # Message processor application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration
├── data-api/
│   ├── app.py             # Data API application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Shared dependencies
├── run-dev.sh            # Run in dev environment
├── run-pro.sh            # Run in pro environment
└── README.md             # This file
```

## Security Notes

⚠️ **Important**: This is a demo project. In production:

1. Never hardcode connection strings or keys in configuration files
2. Use Azure Key Vault or environment variables for sensitive data
3. Implement proper authentication and authorization
4. Use managed identities when possible
5. Enable encryption for data in transit and at rest
6. Implement proper logging and monitoring

## Demo Mode

The Azure service connections are currently mocked for demonstration purposes. To connect to actual Azure services:

1. Update configuration files with real connection strings
2. Uncomment the Azure client initialization code in both `app.py` files
3. Ensure proper Azure permissions are configured
4. Update environment variables with credentials from Azure Key Vault

## Future Enhancements

- Add unit and integration tests
- Implement health check monitoring
- Add API documentation (Swagger/OpenAPI)
- Implement retry logic and circuit breakers
- Add distributed tracing
- Implement proper error handling and logging
- Add CI/CD pipeline configuration
