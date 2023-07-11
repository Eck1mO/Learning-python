# сокращенный for in используется для создания новых последовательностей (list, dict, tuple, set)
# обычный for in
all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)
print(all_nums)
# сокращенный for in
all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = [abs(num) for num in all_nums]

print(absolute_nums)
print(all_nums)
# обычный for in
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)
print(all_nums)
# сокращенный for in
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
print(all_nums)
# example
# форматирование нового набора в обычном for in
my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)
print(my_set)
# сокращенный for in
my_set = {1, 10, 15}

new_set = {val * val for val in my_set}
print(my_set)
print(new_set)
# форматирование нового словаря в обычном for in
my_score = {
    'a': 10,
    'b': 7,
    'c': 14
}

scores = {}

for k, v in my_score.items():
    scores[k] = v * 10

print(scores)
print(my_score)
# сокращенный for in
my_score = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {k: v * 10 for k, v in my_score.items()}

print(scores)
print(my_score)
# практика
# из словаря сделать набор
my_score = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {v * 10 for k, v in my_score.items()}

print(scores)
print(my_score)
# из словаря список
my_score = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = [v * 10 for k, v in my_score.items()]

print(scores)
print(my_score)
# новый словарь из списка
my_score = [10, 7, 14]

scores = {index: element * 2 for index, element in enumerate(my_score)}

print(scores)
# задача
dict_for_practice = {
    'name': 'artem',
    'surname': 'iskom',
    'age': '27'
}

new_dict = {k: v.title() for k, v in dict_for_practice.items()}
print(new_dict)
# задача 2

list_for_practice = ['abc1', 'tre', 'asd56', '12']

new_list = [value for value in list_for_practice if len(value) > 3]

print(list_for_practice)
print(new_list)
