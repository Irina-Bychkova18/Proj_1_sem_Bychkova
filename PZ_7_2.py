# Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов(путь),
# собственно имя и расширение. Выделить из этой строки расширение файла (без предшествующей точки).

filename = 'C:/WindowsSystem22/calc.exe'  # полное имя файла
print(filename)
i = 0
m = filename.find('.')

while i <= 27:
    if m != i:
        i += 1
    else:
        print(filename[i + 1:i + 5])
        break