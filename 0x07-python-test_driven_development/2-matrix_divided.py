#!/usr/bin/python3
"""The module contains a function that divides all elements of a
    a matrix.
    Prototype: def matrix_divided(matrix, div):
    You are not allowed to import any module
    """


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (list): list of lists of numbers
        div (int or float): Divides each elements os the lists

    Raises:
        TypeError: Error raised if matrix is not list of lists or
        each elements matrix are not either float or int
        TypeError: Error raised if length all rows of the matrix are not
        equal
        TypeError: Error raised if div is not either float or int
        ZeroDivisionError: Error raised if div == 0

    Returns:
        _type_: _description_
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(number, int) or isinstance(number, float))
                    for number in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, float)) and (not isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda item:round(item / div, 2), row))
            for row in matrix] 
