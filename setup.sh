#!/bin/bash

# Create directories if they don't exist
mkdir -p input output

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Copy sample citations file if input is empty
if [ ! -f "input/citations.txt" ]; then
    cp samples/citations.txt input/citations.txt
    echo "Created sample citations file in input/citations.txt"
fi

echo "Setup complete! Virtual environment is activated and dependencies are installed."
echo "A sample citations file has been placed in input/citations.txt"
