# Дана непустая строка. Вывести коды ее первого и последнего символа.

import random

a = []
d = int(input('Введи размер массива: '))
t = 0

while t < d:
    a.append(chr(random.randint(45, 100)))
    t += 1

print(''.join(a))
print(ord(a[0]))
print(ord(a[-1]))
