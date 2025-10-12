"""
Data API Microservice
Interacts with Azure Cosmos DB
"""
import os
import yaml
import logging
from flask import Flask, jsonify, request
from azure.cosmos import CosmosClient, exceptions

app = Flask(__name__)

# Load configuration
config_env = os.getenv('ENV', 'dev')
config_path = f'../config/{config_env}.yaml'

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# Configure logging
log_level = config['data-api']['log_level']
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger(__name__)

# Cosmos DB configuration
cosmos_config = config['data-api']['cosmos_db']
endpoint = cosmos_config['endpoint']
key = cosmos_config['key']
database_name = cosmos_config['database_name']
container_name = cosmos_config['container_name']

# Note: In production, use environment variables for sensitive data
# This is a demo showing the structure

# Initialize Cosmos client (commented for demo)
# client = CosmosClient(endpoint, key)
# database = client.get_database_client(database_name)
# container = database.get_container_client(container_name)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'data-api',
        'environment': config_env
    }), 200

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users from Cosmos DB"""
    try:
        logger.info("Fetching users from Cosmos DB")
        
        # Simulate querying Cosmos DB
        # In production, uncomment the following:
        # users = []
        # query = "SELECT * FROM c"
        # items = container.query_items(query=query, enable_cross_partition_query=True)
        # for item in items:
        #     users.append(item)
        
        # Demo response
        users = [
            {'id': '1', 'name': 'John Doe', 'email': 'john@example.com'},
            {'id': '2', 'name': 'Jane Smith', 'email': 'jane@example.com'}
        ]
        
        logger.info(f"Retrieved {len(users)} users")
        
        return jsonify({
            'status': 'success',
            'count': len(users),
            'users': users
        }), 200
        
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    try:
        logger.info(f"Fetching user with ID: {user_id}")
        
        # Simulate reading from Cosmos DB
        # In production, uncomment the following:
        # user = container.read_item(item=user_id, partition_key=user_id)
        
        # Demo response
        user = {'id': user_id, 'name': 'John Doe', 'email': 'john@example.com'}
        
        logger.info(f"User found: {user['name']}")
        
        return jsonify({
            'status': 'success',
            'user': user
        }), 200
        
    except Exception as e:
        logger.error(f"Error fetching user: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user in Cosmos DB"""
    try:
        data = request.json
        logger.info(f"Creating user: {data.get('name')}")
        
        # Simulate creating in Cosmos DB
        # In production, uncomment the following:
        # user = {
        #     'id': data.get('id'),
        #     'name': data.get('name'),
        #     'email': data.get('email')
        # }
        # container.create_item(body=user)
        
        logger.info("User created successfully")
        
        return jsonify({
            'status': 'success',
            'message': 'User created',
            'user': data
        }), 201
        
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    try:
        data = request.json
        logger.info(f"Updating user: {user_id}")
        
        # Simulate updating in Cosmos DB
        # In production, uncomment the following:
        # user = container.read_item(item=user_id, partition_key=user_id)
        # user.update(data)
        # container.replace_item(item=user_id, body=user)
        
        logger.info("User updated successfully")
        
        return jsonify({
            'status': 'success',
            'message': 'User updated',
            'user_id': user_id
        }), 200
        
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    try:
        logger.info(f"Deleting user: {user_id}")
        
        # Simulate deleting from Cosmos DB
        # In production, uncomment the following:
        # container.delete_item(item=user_id, partition_key=user_id)
        
        logger.info("User deleted successfully")
        
        return jsonify({
            'status': 'success',
            'message': 'User deleted',
            'user_id': user_id
        }), 200
        
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    port = config['data-api']['port']
    logger.info(f"Starting data-api on port {port} in {config_env} environment")
    app.run(host='0.0.0.0', port=port, debug=(config_env == 'dev'))
