# циклы используются для перебора элементов последовательностей: dict, list
# , tuple, set, range, str.
# типы циклов: for...in..., while

# for in для списков(list)
my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(elem)

# for in для кортежей(tuple)
video_info = ('1920x1080', True, 27)
for elem in video_info:
    print(elem)

# for in для словарей(dict)
my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_object:
    print(key, my_object[key])

# цикл for in для наборов(set)
video_ids = {1435, 4317, 2761, 5721}

for id in video_ids:
    print(id)

# for in для строк (str)
my_name = 'Bogdan'

for char in my_name:
    print(char)

# for in для диапазонов (range)
for num in range(5):
    print(num)
#########################
for odd_nums in range(3, 10, 2):
    print(odd_nums)
##################################################
# практика
for el in [1, 'abc', True]:
    print(type(el))
    print(el)
#################################################
my_dict = {'id': 101, 'title': 'test'}

for key in my_dict:
    print(key, my_dict[key])
##########################################################
