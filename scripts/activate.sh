#!/bin/bash

# Script to activate Poetry environment based on version

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Error: Poetry is not installed or not in PATH"
    echo "Please install Poetry: https://python-poetry.org/docs/#installation"
    exit 1
fi

# Get Poetry version
POETRY_VERSION=$(poetry --version | awk '{print $3}')
MAJOR_VERSION=$(echo $POETRY_VERSION | cut -d. -f1)
MINOR_VERSION=$(echo $POETRY_VERSION | cut -d. -f2)

echo "Detected Poetry version: $POETRY_VERSION"

# Activate based on version (< 2.0 uses 'shell', >= 2.0 uses 'env activate')
if [ "$MAJOR_VERSION" -lt 2 ]; then
    echo "Using 'poetry shell' for Poetry < 2.0"
    poetry shell
else
    echo "Using 'poetry env activate' for Poetry >= 2.0"
    poetry env activate
fi

echo "Poetry environment activated. You can now run commands with 'poetry run poe <command>'"
echo "Examples:"
echo "  poetry run poe local-infrastructure-up    - Start local infrastructure"
echo "  poetry run poe local-infrastructure-down  - Stop local infrastructure" 