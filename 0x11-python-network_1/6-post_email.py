#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)

print("Your email is:", email)
print(response.text)
