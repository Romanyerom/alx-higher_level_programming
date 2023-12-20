#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'
auth = (username, token)
response = requests.get(url, auth=auth)

try:
    user_data = response.json()
    user_id = user_data.get('id')
    print(user_id)
except ValueError:
    print(None)
