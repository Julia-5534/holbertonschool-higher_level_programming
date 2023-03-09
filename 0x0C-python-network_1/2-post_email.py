#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response.
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    request = Request(argv[1], data=data)
    with urlopen(request) as site:
        print(site.read().decode("utf-8"))
