def my_fn():
    global a
    a = 10


my_fn()

print(a)
###########################
a = 10


def my_fn():
    global a
    a = 15


my_fn()

print(a)
