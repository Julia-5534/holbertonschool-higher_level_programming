#!/usr/bin/python3
"""1-write_file"""


def write_file(filename="", text=""):
    """Function writes string to text file & returns # of characters written"""
    with open(filename, 'w', encoding="utf8") as f:
        f.write(text)
    return len(text)
