#!/usr/bin/python3
"""The Square Mod Squad"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes a square with a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Prints area"""
        return self.__size ** 2

    @property
    def size(self):
        """Gets a square's size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a square's size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
