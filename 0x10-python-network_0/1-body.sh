#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request and display the body for a 200 status code
response=$(curl -s -w "%{http_code}" "$1")

# Extract the numeric part of the status code from the response
status_code=$(echo "$response" | tail -n1 | tr -cd '[:digit:]')

# Check if the status code is 200 and display the body
if [ "$status_code" -eq 200 ]; then
    curl -s "$1"
fi
