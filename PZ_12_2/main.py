# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# PZ_5_1
# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.

from tkinter import *


def count_num(_):
    s = 0

    n1 = int(num1.get())
    n2 = int(num2.get())

    while n1 <= n2:
        s += n1
        n1 += 1

    positive['text'] = "Сумма_чисел_=", s


root = Tk()
root.title("Поиск суммы чисел ряда 1, 2, 3...")
root.geometry("300x200+200+200")


Label(text="Первое число").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)


Label(text="Второе число").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)


button1 = Button(text="Вычислить")
button1.grid(row=4, column=1)

positive = Label()
positive.grid(row=5, column=1)

button1.bind('<Button-1>', count_num)


root.mainloop()
