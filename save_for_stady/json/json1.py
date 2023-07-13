# json - формат обмена данными и формат файлов(javascript object natation)
# допустимые типы значений в json: string, number, json object, boolean, array, null
# передача данных в формате json передается в виде строки

# конвертация json в словарь
import json

json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'

sneakers = json.loads(json_str)

print(type(sneakers))
print(sneakers)

print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])

# если json массив
json_array = '[1, 2, 3]'

my_list = json.loads(json_array)

print(my_list)
# конвертация словаря в json

json_form_dict = json.dumps(sneakers, indent=1)

print(json_form_dict)
print(type(json_form_dict))
# задача

my_dict = {
    'name': 'Artem',
    'surname': 'Iskom',
    'age': 27
}

dict_on_json = json.dumps(my_dict, indent=1)

print(type(dict_on_json))
print(dict_on_json)
# из json в словарь
converted_json = json.loads(dict_on_json)
print(converted_json)
