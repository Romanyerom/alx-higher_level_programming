#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./100-github_commits.py <repository> <owner>")
    sys.exit(1)

repository = sys.argv[1]
owner = sys.argv[2]

url = f'https://api.github.com/repos/{owner}/{repository}/commits'
params = {'per_page': 10}
response = requests.get(url, params=params)

commits = response.json()

for commit in commits:
    sha = commit.get('sha')
    author_name = commit['commit']['author']['name']
    print(f"{sha}: {author_name}")
