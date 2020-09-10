#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[pow_ ** 2 for pow_ in vector] for vector in matrix]
    return new_matrix
