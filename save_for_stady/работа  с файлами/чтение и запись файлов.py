# чтение файла
with open('../python/for_practice/read_write_module/read.txt') as test_file:
    print(test_file.read())

# чтение файла (помещает все строки в список)
with open('../python/for_practice/read_write_module/read.txt') as test_file:
    print(test_file.readlines())
print('########################################################')
# запись в файл
with open('../python/for_practice/read_write_module/write.txt', 'w') as new_file:
    new_file.write("First line in the new file\n")

with open('../python/for_practice/read_write_module/read.txt', 'w') as new_file:
    new_file.write("First line in the new file\n")

# прочитать файл
with open('../python/for_practice/read_write_module/write.txt') as new_file:
    print(new_file.read())

# дозапись в файл
with open('../python/for_practice/read_write_module/write.txt', 'a') as new_file:
    new_file.write("Second line in the new file\n")

# прочитать файл
with open('../python/for_practice/read_write_module/write.txt') as new_file:
    print(new_file.read())
