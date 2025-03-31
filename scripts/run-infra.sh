#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Get the project root directory (parent of scripts directory)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# Export the required environment variable for MacOS
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# Function to display usage
show_usage() {
    echo "Usage: ./scripts/run-infra.sh [up|down|status|api]"
    echo ""
    echo "Commands:"
    echo "  up      Start local infrastructure (MongoDB, Qdrant, ZenML)"
    echo "  down    Stop local infrastructure"
    echo "  status  Check status of services"
    echo "  api     Start the inference API service"
    echo ""
    exit 1
}

# Function to check if services are running
check_status() {
    echo "Checking services status..."
    
    # Check MongoDB
    if nc -z localhost 27017 2>/dev/null; then
        echo "✅ MongoDB is running"
    else
        echo "❌ MongoDB is not running"
    fi
    
    # Check Qdrant
    if nc -z localhost 6333 2>/dev/null; then
        echo "✅ Qdrant is running"
    else
        echo "❌ Qdrant is not running"
    fi
    
    # Check ZenML
    if nc -z localhost 8237 2>/dev/null; then
        echo "✅ ZenML is running"
    else
        echo "❌ ZenML is not running"
    fi
}

# Change to project root directory
cd "$PROJECT_ROOT"

# Check if command is provided
if [ $# -eq 0 ]; then
    show_usage
fi

# Handle commands
case "$1" in
    up)
        echo "Starting local infrastructure from $PROJECT_ROOT..."
        poetry run poe local-infrastructure-up
        ;;
    down)
        echo "Stopping local infrastructure from $PROJECT_ROOT..."
        poetry run poe local-infrastructure-down
        ;;
    status)
        check_status
        ;;
    api)
        echo "Starting inference API service from $PROJECT_ROOT..."
        poetry run poe run-inference-ml-service
        ;;
    *)
        show_usage
        ;;
esac 