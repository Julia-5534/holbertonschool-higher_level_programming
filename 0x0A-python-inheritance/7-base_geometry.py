#!/usr/bin/python3
"""7-base_geometry"""


class BaseGeometry:
    """Hey Hey Hey I Wanna Live On A Mountain"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
