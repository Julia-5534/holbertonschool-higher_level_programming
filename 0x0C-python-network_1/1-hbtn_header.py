#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header_dict = dict(response.getheaders())
    x_request_id = header_dict.get('X-Request-Id')

print(x_request_id)
