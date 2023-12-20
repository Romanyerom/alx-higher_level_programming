#!/bin/bash
# This script sends a JSON POST request with the contents of a file and displays the body of the response
jq . "$2" > /dev/null && curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1" || echo "Not a valid JSON"
