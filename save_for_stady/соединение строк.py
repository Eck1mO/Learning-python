# f-string

hello = 'Hello'
world = 'World'

greeting = f"{hello} {world}"

print(greeting)

###########################
my_name = 'Artem'
my_hobby = 'computer'
time = 8

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + ' o\'clock '

print(info)

#########################################
# в f строках можно использовать значения других типов без конвертации
my_name = 'Artem'
my_hobby = 'computer'
time = 8
list1 = [1, 'abc', [1, 4, 2]]


info1 = f"{my_name} likes {my_hobby} at {time} o\'clock {list1}"


print(info1.title())
