# В матрице элементы последнего столбца заменить на -1.

import random

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
print('Исходная матрица: ')

for i in range(n):
    print(matrix[i])

matrix = [[-1 if j == m - 1 else matrix[i][j] for j in range(m)] for i in range(n)]
print('Конечная: ')

for i in range(n):
    print(matrix[i])
