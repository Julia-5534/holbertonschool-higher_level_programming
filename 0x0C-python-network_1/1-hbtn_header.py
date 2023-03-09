#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the
URL and displays the value of the `X-Request-Id`
variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    http = sys.argv[1]
    req = urllib.request.Request(http)
    with urllib.request.urlopen(req) as response:
        headers = response.getheaders()
        x_request_id = [x[1] for x in headers if x[0] == 'X-Request-Id'][0]

print(x_request_id)
