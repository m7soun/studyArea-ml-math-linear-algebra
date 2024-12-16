#!/bin/bash
echo "Setting up the environment..."
source venv/bin/activate

echo "Running ML Math Topics..."
for file in topics/*.py; do
    echo "----------------------------------"
    echo "Running $file"
    python3 "$file"
    echo "----------------------------------"
done

echo "Deactivating environment..."
deactivate
echo "All topics executed successfully."