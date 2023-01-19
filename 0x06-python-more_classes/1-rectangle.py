#!/usr/bin/python3
""" 0-rectangle Module """


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with a width and height"""
        if type(width) != int:
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be >= 0")
        if type(height) != int:
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return 2*self.__width + 2*self.__height

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
