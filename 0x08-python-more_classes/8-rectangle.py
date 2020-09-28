#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle: """


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

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

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        rec = ''
        if self.__width == 0 or self.__height == 0:
            return rec

        for i in range(self.__height):
            if i < self.__height - 1:
                rec += (str(self.print_symbol) * self.__width) + '\n'
            else:
                rec += (str(self.print_symbol) * self.__width)
        return rec

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_1
