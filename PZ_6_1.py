# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
# нечетные числа в порядке возрастания их индексов, а также их количество K.

import random

a = []
b = []
i = 0
K = 0

while i < 10:
    a.append(random.randint(-10, 10))
    if a[i] % 2 == 1:
        b.append(a[i])
        i += 1
        K += 1
    else:
        i += 1

print(a)

for element in b:
    print(element)

print('Количество нечетных чисел: ', K)
