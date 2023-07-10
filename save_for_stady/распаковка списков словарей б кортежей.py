# распаковка словаря
dict1 = {
    'item': 'Banana',
    'collor': 'yellow'
}

dict2 = {
    'weight': '12g',
    'style': 'green'
}

all_dict = {
    **dict2,
    **dict1,
    'cost': 12
}

print(dict1 | dict2)
print(all_dict)

# распаковка словаря в именованные аргументы
# в этом случаче не может быть в словаре больше 2 ключей
user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))  # or
# or позиционные аргументы
print(user_info(user_profile['name'], user_profile['comments_qty']))
print(user_info(name=user_profile['name'],
      comments_qty=user_profile['comments_qty']))


# распаковка списков, кортежей
my_fruits = ['apple', 'banana', 'lime']
my_apple, my_banana, my_lime = my_fruits

print(my_apple)
print(my_banana)
print(my_lime)
# использование * при распаковке
my_vegetables = ['kartoha', 'pomidor', 'tikva']
my_kartoha, *remaining_vegetables = my_vegetables

print(my_kartoha)
print(remaining_vegetables)
# распаковка списка в позиционные аргументы
# в списке так же должно быть 2 элемента
user_data = ['Bogdan', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))
# так тоже можно
# my_name, my_comments_qty = user_data
# print(user_info(my_name, my_comments_qty))
