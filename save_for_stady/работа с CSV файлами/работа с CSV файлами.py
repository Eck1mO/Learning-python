import csv
from pathlib import Path

csv_path = Path('../python/for_practice/csv_module')

with open(csv_path / 'test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'user_qty'])
    writer.writerow([523, 'bogdan', 1352])
    writer.writerow([524, 'mika', 13])
    writer.writerow([525, 'alice', 122])
