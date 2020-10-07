#!/usr/bin/python3
""" create a square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ my square """

    def __init__(self, size):
        """ init method"""

        self.integer_validator('size', self.__size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ magic method"""

        return '[Square] {}/{}'.format(self.__size, self.__size)
