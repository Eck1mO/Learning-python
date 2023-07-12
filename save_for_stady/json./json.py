# json - формат обмена данными и формат файлов(javascript object natation)
# допустимые типы значений в json: string, number, json object, boolean, array, null
# передача данных в формате json передается в виде строки

# конвертация json в словарь
import json

json_str = '{"id":235, "brand": "Nike","qty":84, "status": {"isForSale":true}}'

sneakers = json.loads(json_str)

print(type(sneakers))
print(sneakers)

print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status'], ['isForSale'])

# конвертация словаря в json
