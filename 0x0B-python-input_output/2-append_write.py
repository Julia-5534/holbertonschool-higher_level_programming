#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """Appends string @ end of text file & returns # of characters added"""
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
