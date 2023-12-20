#!/usr/bin/python3
"""
Sends a POST request with an email parameter
and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
