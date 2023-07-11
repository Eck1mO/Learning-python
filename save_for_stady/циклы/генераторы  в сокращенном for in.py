# генератор - это последовательность элементов
from sys import getsizeof
nums = (3, 5, 10)

squares = (num * num for num in nums)

print(squares)
print(type(squares))
#########################################
squares = (num * num for num in range(6))

print(squares)
print(type(squares))

for num in squares:
    print(num)
#########################################
nums = [3, 5, 10]

gen = (num * num for num in nums)

squares = tuple(gen)

print(squares)
print(type(squares))
#########################################

squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))
print(type(squares_gen))
###
squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
print(type(squares_list))
# практика генераторы
squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))
print(type(squares_gen))

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break
####
squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
print(type(squares_list))
