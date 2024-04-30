#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    rotate matrix
    """
    new = []
    for _ in range(len(matrix)):
        new.append([0] * len(matrix[0]))
    matrix.reverse()
    count = 0
    for row in matrix:
        for col in range(len(row)):
            new[col][count] = matrix[count][col]
        count += 1
    matrix[:] = new
