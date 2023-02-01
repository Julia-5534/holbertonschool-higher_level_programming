#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """Function that reads a text file and prints to stdout"""
    with open(filename, encoding="utf8") as f:
        print(f.read())
