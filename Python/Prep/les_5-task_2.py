# Подключение собственного модуля
#
# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2
# сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и
# проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

# сделан импорт только модуля целиком из задания 2

# 1) файл main.py

import randtest


print(randtest.random_element([5, 6, 7, 8]))
print(randtest.random_element([]))

# 2) файл randtest.py

import random


def random_element(list1):
    if list1:
        result = random.choice(list1)
        return result


if __name__ == '__main__':
    print(random_element([1, 2, 3, 4]))
    print(random_element([]))
