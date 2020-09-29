#!/usr/bin/python3
"""
In this Python script, a class called rectangle is created,
where width and height attributes are declared and initialized.
"""


class Rectangle:
    """
    in this class is declared
    the width and height attributes
    """

    def __init__(self, width=0, height=0):
        """ inicializador"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """ retorna el ancho """

        return self.__width

    @width.setter
    def width(self, value):
        """ actualiza el ancho """

        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ retorna el alto """

        return self.__height

    @height.setter
    def height(self, value):
        """ cambia el alto """

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
