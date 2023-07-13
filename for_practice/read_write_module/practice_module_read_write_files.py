# # создаем файл
# test_file = open('../python/for_practice/read_write_module/test.txt', 'w')
# # записываем в него 2 строки
# test_file.write("First string\n")
# test_file.write("Second string\n")
# # закрываем файл
# test_file.close()
# # открываем файл для чтения
# test_file = open('../python/for_practice/read_write_module/test.txt')

# print(test_file.read())
# # или другой вариант записать в файл + создать его
from pathlib import Path
# этот код равносилен коду выше
with open('../python/for_practice/read_write_module/test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("\n")
    test_file.write("Second string\n")

with open('../python/for_practice/read_write_module/test.txt') as test_file:
    print(test_file.read())

# дописать в файл не переписывая его
# этот код равносилен коду выше
with open('../python/for_practice/read_write_module/test.txt', 'a') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")

with open('../python/for_practice/read_write_module/test.txt') as test_file:
    print(test_file.read())
# список строк(получаем разные строки )
with open('../python/for_practice/read_write_module/test.txt') as test_file:
    lines = test_file.readlines()
    for line in lines:
        print(line)
# прочитать только определенную строку(работа с курсором)
with open('../python/for_practice/read_write_module/test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break
print("############################################################")
# удаление файлов
# from pathlib import Path

# удостовериться , что файл есть
my_file = Path('../python/for_practice/read_write_module/test.txt')


# удалить файл
if my_file.exists():
    my_file.unlink()
