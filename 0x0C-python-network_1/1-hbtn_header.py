#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the
URL and displays the value of the `X-Request-Id`
variable found in the header of the response.
"""
from urllib import request
import sys

if __name__ == "__main__":
    http = sys.argv[1]
    req = request.Request(http)
    with request.urlopen(req) as response:
        print(response.info()['X_Request_Id'])
