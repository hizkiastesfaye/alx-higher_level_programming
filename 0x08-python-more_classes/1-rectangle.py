#!/usr/bin/python3
""" 1-rectangle : module"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height class of settler
        args:
           value : param1
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width class of settler
        args:
            value: param 1
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
