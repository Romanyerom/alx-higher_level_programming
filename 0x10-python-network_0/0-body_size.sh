#!/bin/bash
# Check if a URL is provided as an argument

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and display the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
