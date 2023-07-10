a = 10


def my_fn():
    a = True
    b = 15
    print(a)
    print(b)


my_fn()

print(a)
print(b)
#####################################
a = 5


def my_fn():
    def inner_fn():
        print(a)
    inner_fn()


my_fn()
# S
