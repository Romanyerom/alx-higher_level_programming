#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send OPTIONS request to get allowed methods and display only the Allow header
allowed_methods=$(curl -s -I -X OPTIONS HEAD PUT "$1" | grep -i ^Allow | cut -d ' ' -f 2-)

echo "$allowed_methods"
