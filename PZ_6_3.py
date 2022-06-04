# Дан список размера N. Возвести в квадрат все его локальные минимумы
# (то есть числа,меньшие своих соседей).

import random

N = int(input('Введите размер массива: '))
a = []
t = 0
b = []

while t < N:
    a.append(random.randint(-10, 10))
    t += 1

print(a)
p = 1

while p < N - 1:
    if (a[p] <= a[p - 1]) and (a[p] <= a[p + 1]):
        b.append(a[p])
        p += 1
    else:
        p += 1

if len(b) == 0:
    print('Нет локальных минимумов!')
else:
    for element in b:
        print(element**2)
