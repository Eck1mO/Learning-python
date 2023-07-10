try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error = Division by zero!")

print('Continue...')

# информация об ошибке

try:
    print(10 / 0)
except ZeroDivisionError as e:
    # print(type(e))
    # print(dir(e))
    # print(e.__str__())
    print(e)

print("Continue...")

# разные типы ошибок в блоке except

try:
    print('10' / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    # print(type(e))
    print(e)

print("Continue...")

# блоки else и finally в обработке ошибок

try:
    print(10 / 5)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")
finally:
    print("Continue...")

# отсутствие типа ошибки и класс Exception

try:
    print(10 / 0)
except Exception as e:
    print(e)
    # or # но не рекомендуется применять , нет доступа к ошибке
try:
    print(10 / 0)
except:
    print("Some error occurred")


# создание ошибок

def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    divide_nums(10, 0)
except ValueError as e:
    print(e)

print('Continue...')

# задача


def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image '{img['image_title']}' has id {img['image_id']}"


print(image_info({'image_title': 'My cat', 'image_id': 123}))

try:
    print(image_info({'image_id': 123}))
except TypeError as e:
    print(e)

##########

img = {
    'image_title': 'abc',
    'image_id': 12
}

result = ''


def image(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Error")

    return f"Image '{img['image_title']}' has id {img['image_id']}"


try:
    print(image(img))
except TypeError as e:
    print(e)
