# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.

def amount(n, m):
    s = 0

    while n <= m:
        s += n
        n += 1

    return s


k = int(input('Введите первое число: '))
p = int(input('Введите второе число: '))
print('Сумма чисел = ', amount(k, p))
