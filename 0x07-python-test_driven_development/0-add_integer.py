#!/usr/bin/python3
def add_integer(a, b=98):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or floats")
    a, b = int(a), int(b)
    return a + b
