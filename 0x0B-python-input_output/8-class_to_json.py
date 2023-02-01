#!/usr/bin/python3
"""8-class_to_json"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of obj"""
    return obj.__dict__
