# not (bool)
# and
# or

not 10  # False
not 0  # True
not 'abc'  # False
not ''  # True
not True  # False
not False  # True


not not 10  # True
not not 0  # False
not not 'abc'  # True
not not ''  # False
not not True  # True
not not False  # False

my_list = [1, 2]
print(not my_list)


# операторы короткого замыкания (short-circuit) or, and
# or - ищет правду(True) и возвращает значение
# and - ищут ложь(False) и возвращает значение
other_list = ['a', 'b']
print(my_list or other_list)
print(len(my_list) > 0 or other_list)
print(len(my_list) < 0 or other_list)

my_list1 = [1, 2]
my_dict = {}
print(my_list1 and my_dict)


my_list2 = [1, 2]
my_list2 and print("List is not empty")


##################################

dict1 = {
    'name': 'Vasia',
    'age': 20
}

dict2 = {
    'age': 20,
    'name': 'Vasia'
}


dict1 == dict2 and print("Словари одинаковы")
