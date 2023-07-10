# int 0        false
# float 0.0    false
# complex 0j   false
# dict {}      false
# list []      false
# tuple ()     false
# set set()    false
# range range(0) false
# str ""       false


# bool         false
# NonType      None

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print(bool(''))

# двойное отрицание
print(not not {})


# ложные значения в условных инструкциях if
my_list = [1, 2]
if len(my_list) > 0:
    print(len(my_list) > 0)
    print("List has elements")  # так не пишут

my_list1 = [1, 2]

if my_list1:
    print("List has elements")  # так пишут
