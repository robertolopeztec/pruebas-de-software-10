#!/usr/bin/bash

# Test all the files with the actual script
SCRIPT=$1
DIR=$2

echo "---"
echo "Testing $SCRIPT with $DIR" 
echo "---"
echo ""

for file in $DIR/*; do
    echo "- TESTING $SCRIPT ON: $file"
    python3 $SCRIPT $file
    echo '---'
    echo ''
done