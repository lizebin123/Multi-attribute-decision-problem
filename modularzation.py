import numpy as np


def modularzation(matrix):
    mod_matrix = matrix

    if matrix.ndim > 1:
        rows, columns = matrix.shape
        column_sum = np.sum(matrix**2, axis=0)
        column_sqrt = np.sqrt(column_sum)
        for i in range(0, rows):
            for j in range(0, columns):
                mod_matrix[i][j] = matrix[i][j] / column_sqrt[j]
    else:
        rows_sum = np.sum(matrix**2)
        rows_sqrt = np.sqrt(rows_sum)
        for i in range(0, len(matrix)):
            mod_matrix[i] = matrix[i] / rows_sum

    return mod_matrix
