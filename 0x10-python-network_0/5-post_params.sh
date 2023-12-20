#!/bin/bash
# Check if URL is provided

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Set POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with parameters
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$1")

# Display the body of the response
echo "$response"
