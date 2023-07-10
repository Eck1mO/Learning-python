# if
# if...else
# if...elif
# тернарный оператор(используется в выражении)

# if
my_number = 25
if my_number > 0:
    print(my_number, "is positive number")
#######################################
person_info = {
    'age': 20
}

if not person_info.get('name'):
    print("Name is absent")
########################################
num_one = 10
num_two = 5.3
if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Both numbers are ints and positive")

# if else
my_number = 21.5
if type(my_number) is int:
    print(my_number, "is unteger")
else:
    print(my_number, "is not an integer")
##########################################
my_phone = {
    'price': 200
}
if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")

# if elif
my_number = -10

if my_number > 0:
    print(my_number, "is positive number")
elif my_number < 0:
    print(my_number, "is negative number")
else:
    print(my_number, "is zero")

# использование if в функциях


def nums_info(a, b):  # лучше писать так
    if (type(a) is not int) or (type(b)) is not int:
        return "One of arguments not int"
    if a >= b:
        return f"{a} >= {b}"
    return f"{a} < {b}"


print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))
#####################


def nums_info(a, b):
    if (type(a) is not int) or (type(b)) is not int:
        info = "One of arguments not int"
    elif a >= b:
        info = f"{a} >= {b}"
    else:
        info = f"{a} < {b}"
    return info


# задача
# мое решение
dict_info = {
    'distance': 100,
    'speed': 20,
    'time': 60
}


def route_info(opt):
    if not not isinstance(opt['distance'], int):
        return f"Distance to your destination is {opt['distance']}"
    if not not opt['speed'] and opt['time']:
        return f"Distance to your destination is {opt['speed'] * opt['time']}"
    return f"No distance info is available"


print(route_info(dict_info))
# решение Богдан


def route_info(route):
    if ('distance' in route) and isinstance(route['distance'], int):
        return f"Distance to your destination is {route['distance']}"
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"
    return f"No distance info is available"


print(route_info({'distance': 100}))
print(route_info({'speed': 75, 'time': 20}))
print(route_info({'my_speed': 21}))
# or


def route_info(route):
    if ('distance' in route) and isinstance(route['distance'], int):
        route_info = f"Distance to your destination is {route['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info = f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        route_info = f"No distance info is available"
    return route_info


print(route_info({'distance': 100}))
print(route_info({'speed': 75, 'time': 20}))
print(route_info({'my_speed': 21}))
