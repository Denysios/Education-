# пример использования универсальной функции
# в которую в качестве одного из параметров передаем другую функцию
def my_filter (numbers, function):
    result = []
    for number in numbers:
        if function (number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# передаем лямбда функцию в универсальную ф-ю
# лямбда функции записываются в одну строку
print(my_filter(numbers, lambda number: number % 2 == 0))
# функция выше выводит в консоль четный числа из списка

# эта ф-я выводит не четные числа
print(my_filter(numbers, lambda number: number % 2 != 0))

# эта ф-я выводит числа больше 4
print(my_filter(numbers, lambda number: number > 4))