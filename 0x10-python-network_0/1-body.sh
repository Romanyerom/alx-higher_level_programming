#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body for a 200 status code.
curl -s "$1" | grep -oP "(?<=^Route\ 2\n).*"
