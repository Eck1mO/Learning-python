from pathlib import Path

# проверяем наличие файла
print(Path('/home/administrator/python/for_practice/write.txt').exists())

# удаляем файл
Path('/home/administrator/python/for_practice/read_write_module/write.txt').unlink()

# проверяем наличие файла
print(Path('/home/administrator/python/for_practice/read_write_module/write.txt').exists())
