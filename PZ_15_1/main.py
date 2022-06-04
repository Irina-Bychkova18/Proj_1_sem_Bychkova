# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

import random

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
N = int(input('Введите номер строки: '))
matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
print('Исходная матрица: ')

for i in range(n):
    print(matrix[i])

matrix = [[matrix[i][j] + 3 if N == i else matrix[i][j] for j in range(m)] for i in range(n)]
print('Конечная: ')

for i in range(n):
    print(matrix[i])
