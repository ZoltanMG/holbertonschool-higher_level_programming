#!/usr/bin/python3
""" inherits to BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ my Rectangle class"""

    def __init__(self, width, height):
        """ method init """

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
