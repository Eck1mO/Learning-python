my_dict = {}

for _ in range(3):
    num = input("Ведите ваше название ключа: ")
    name = input("Введите ваше значение: ")
    my_dict[num] = name


my_dict['vasia'] = 'pidor'
my_dict['petia'] = 'krasava'

del my_dict['vasia']


print(len(my_dict))

print(my_dict)
