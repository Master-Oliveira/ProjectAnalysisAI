#!/bin/bash

# Run both microservices in pro environment

echo "Starting microservices in PRO environment..."
export ENV=pro

# Install dependencies if needed
echo "Installing dependencies..."
pip install -r requirements.txt

# Start message-processor in background
echo "Starting message-processor on port 8001..."
cd message-processor
python app.py &
PROC1_PID=$!
cd ..

# Start data-api in background
echo "Starting data-api on port 8002..."
cd data-api
python app.py &
PROC2_PID=$!
cd ..

echo ""
echo "Both services are running!"
echo "Message Processor: http://localhost:8001/health"
echo "Data API: http://localhost:8002/health"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for both processes
wait $PROC1_PID $PROC2_PID
