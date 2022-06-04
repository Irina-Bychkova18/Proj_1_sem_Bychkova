# Составить генератор (yield), который преобразует все буквенные символы в строчные.


def sq_all():
    yield from [n.lower() for n in numbers]


numbers = 'In PyCharm, You can sPeСify 3-party standalone aPPlications and RUN them as External Tools123.'
squares = sq_all()

[print(i) for i in squares]
