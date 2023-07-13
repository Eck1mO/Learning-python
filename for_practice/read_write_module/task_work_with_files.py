from pathlib import Path

# создание пути к папке
files_dir = Path(
    '../python/for_practice/read_write_module/dir_for_practice_bogdan')
# создаем папку и проверяем наличие папки (если она есть , ошибки не будет)
files_dir.mkdir(exist_ok=True)

# путь к файлам
first_file = files_dir / 'first.txt'
second_file = files_dir / 'second.txt'

#  добавляем файлы и строки в них
with open(first_file, 'w') as f:
    f.write("First line \n")
    f.write("Second line \n")

with open(second_file, 'w') as f:
    lines = [
        "First line in the second file",
        "Second line in the second file",
        "Last line in the second file"
    ]
    for line in lines:
        f.write(line + '\n')

# прочитать файл
# полностью
with open(first_file) as f:
    print(f.read())
# построчно (убирая пробелы)
with open(second_file) as f:
    for line in f:
        print(line.strip())
        # or OPTION 2
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip())

# удалить папку и файлы
# удалить файлы
first_file.unlink()
second_file.unlink()

# удаляем папку
files_dir.rmdir()
