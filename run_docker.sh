#!/bin/bash
set -e

# -------------------------------
# Script to build and run Docker container safely
# with:
# ✅ Port check & mapping
# ✅ Database persistence using a local folder
#
# Key Concepts:
# - Container Port: Inside Docker (your app listens on 5000)
# - Host Port: Your machine (browser uses this port)
# - Bind Mount: Maps local ./data folder to /app/data in container
#
# After running:
#   Database file inside container (/app/data) = Host folder ./data
#   So data persists after container stops.
# -------------------------------

IMAGE_NAME="my-flask-api"
DOCKERFILE="Dockerfile"
CONTAINER_PORT=5000
HOST_PORT=${1:-5000}
DB_HOST_DIR="$(pwd)/data"
DB_CONTAINER_DIR="/app/data"

# Ensure local data folder exists
mkdir -p "$DB_HOST_DIR"

# Function: check if port is free
check_port() {
    local PORT=$1
    if lsof -i :"$PORT" > /dev/null 2>&1; then
        return 1
    else
        return 0
    fi
}

# Find free host port
while ! check_port "$HOST_PORT"; do
    echo "⚠️  Port $HOST_PORT in use. Trying next port..."
    HOST_PORT=$((HOST_PORT+1))
done

echo "✅ Using host port $HOST_PORT mapped to container port $CONTAINER_PORT."
echo "✅ Database persistence enabled: $DB_HOST_DIR ↔ $DB_CONTAINER_DIR"

# Build Docker image
echo "🔨 Building Docker image '$IMAGE_NAME'..."
docker build -t "$IMAGE_NAME" -f "$DOCKERFILE" .

# Run container with:
# - Port mapping
# - Volume for DB persistence
echo "🚀 Running container with persistent storage..."
docker run --rm \
    -p "$HOST_PORT":"$CONTAINER_PORT" \
    -v "$DB_HOST_DIR":"$DB_CONTAINER_DIR" \
    "$IMAGE_NAME"

echo "✅ Container running at: http://localhost:$HOST_PORT"
echo "📂 Database stored locally in: $DB_HOST_DIR"

