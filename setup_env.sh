#!/bin/bash
set -e

echo "Removing old virtual environment (if exists)..."
rm -rf env

echo "Creating new virtual environment..."
python3 -m venv env

echo "Activating virtual environment..."
source env/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing packages with pinned versions..."
pip install -r requirements.txt

echo "Verifying installed versions..."
pip list | grep -E "Flask|connexion|marshmallow|uvicorn|SQLAlchemy"

echo "Setup complete! Your environment is ready."

