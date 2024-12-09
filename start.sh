#!/bin/bash

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

echo ""
echo "Starting backend"
echo ""
source .venv/bin/activate
export FLASK_APP=app.py  # Ensure the correct module is specified
python -m quart run --port=50505 --host=127.0.0.1 --reload

if [ $? -ne 0 ]; then
    echo "Failed to start backend"
    exit $?
fi