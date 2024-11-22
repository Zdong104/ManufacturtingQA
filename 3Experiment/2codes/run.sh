#!/bin/bash

# Define the QAType values you want to run
QATypes=("2" "3" "4")

# Loop through each QAType and run the Python script with the given QAType
for QAType in "${QATypes[@]}"; do
    echo "Running main.py with --QAType $QAType..."
    python main.py --QAType "$QAType"
done

echo "All QAType runs completed."
