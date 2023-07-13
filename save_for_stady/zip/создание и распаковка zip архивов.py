from zipfile import ZipFile
from pathlib import Path

my_dir = Path('../python/for_practice/zip_module')
dir_for_zip_file = Path('../python/for_practice/zip_module/dir_zip')
first_file = my_dir / 'first.txt'
second_file = my_dir / 'second.txt'

if not dir_for_zip_file.exists():
    dir_for_zip_file.mkdir()

if not my_dir.exists():
    my_dir.mkdir()


with open(first_file, 'w') as my_file:
    my_file.write("This is first file")

with open(second_file, 'w') as my_file:
    my_file.write("This is second file")

# cоздаем архив
with ZipFile(dir_for_zip_file / 'my_files.zip', mode='w') as my_zip_file:
    # итерация по директории
    for file in Path(my_dir).iterdir():
        print(file)
        # добавить в архив
        my_zip_file.write(file)

# распаковываем архив
# with ZipFile(dir_for_zip_file / 'my_files.zip') as my_zip_file:
#     my_zip_file.extractall('./unzip')
#     # print(my_zip_file.infolist())
