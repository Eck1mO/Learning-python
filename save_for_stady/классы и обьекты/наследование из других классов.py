class ExtendedList(list):  # указываем родительский класс для нашего класса
    # следовательно на класс будет подклассом класса list
    def print_list_info(self):  # добавляем метод, при этом
        # метод __init__ родительского класса вызывается автоматически
        print(f"List has {len(self)} elements")  # возвращаем строку


custom_list = ExtendedList([3, 5, 2])
custom_list.print_list_info()

custom_list.append(7)
custom_list.print_list_info()

# custom_list - обьект, является экземпляром класса ExtendedList, наследует атрибуты ExtendedList
# ExtendedList - подкласс класса list, наследует атрибуты list
# list - подкласс класса object, наследует атрибуты object
