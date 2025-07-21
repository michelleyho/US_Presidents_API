# Use official Python 3.11 image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional, needed for some packages)
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# Create persistent data directory
RUN mkdir -p /app/data

# Copy requirements file first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run the app (using uvicorn)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

