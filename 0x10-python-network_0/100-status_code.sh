#!/bin/bash
# Check if URL is provided

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and display only the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

echo "$status_code"
