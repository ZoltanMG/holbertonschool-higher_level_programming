#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """

    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    err_int_fl = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) == 0\
       or type(matrix[0]) is not list:
        raise TypeError(err_int_fl)
    new_matrix = []
    size_ref = len(matrix[0])

    for vector in matrix:
        if len(vector) != size_ref:
            raise TypeError('Each row of the matrix must have the same size')
        row = []
        for num in vector:
            if type(num) not in (int, float):
                raise TypeError(err_int_fl)
            row.append(round(num / div, 2))
        new_matrix.append(row)

    return new_matrix
