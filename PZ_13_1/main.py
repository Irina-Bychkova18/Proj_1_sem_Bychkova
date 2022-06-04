# Организовать и вывести последовательность из N случайных целых чисел. Из исходной последовательности
# организовать первую последовательность, содержащую четные числа, и вторую – для всех остальных.
# Найти среднее арифметическое в полученных последовательностях.

import random
from functools import reduce
L = random.sample(range(10), 5)
print(L)
M = list(filter(lambda x: x % 2 == 0, L))
m = len(M)
print(M)
C = list(filter(lambda x: x % 2 == 1, L))
c = len(C)
print(C)
K = reduce(lambda x, y: x + y, M)
print(K // m)
P = reduce(lambda x, y: x + y, C)
print(P // c)
