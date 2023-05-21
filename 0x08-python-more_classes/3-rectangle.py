#!/usr/bin/python3
"""2-rectangle : module
"""


class Rectangle:
    """ Rctangle class"""
    def __init__(self, width=0, height=0):
        """initiate the instance
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """height
        """
        return(self.__height)

    @property
    def width(self):
        """width
        """
        return self.__width

    @width.setter
    def width(self, Value):
        """width func
        """
        if type(Value) is not int:
            raise TypeError("it is not intiger")
        if Value < 0:
            raise ValueError("less than zero")

        self.__width = Value

    @height.setter
    def height(self, Value):
        """height func
        """
        if type(Value) is not int:
            raise TypeError("it is not intiger")
        if Value < 0:
            raise ValueError("less than zero")
        self.__height = Value

    def area(self):
        """returns area func
        """
        return(self.__height * self.__width)

    def perimeter(self):
        """perimeter func
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return((self.__height + self.__width)*2)

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))
