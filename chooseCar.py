import math
import numpy as np

from modularzation import modularzation
from normalization import normalization

A = np.array([[1 / 25, 9, 7],
              [1 / 18, 7, 7],
              [1 / 12, 5, 5]])
rows, columns = A.shape
matrix = np.copy(A)
matrix = normalization(matrix)
for i in range(0, rows):
    for j in range(0, columns):
        matrix[i][j] = matrix[i][j] * math.log(matrix[i][j])
matrix1 = np.sum(matrix, axis=0)
E = -(1 / math.log(rows)) * matrix1
F = 1 - E
w = normalization(F)
# 简单集权和法
matrix2 = np.copy(A)
matrix2 = normalization(matrix2)
# 简单集权和法
for i in range(rows):
    for j in range(columns):
        matrix2[i][j] *= w[j]

v1 = np.sum(matrix2, axis=1)  # 计算列的加权和
print('加权和法：',v1)
# 加权积法
matrix3 = np.copy(A)
for i in range(rows):
    for j in range(columns):
        matrix3[i][j] = matrix3[i][j] ** w[j]
v2 = np.prod(matrix3, axis=1)
print('加权积法：',normalization(v2))  # 最后记得归一化
# TOPSIS
matrix4 = np.copy(A)
matrix4 = modularzation(matrix4)

for i in range(rows):
    for j in range(columns):
        matrix4[i][j] *= w[j]
V_positive = np.max(matrix4, axis=0)
V_negative = np.min(matrix4, axis=0)
matrix5 = np.copy(matrix4)
matrix6 = np.copy(matrix4)
for i in range(rows):
    for j in range(columns):
        matrix5[i][j] = (matrix4[i][j] - V_positive[j]) ** 2
        matrix6[i][j] = (matrix4[i][j] - V_negative[j]) ** 2

S_positive = np.sqrt(np.sum(matrix5, axis=1))
S_negative = np.sqrt(np.sum(matrix6, axis=1))
C=S_negative/(S_positive+S_negative)
print('TOPSIS:',normalization(C))
