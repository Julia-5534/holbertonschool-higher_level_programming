#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    site = requests.get(url)
    body = site.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
