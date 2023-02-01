#!/usr/bin/python3
"""6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
