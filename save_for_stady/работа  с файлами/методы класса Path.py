# атрибуты pathlib path
from pathlib import Path

file_path = Path('test.txt')

print([m for m in dir(file_path)
       if not m.startswith('_')])
