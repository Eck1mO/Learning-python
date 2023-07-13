# встроенные модули для работы  с файлами:
#      os - является пакетом, который содержит разные модули, в том числе path
#      pathlib - обьектно-ориентированный подход к работе с файлами

# os example - функциональный подход
from pathlib import Path
from os import path

print(path.abspath('.'))
print(type(path))

# pathlib example - обьектно-ориентированный подход
# from pathlib import Path

print(Path('.').absolute())
print(type(Path))
