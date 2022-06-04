import sqlite3 as sq

with sq.connect('АПТЕКА.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Лекарственные_средства (
 code INTEGER PRIMARY KEY AUTOINCREMENT,
 name_of_the_medicine TEXT NOT NULL,
 application TEXT NOT NULL,
 quantity INTEGER,
 price INTEGER,
 country_of_origin TEXT NOT NULL)""")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (1, 'Афобазол', 'лечение ран', "
                "22, 1000, 'Россия')")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (2, 'Гаргазон', 'лечение ожогов', 19, 800, 'США')")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (3, 'Риномакс', 'лечение зубной боли', "
                "19, 900, 'Франция')")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (4, 'Ентриксамакс', 'лечение головной боли',"
                " 18, 1500, 'Германия')")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (5, 'Реканат', 'лечение ран', 20, 1100, 'США')")
    cur.execute("INSERT INTO Лекарственные_средства VALUES (6, 'Ларималь', 'лечение ожогов', 20, 1100, "
                "'Россия')")
