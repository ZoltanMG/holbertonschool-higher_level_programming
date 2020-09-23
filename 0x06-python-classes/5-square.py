#!/usr/bin/python3
"""  class Square that defines a square by: (based on 2-square.py) """


class Square:
    """  class Square that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0):
        """ stored size if size is a integer >= 0"""

        try:
            if type(size) == int:
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except (TypeError, ValueError):
            raise

    def area(self):
        """ returns the current square area """

        return self.__size ** 2

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
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
