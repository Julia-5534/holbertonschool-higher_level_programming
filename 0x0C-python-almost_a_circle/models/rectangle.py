#!/usr/bin/python3
"""class Rectangle is also based
    due to inheritating the basedness
"""
from models.base import Base


class Rectangle(Base):
    """
    create based class rectangle which is based off based Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize based rectangle values width, height, x, y, and id
        Based Args:
            width: width of rectangle
            height: height of rectangle
            x: x coordinate of rectangle
            y: y coordinate of rectangle
            id: id of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width of based rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets width of based rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns height of based rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets height of based rectangle"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns x coordinate of based rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets x coordinate of based rectangle"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns x coordinate of based rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y coordinate of based rectangle"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Print rectangle in stdout with character #"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes
        **kwargs can be thought of as a double pointer
            to a dictionary: key/value
        """
        argList = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, argList[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of based rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

    def __str__(self):
        """
        Overrides the built-in __str__ method to return a string in the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
