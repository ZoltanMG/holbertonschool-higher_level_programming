#!/usr/bin/python3
def add_integer(a, b=98):
    if a is not None:
        if type(a) not in (float, int):
            raise TypeError('a must be an integer')
        if type(b) not in (int, float):
            raise TypeError('b must be an integer')
        return int(a) + int(b)
    else:
        raise TypeError('a must be an integer')
