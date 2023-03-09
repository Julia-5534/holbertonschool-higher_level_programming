#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the
URL and displays the value of the `X-Request-Id`
variable found in the header of the response.
"""
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    request = Request(argv[1])
    with urlopen(request) as webpage:
        header = webpage.info()
        print(header['X-Request-Id'])
