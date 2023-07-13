from datetime import date, time, datetime

my_date = date(2023, 4, 15)
my_time = time(18, 10, 45)
my_datetime = datetime(2023, 12, 10, 18, 10, 45)

print(my_date.isocalendar())
# print(my_date)
# print(my_date.day)
# print(my_date.year)
# print(my_date.month)

print(my_time)
# print(my_time.hour)
# print(my_time.minute)
# print(my_time.second)

print(my_datetime)
print(my_datetime.isoformat())
print(my_datetime.now())

print("########################################################")
# практика

print(my_datetime.strftime('%d-%b-%Y %H:%M:%S'))


date_str = '10/12/2023'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')

print(converted_date)
