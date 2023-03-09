#!/usr/bin/python3
import urllib.request
import sys

# get the URL from the command line argument
url = sys.argv[1]

# send a request to the URL and get the response
with urllib.request.urlopen(url) as response:
    # get the value of the X-Request-Id variable from header of response
    x_request_id = response.getheader('X-Request-Id')
    # display the value of the X-Request-Id variable
    print(x_request_id)
