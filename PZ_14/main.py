# В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.

import re

p = re.compile(r'[1][8][2-8][0-9]\s[г][о][д][\sау]')
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    k = p.findall(text)
    print(k)
    print(len(k))
