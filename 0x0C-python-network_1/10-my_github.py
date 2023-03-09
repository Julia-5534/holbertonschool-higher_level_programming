#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from requests import get
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    requests = get(url, auth=HTTPBasicAuth(username, token).json())
    site = requests.json()["id"]
    print(site)
