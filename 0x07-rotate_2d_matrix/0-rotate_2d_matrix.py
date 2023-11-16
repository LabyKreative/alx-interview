#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate it 90 degrees clockwise"""
    n = len(matrix)

    # Traverse each layer of the matrix
    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        # Iterate over elements in current layer
        for i in range(first, last):
            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom element to left
            matrix[last - (i - first)][first] = \
                matrix[last][last - (i - first)]

            # Move right element to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top
