import numpy as np


def normalization(matrix):
    ledone_matrix = matrix

    if matrix.ndim > 1:
        rows, columns = matrix.shape
        column_sum = np.sum(matrix, axis=0)
        for i in range(0, rows):
            for j in range(0, columns):
                ledone_matrix[i][j] = matrix[i][j] / column_sum[j]
    else:
        rows_sum = np.sum(matrix)
        for i in range(0, len(matrix)):
            ledone_matrix[i] = matrix[i] / rows_sum

    return ledone_matrix
