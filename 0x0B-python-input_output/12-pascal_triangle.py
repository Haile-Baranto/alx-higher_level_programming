#!/usr/bin/python3
"""
    Returns list of lists which represent pascal triangle
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
    """
def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle
    up to the given n number of rows.
    """
    if n <= 0:
        return ""

    # Initialize the first row of the triangle.
    triangle = [[1]]

    # Compute each subsequent row of the triangle.
    for row_num in range(1, n):
        prev_row = triangle[row_num - 1]
        new_row = [1]  # The first element of each row is always 1.
        for elem_num in range(1, row_num):
            # Compute the middle elements of each row.
            elem_value = prev_row[elem_num] + prev_row[elem_num - 1]
            new_row.append(elem_value)
        new_row.append(1)  # The last element of each row is always 1.
        triangle.append(new_row)

    return triangle
