#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request with custom header
response=$(curl -s -H "X-School-User-Id: 98" "$1")

# Display the body of the response
echo "$response"