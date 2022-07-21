l1 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
l2 = [[4, 4, 4, 4], [5, 5, 5, 5], [7, 7, 7, 7]]

import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ''
        for i in range(len(self.matrix)):
            a = a + '\t'.join(map(str, self.matrix[i])) + '\n'
        return a

    def __add__(self, other):
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


matrix1 = Matrix(l1)
matrix2 = Matrix(l2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)