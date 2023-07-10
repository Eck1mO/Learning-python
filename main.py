def dict_to_list(instance_dict):
    list_for_convertion = []
    for k, v in instance_dict.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list({'name': 123, 'surname': 'Poroshenko'}))

########################################################################


def filter_list(list_for_filter, type_of_value):
    new_list = []
    for elem in list_for_filter:
        if type(elem) == type_of_value:
            new_list.append(elem)
    return new_list


list1 = [1, 'abc', 20, True]


print(filter_list([1, 'abc', 20, True], int))
