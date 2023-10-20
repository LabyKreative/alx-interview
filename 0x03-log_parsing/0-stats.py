#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:"""
import sys
import re

# Initialize variables to store metrics
total_size = 0
status_code_count = {}

# Define a regular expression pattern to match the input format
pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

# Define a function to print metrics
def print_metrics():
    print(f"File size: {total_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

try:
    line_count = 0
    for line in sys.stdin:
        # Try to match the input line with the pattern
        match = re.match(pattern, line)
        if match:
            # Extract data from the matched line
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update metrics
            total_size += file_size
            status_code_count[status_code] = status_code_count.get(status_code, 0) + 1

            line_count += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics()
                status_code_count = {}
        else:
            # Skip lines that do not match the expected format
            continue

finally:
    # Handle keyboard interruption (CTRL + C)
    print_metrics()
