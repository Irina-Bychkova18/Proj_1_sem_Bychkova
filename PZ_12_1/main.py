# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

from tkinter import *

root = Tk()
root.title("Contact form")
root.geometry('800x680+200+200')
root.minsize(100, 100)
root.maxsize(800, 800)

img = PhotoImage(file='phon00.png')
c = Label(image=img).place(x=1, y=50)
tri = PhotoImage(file='tri tochki1.png')
rash = PhotoImage(file='rash.png')
Label(text="", width=20, fg='#0000aa', image=tri, compound=RIGHT, font='arial 8').place(x=20, y=10)
Label(text="", width=20, fg='#0000aa', image=rash, compound=RIGHT, font='arial 8').place(x=760, y=7)

Label(text="Contact form", width=10, bg='dodger blue', fg='white', font='arial 15').place(x=117, y=75)
Label(text="Please fill in your information and we'll be sending your order in no time.",
      width=55, bg='dodger blue', fg='white', font='arial 10').place(x=117, y=115)
Label(text="First Name", width=8, fg='blue', font='arial 8').place(x=217, y=190)
Label(text="Last Name", width=8, fg='blue', font='arial 8').place(x=370, y=190)
Label(text="Your Name", width=8, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=235)
Label(text="Your Email", width=12, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=298)
Label(text="Message Subject*", width=15, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=405)
Label(text="Message*", width=10, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=465)
Label(text="Phone*", width=10, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=350)
Label(text="###", width=5, fg='#0000aa', font='arial 8').place(x=217, y=326)
Label(text="###", width=5, fg='#0000aa', font='arial 8').place(x=321, y=326)
Label(text="####", width=7, fg='#0000aa', font='arial 8').place(x=417, y=326)
Label(text="Verification*", width=15, bg='dodger blue', fg='white', font='arial 8').place(x=117, y=545)

Entry(width=10, font='arial 18').place(x=217, y=220)
Entry(width=10, font='arial 18').place(x=370, y=220)
Entry(width=22, font='arial 18').place(x=217, y=290)
Entry(width=9, font='arial 43').place(x=217, y=465)
Entry(width=10, font='arial 13').place(x=217, y=350)
Entry(width=10, font='arial 13').place(x=314, y=350)
Entry(width=10, font='arial 13').place(x=410, y=350)

photo = PhotoImage(file="knopka.png")
var = IntVar()
check1 = Checkbutton(root, text=u"I'm not a robot", variable=var,
                     onvalue=1, offvalue=0, image=photo, compound=RIGHT).place(x=217, y=545)

Button(text="SUBMIT FORM", width=19, height=1, bg='dodger blue',
       fg='white', font='arial 15').place(x=117, y=620)

listbox2 = Listbox(root, height=3, width=10, selectmode=SINGLE)
list2 = [u"My family", u"Friends", u"Other"]
for i in list2:
 listbox2.insert(END, i)
listbox2.place(x=217, y=405)


root.mainloop()
