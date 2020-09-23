#!/usr/bin/python3
"""  class Square that defines a square by: (based on 2-square.py) """


class Square:
    """  class Square that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """ stored size if size is a integer >= 0"""

        err = 'position must be a tuple of 2 positive integers'
        try:
            if type(size) == int:
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')

            if type(position) == tuple and len(position) == 2 and\
               type(position[0]) == int and type(position[1] == int) and\
               position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError(err)
        except (TypeError, ValueError):
            raise

    def area(self):
        """ returns the current square area """

        return self.__size ** 2

    @property
    def position(self):
        """ returns _position"""

        return self.__position

    @position.setter
    def position(self):
        """ returns changed value of __position"""

        try:
            if type(position) == tuple and len(position) == 2 and\
               type(position[0]) == int and type(position[1] == int) and\
               position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError(err)
        except TypeError:
                raise

    @property
    def size(self):
        """ return size value """

        return self.__size

    @size.setter
    def size(self, value):
        """ stored size if size is a integer >= 0"""

        try:
            if type(value) == int:
                if value >= 0:
                    self.__size = value
                else:
                    raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except (TypeError, ValueError):
            raise

    def my_print(self):
        """ prints a squad with # character """

        if self.__size == 0:
            print()
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.__size):
                if self.__position[1] == 0:
                    print('{}'.format(' ' * self.__position[0]), end='')
                print('{}'.format('#' * self.__size))
