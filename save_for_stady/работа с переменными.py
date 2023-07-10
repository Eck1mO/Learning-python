#########################
# создание копии обьекта

def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increase_person_age(person_one)
print(new_person['age'])
print(person_one['age'])

############################
# передача изменяемых обьектов


def increase_person_age(person):
    print(id(person))
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one))

increase_person_age(person_one)
print(person_one['age'])

###########################################
# example


def merge_list_to_dict(a, b):
    y = zip(a, b)
    # print(y)
    c = dict(y)
    # print(c)
    return (c)


d = ['Petro', 'Egor', 'Makar']
c = [13, 14, 12]

result = (merge_list_to_dict(d, c))
print(result)

t = ['Petro', 'Egor', 'Makar']
y = [13, 14, 12]

result_1 = (merge_list_to_dict(t, y))
print(result_1)

#################################################
# наименьшая функция


def res():
    pass


print(res)
