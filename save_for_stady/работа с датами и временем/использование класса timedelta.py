from datetime import datetime, timedelta

my_datetime = datetime(2023, 7, 13, 12, 00, 18)

# добавляем(отнимаем) дни, часы, минуты к выбраной дате
print(my_datetime + timedelta(days=100, minutes=120, hours=2))
