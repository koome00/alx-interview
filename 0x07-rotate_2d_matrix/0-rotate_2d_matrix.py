#!/usr/bin/python3
"""
Module: Interview Question
"""
def rotate_2d_matrix(matrix: list[int]) -> list[int]:
    """
    rotate matrix
    """

    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][rows - i - 1] = matrix[i][j]

    matrix[:] = new_matrix
