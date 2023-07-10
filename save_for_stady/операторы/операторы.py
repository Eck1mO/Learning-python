=  # оператор присвоения
+ - * /  # арифметические
== != < >  # сравнения
not and or is , is not, in , not in  # логические


a = 10
b = a

c = a + b
print(a is b)  # True
print(c is a)  # False
################################################################
a = [1, 2]
b = [1. 2]

print(a == b)
# одинаковые выражения только второе вызвано магическим методом
print(a.__eq__(b))

###############################################################
# унарные операторы

- my_number
+ my_number
not is_activated

my_num = 10

print(+my_num)  # 10
my_bool = True  # False
print(+my_bool)  # 1 # 0


my_num = 10
print(not my_num)

###################################################################
# бинарные операторы

a = 5
a + b
a += 5
a == b
a and b


#####################################################################
# инфиксная запись
a = True
a + b
a += 5
a or b
a > b

########################################################
# операторы in , not in

my_car = {
    'brand': 'Toyota',
    'price': 10_000
}

print('brand' in my_car)  # True
print('year' in my_car)  # False
print('year' not in my_car)  # True
