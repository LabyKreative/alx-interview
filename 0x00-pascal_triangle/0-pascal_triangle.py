#!/usr/bin/python3
""" a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):

    """Returns a list of lists of integers representing
    the Pascal's triangle of `n`.
    """

    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
