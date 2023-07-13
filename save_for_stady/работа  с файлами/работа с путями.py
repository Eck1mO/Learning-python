from os import path
from pathlib import Path
# путь к текущей директории

print(Path.cwd())
# формирование путей на mac и unix
# from pathlib import Path

print(Path('usr').joinpath('local').joinpath('bin'))
# or (it's the same)
print(Path('usr') / 'local' / 'bin')

# форматирование путей на windows
# from pathlib import Path

print(Path('C:/').joinpath('Users').joinpath('bogdan'))
# or
print(Path('C:/') / 'Users' / 'bogdan')

# првоерка присутствия директории или файла
# from pathlib import Path

print(Path('main.py').exists())

print(Path('/home/administrator/Desktop').exists())

print(Path('other.py').exists())

# директория или файл?
# from pathlib import Path

print(Path('main.py').is_file())

print(Path('../python').is_file())

print(Path('../python').is_dir())

# список файлок и папок
# from pathlib import Path

for f in Path('../python').iterdir():
    print(f)

# практика
# from os import path

print(path.abspath('.'))  # текущая директория

# from pathlib import Path

my_dir = Path('/home') / 'administrator' / 'Desktop' / 'django'

print(my_dir.exists())
print(my_dir.is_dir())

# - проверяет наличие папки и создает папку по пути, если ее нет my_dir = Path('/home') / 'administrator' / 'Desktop' / 'django'
if not my_dir.exists():
    my_dir.mkdir()
# - проверяет наличие папки и удаляет папку по пути, если она есть my_dir = Path('/home') / 'administrator' / 'Desktop' / 'django'
if my_dir.exists():
    my_dir.rmdir()

# на windows
# from pathlib import Path

print(Path('C:/') / 'Users' / 'bogdan')

print(Path('.').cwd())
