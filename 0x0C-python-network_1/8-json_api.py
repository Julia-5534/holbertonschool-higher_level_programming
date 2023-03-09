#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    site = requests.post(url, data=data)
    try:
        result = site.json()
        if len(result) == 0:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except ValueError:
        print("Not a valid JSON")
