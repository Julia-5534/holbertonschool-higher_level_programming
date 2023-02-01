#!/usr/bin/python3
"""4-from_json_string"""
import json


def from_json_string(my_str):
    """Function returns obj (Python data structure) represented by JSON str"""
    return json.loads(my_str)
