# Дан список размера N. Найти минимальный из его локальных максимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).

import random

a = []
b = []
N = int(input('Введите размер массива: '))
i = 0

while i < N:
    a.append(random.randrange(-10, 10))
    i += 1

print(a)
c = 1

while c < N - 1:
    if (a[c - 1] <= a[c]) and (a[c + 1] <= a[c]):
        b.append(a[c])
        c += 1
    else:
        c += 1

if len(b) == 0:
    print('Нет локальных максимумов!')
else:
    print('Минимальный из локальных максимумов: ', min(b))
