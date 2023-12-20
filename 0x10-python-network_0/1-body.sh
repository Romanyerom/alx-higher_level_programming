#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep "200" && curl -s "$1"
