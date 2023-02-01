#!/usr/bin/python3
"""11-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """It's Hip Tp Be Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


def __str__(self):
    square_string = "[Square] "
    square_string += str(self.__size) + "/" + str(self.__size)
    return square_string
