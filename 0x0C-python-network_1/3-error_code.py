#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = Request(argv[1])
    try:
        with urlopen(url) as site:
            print(site.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
