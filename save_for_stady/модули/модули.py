# модули позволяют избегать дублирования блоков кода
# любой файл с раширением .py является модулем
# для импорта из другого модуля нужно использовать import

import module_one  # импорт пишется всегда вверху файла один под одним


def print_name(name):
    print(name)

    ###############################


# import module_one as m_one - переименование модуля
# from module_one import print_name можно импортировать только определенные переменные
# from module_one import * - доступ ко всем переменным

print(type(module_one))
print(dir(module_one))

module_one.print_name('Igor')
# m_one.print_name('Igor') - новое обращение при переименовании модуля
# print_name('Igor')
