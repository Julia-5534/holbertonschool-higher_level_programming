#!/usr/bin/python3
"""11-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class Inherits From Rectangle"""
    def __init__(self, size):
        """__init__ - initialize a square class
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """returns square description"""
        return f"[Square] {self.__size}/{self.__size}"
