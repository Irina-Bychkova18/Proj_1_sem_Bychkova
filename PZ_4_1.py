# Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно.

A = input('Введите первое число: ')

while type(A) != int:  # обработка исключений
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели!')
        A = input('Введите первое целое число: ')

B = input('Введите второе число: ')

while type(B) != int:  # обработка исключений
    try:
        B = int(B)
    except ValueError:
        print('Неправильно ввели!')
        B = input('Введите второе целое число: ')

while B <= A:  # ограничение диапазона
    try:
        print('Неправильно ввели!')
        A = int(input('Введите первое число: '))
    except TypeError:
        A = int(input('Введите первое число: '))

P = 1

while A <= B:
    P *= A
    A += 1

print('Произведение = ', P)
