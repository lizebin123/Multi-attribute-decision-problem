import numpy as np


def maximize(matrix):
    max_matrix = matrix

    if matrix.ndim > 1:
        rows, columns = matrix.shape
        column_sum = np.max(matrix, axis=0)
        for i in range(0, rows):
            for j in range(0, columns):
                max_matrix[i][j] = matrix[i][j] / column_sum[j]
    else:
        rows_sum = np.max(matrix)
        for i in range(0, len(matrix)):
            max_matrix[i] = matrix[i] / rows_sum

    return max_matrix
