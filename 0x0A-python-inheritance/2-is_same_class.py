#!/usr/bin/python3
"""2-is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if object is exact instance of class"""
    return type(obj) is a_class
