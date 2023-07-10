# обычная функция
def mult(a, b):
    return a * b


print(mult(10, 5))

# лямбда функция + замыкание


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")
print(morning_greeting('Bogdan'))

evening_greeting = greeting("Good Evening")
print(evening_greeting('Bogdan'))

night_greeting = greeting("Good Night")
print(night_greeting('Artem'))
# practice
