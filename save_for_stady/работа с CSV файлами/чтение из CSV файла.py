import csv
from pathlib import Path

csv_path = Path('../python/for_practice/csv_module')

with open(csv_path / 'test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    # csv_list = list(reader)
    # print(csv_list)
    for line in reader:
        print(line)

    print(reader.line_num)
