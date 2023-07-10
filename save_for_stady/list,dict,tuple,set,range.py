my_list = [10, 20, 30]
print(my_list)
print(type(my_list))

#############################################

my_dict = {
    'id': 10,
    'name': 'Petro'
}
print(my_dict)
print(type(my_dict))

##############################################

my_tuple = (10, 20, 20, 30)
print(my_tuple)
print(type(my_tuple))

###############################################
my_set = {10, 'abc', 10, True}
print(my_set)
print(type(my_set))

my_set = {12, 11, 155, 123}
my_set.add(111)

print(my_set)

other_set = {12, 111, 22, 343}

print(my_set & other_set)

new_set = list(my_set & other_set)

print(new_set)

####################################################
my_range = range(1, 100, 10)
print(type(my_range))
my_list = []


for n in range(1, 100, 10):
    my_list.append(n)

# for n in my_range:
#     my_list.append(n)
#     print(my_list)


print(my_list)


print(my_range.start)
print(my_range.stop)
