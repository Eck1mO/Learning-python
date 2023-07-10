##############
# распаковка словаря
button = {
    'width': 200,
    'text': 'Buy',
    'collor': 'Gray'
}

red_button = {
    **button,
    'collor': 'red'
}


print(button)
print(red_button)

##########
# обьединение словарей

button_default = {
    'text': 'Buy'
}


button_style = {
    'collor': 'yellow',
    'width': 200,
    'height': 300
}

button = {
    **button_default,
    **button_style
}

print(button)

# or
button_default = {
    'text': 'Buy',
    'color': 'black',
    'width': 0,
    'height': 0
}


button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button_grap = {
    'info': 'Text',
    'cost': 1000,
    'age': 20,
    'color': 'green'
}


button = button_default | button_style | button_grap


print(button)
