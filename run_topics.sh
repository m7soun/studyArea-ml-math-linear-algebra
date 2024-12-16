#!/bin/bash
echo "Running ML Math Topics..."
for file in topics/*.py; do
    echo "----------------------------------"
    echo "Running $file"
    python3 "$file"
    echo "----------------------------------"
done
echo "All topics executed successfully."