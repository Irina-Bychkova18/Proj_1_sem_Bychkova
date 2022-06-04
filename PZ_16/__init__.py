import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)

        self.btn_open_dialog = None
        self.tree = ttk.Treeview(self, columns=('code', 'name_of_the_medicine', 'application', 'quantity',
                                                'price', 'country_of_origin'), height=15, show='headings')
        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        self.update_img = tk.PhotoImage(file="BD/12.gif")
        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.search_img = None
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.btn_open_dialog = tk.Button(toolbar, text='Добавить лекарственное средство ',
                                         command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130', bd=0,
                               compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree.column('code', width=50, anchor=tk.CENTER)
        self.tree.column('name_of_the_medicine', width=150, anchor=tk.CENTER)
        self.tree.column('application', width=120, anchor=tk.CENTER)
        self.tree.column('quantity', width=120, anchor=tk.CENTER)
        self.tree.column('price', width=50, anchor=tk.CENTER)
        self.tree.column('country_of_origin', width=160, anchor=tk.CENTER)

        self.tree.heading('code', text='Код')
        self.tree.heading('name_of_the_medicine', text='Название препарата')
        self.tree.heading('application', text='Применение')
        self.tree.heading('quantity', text='Количество')
        self.tree.heading('price', text='Цена')
        self.tree.heading('country_of_origin', text='Страна-производитель')

        self.tree.pack()

    def records(self, code, name_of_the_medicine, application, quantity, price, country_of_origin):
        self.db.insert_data(code, name_of_the_medicine, application, quantity, price, country_of_origin)
        self.view_records()

    def update_record(self, code, name_of_the_medicine, application, quantity, price, country_of_origin):
        self.db.cur.execute("""UPDATE Лекарственные_средства SET code=?, name_of_the_medicine=?, application=?,
         quantity=?, price=?,  country_of_origin=? WHERE code=?""",
                            (code, name_of_the_medicine, application, quantity, price, country_of_origin,
                             self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM Лекарственные_средства""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM Лекарственные_средства WHERE code=?""", (self.tree.set(selection_item,
                                                                                                      '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, name_of_the_medicine):
        name_of_the_medicine = ("%" + name_of_the_medicine + "%",)
        self.db.cur.execute("""SELECT * FROM Лекарственные_средства WHERE name_of_the_medicine LIKE ?""",
                            name_of_the_medicine)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.btn_ok = ttk.Button(self, text='Добавить')
        self.entry_description = ttk.Entry(self)
        self.entry_name = ttk.Entry(self)
        self.entry_sex = ttk.Entry(self)
        self.entry_old = ttk.Entry(self)
        self.entry_price = ttk.Entry(self)
        self.entry_score = ttk.Entry(self)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить лекарственное средство')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код')
        label_description.place(x=50, y=25)
        self.entry_description.place(x=190, y=25)

        label_name = tk.Label(self, text='Название препарата')
        label_name.place(x=50, y=50)
        self.entry_name.place(x=190, y=50)

        label_sex = tk.Label(self, text='Применение')
        label_sex.place(x=50, y=75)
        self.entry_sex.place(x=190, y=75)

        label_old = tk.Label(self, text='Количество')
        label_old.place(x=50, y=100)
        self.entry_old.place(x=190, y=100)

        label_price = tk.Label(self, text='Цена')
        label_price.place(x=50, y=125)
        self.entry_price.place(x=190, y=125)

        label_score = tk.Label(self, text='Страна-производитель')
        label_score.place(x=50, y=150)
        self.entry_score.place(x=190, y=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=180)

        self.btn_ok.place(x=220, y=180)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_sex.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_price.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=180)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_sex.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_price.get(),
                                                                          self.entry_score.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.entry_search = ttk.Entry(self)
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:

    def __init__(self):
        with sq.connect('BD/АПТЕКА_.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS Лекарственные_средства (
                    code INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_of_the_medicine TEXT NOT NULL,
                    application TEXT NOT NULL,
                    quantity INTEGER,
                    price INTEGER,
                    country_of_origin TEXT NOT NULL
                    )""")


    def insert_data(self, code, name_of_the_medicine, application, quantity, price, country_of_origin):
        self.cur.execute("""INSERT INTO Лекарственные_средства(code, name_of_the_medicine, 
        application, quantity, price, country_of_origin) VALUES (?, ?, ?, ?, ?, ?)""",
                         (code, name_of_the_medicine, application, quantity, price, country_of_origin))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных АПТЕКА")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
