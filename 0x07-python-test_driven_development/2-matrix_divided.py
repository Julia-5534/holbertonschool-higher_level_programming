#!/usr/bin/python3
""" 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """ Function that performs matrix division
        on a list of lists of integers/floats.
    """
    if not all(isinstance(i, (int, float)) for row in matrix for i in l):
        raise TypeError("matrix must be a matrix (list of lists) \
    of integers/floats")
    if len(set(len(row) for lrow in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
