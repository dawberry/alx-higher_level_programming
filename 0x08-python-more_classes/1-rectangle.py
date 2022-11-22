#!/usr/bin/python3

"""Defines a Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Class instance method.
        
        Args:
            
            width (int): the width value
            height (int): the height value
        """
        self.width = width
        self.height = width

    @property
    def width(self):
        """Getts the width private variable"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setes the width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Setes the height value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
