"""
Message Processor Microservice
Processes messages from Azure Service Bus
"""
import os
import yaml
import logging
from flask import Flask, jsonify, request
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)

# Load configuration
config_env = os.getenv('ENV', 'dev')
config_path = f'../config/{config_env}.yaml'

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# Configure logging
log_level = config['message-processor']['log_level']
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger(__name__)

# Service Bus configuration
service_bus_config = config['message-processor']['service_bus']
connection_string = service_bus_config['connection_string']
queue_name = service_bus_config['queue_name']

# Note: In production, use environment variables for sensitive data
# This is a demo showing the structure

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'message-processor',
        'environment': config_env
    }), 200

@app.route('/send-message', methods=['POST'])
def send_message():
    """Send a message to Service Bus queue"""
    try:
        data = request.json
        message_content = data.get('message', '')
        
        logger.info(f"Sending message to queue: {queue_name}")
        
        # Simulate sending message to Service Bus
        # In production, uncomment the following:
        # with ServiceBusClient.from_connection_string(connection_string) as client:
        #     with client.get_queue_sender(queue_name) as sender:
        #         message = ServiceBusMessage(message_content)
        #         sender.send_messages(message)
        
        logger.info(f"Message sent successfully: {message_content}")
        
        return jsonify({
            'status': 'success',
            'message': 'Message sent to Service Bus',
            'queue': queue_name
        }), 200
        
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/receive-messages', methods=['GET'])
def receive_messages():
    """Receive messages from Service Bus queue"""
    try:
        logger.info(f"Receiving messages from queue: {queue_name}")
        
        # Simulate receiving messages from Service Bus
        # In production, uncomment the following:
        # messages = []
        # with ServiceBusClient.from_connection_string(connection_string) as client:
        #     with client.get_queue_receiver(queue_name) as receiver:
        #         received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
        #         for msg in received_msgs:
        #             messages.append(str(msg))
        #             receiver.complete_message(msg)
        
        # Demo response
        messages = ["Demo message 1", "Demo message 2"]
        
        logger.info(f"Received {len(messages)} messages")
        
        return jsonify({
            'status': 'success',
            'message_count': len(messages),
            'messages': messages
        }), 200
        
    except Exception as e:
        logger.error(f"Error receiving messages: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    port = config['message-processor']['port']
    logger.info(f"Starting message-processor on port {port} in {config_env} environment")
    app.run(host='0.0.0.0', port=port, debug=(config_env == 'dev'))
