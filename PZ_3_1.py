# Даны три целых числа: A, B, C.
# Проверить истинность высказывания: «Число B находится между числами A и C».

A, B, C = input('Введите первое число: '), input('Введите второе число: '), input('Введите '
                                                                                  'третье число: ')

while type(A) != int:  # обработка исключений
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели!')
        A = input('Введите первое число: ')

while type(B) != int:  # обработка исключений
    try:
        B = int(B)
    except ValueError:
        print('Неправильно ввели!')
        B = input('Введите второе число: ')

while type(C) != int:  # обработка исключений
    try:
        C = int(C)
    except ValueError:
        print('Неправильно ввели!')
        C = input('Введите третье число: ')

if (A < B < C) or (A > B > C):
    print('Истина')
else:
    print('Ложь')
