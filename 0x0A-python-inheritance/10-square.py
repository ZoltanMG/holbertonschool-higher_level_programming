#!/usr/bin/python3
""" create a square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ my square """

    def __init__(self, size):
        """ init method"""

        self.__size = size
        self.integer_validator('size', self.__size)
        super().__init__(size, size)

#    def area(self):
#        """ area """

#        return super().area()
