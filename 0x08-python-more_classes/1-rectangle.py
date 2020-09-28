#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle: """


class Rectangle:
    def __init__(self, width=0, height=0):
        """ inicializa los valores de width y height """

        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.wigth = width
        self.height = height
        # como prueba no encapsulé las variables en el init
        # pero si en los setters and getters

    @property
    def width(self):
        """ retorna el valor de width """

        return self.__width

    @width.setter
    def width(self, value):
        """ actualiza o cambia el valor de width """

        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ retorna el valor de height """

        return self.__height

    @height.setter
    def height(self, value):
        """ actualiza o cambia el valor de hetght"""

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
