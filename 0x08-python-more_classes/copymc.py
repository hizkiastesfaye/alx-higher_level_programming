#!/usr/bin/python3
"""2-rectangle : module
"""


class Rectangle:
    """ Rctangle class
    args:
        number_of_instances: number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

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
        return ("\n".join("".join([str(self.print_symbol)
                for i in range(self.__width)])
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

    def bigger_or_equal(rect_1, rect_2):
        """ biiger_or_equal func return the bigger rectangle in area
        """
        rec1 = rect_1.area()
        rec2 = rect_2.area()

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rec1>= rec2):
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)



my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
