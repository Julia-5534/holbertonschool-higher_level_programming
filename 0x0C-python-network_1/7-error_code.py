#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response. If the HTTP status code is greater than or equal
to 400, prints: Error code: followed by the value of the HTTP status code
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    site = requests.get(url)
    if site.status_code >= 400:
        print(f"Error code: {site.status_code}")
    else:
        print(site.text)
