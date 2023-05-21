#!/usr/bin/python3
"""2-rectangle : module
"""


class Rectangle:
    """ Rctangle class
    args:
        number_of_instances: number of instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initiate the instance of Rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """height function which return height
        """
        return(self.__height)

    @property
    def width(self):
        """width function which return width
        """
        return self.__width

    @width.setter
    def width(self, Value):
        """width func which set width
        """
        if type(Value) is not int:
            raise TypeError("it is not intiger")
        if Value < 0:
            raise ValueError("less than zero")

        self.__width = Value

    @height.setter
    def height(self, Value):
        """height func which set height
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return((self.__height + self.__width)*2)

    def __str__(self):
        """ str function which return the string
        Retrun:
            return: which return of height by width #
        """
        return ("\n".join("".join(['#' for i in range(self.__width)])
                for j in range(self.height)))

    def __repr__(self):
        """repr returns the string function
        """
        return("Rectangle({},{})".format(self.width, self.height))

    def __del__(self):
        """ delete the instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
