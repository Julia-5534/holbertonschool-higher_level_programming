#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """True-obj instance of class inherited from specified class|else-False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
