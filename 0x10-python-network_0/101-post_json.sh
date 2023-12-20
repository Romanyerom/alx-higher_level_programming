#!/bin/bash
# Check if URL and filename are provided

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <URL> <JSON_FILE>"
  exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" > /dev/null 2>&1; then
  echo "Not a valid JSON"
  exit 1
fi

# Send JSON POST request and display the body of the response
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1")

echo "$response"
