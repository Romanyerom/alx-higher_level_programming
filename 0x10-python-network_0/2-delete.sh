#!/bin/bash
# Check if URL is provided

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send DELETE request and display response body
response=$(curl -s -X DELETE "$1")
echo "$response"
