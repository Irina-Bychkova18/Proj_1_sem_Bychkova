# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', отражающая продажи продукции
# по дням в кг. Преобразовать информацию из строки в словари, с использованием функции
# найти минимальные продажи по каждому виду продукции, результаты вывести на экран.


def minimum():
    print('Минимальные продажи груш:', min(pears.values()))
    print('Минимальные продажи моркови:', min(carrot.values()))


sales = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
sales = sales.split()
pears = {'1 день': int(sales[1]), '2 день': int(sales[2]), '3 день': int(sales[3]),
         '4 день': int(sales[4]), '5 день': int(sales[5])}
print('Продано всего груш:', pears)
carrot = {'1 день': int(sales[7]), '2 день': int(sales[8]), '3 день': int(sales[9]),
          '4 день': int(sales[10]), '5 день': int(sales[11])}
print('Продано всего моркови:', carrot)
minimum()
