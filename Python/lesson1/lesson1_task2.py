# Задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

# Простой способ, но с некоторыми недочетами
# time_sec = int(input('Введите время в секундах: '))
# minutes = time_sec // 60
# hours = minutes // 60
# sec = minutes % 60
# print(f'{hours}:{minutes}:{sec}')


# Cпособ c использованием конструкции if
time_sec = int(input('Введите время в секундах: '))

temp_hours = time_sec / 60 // 60
if temp_hours <= 0:
    hours = '00'
elif len(str(int(temp_hours))) == 1:
    hours = '0' + str(int(temp_hours))
else:
    hours = str(int(temp_hours))

temp_minutes = (time_sec // 60) - (time_sec / 60 // 60) * 60
if temp_minutes == 0:
    minutes = '00'
elif len(str(int(temp_minutes))) == 1:
    minutes = '0' + str(int(temp_minutes))
else:
    minutes = str(int(temp_minutes))

temp_second = time_sec % 60
if temp_second == 0:
    second = '00'
elif len(str(int(temp_second))) == 1:
    second = '0' + str(int(temp_second))
else:
    second = str(int(temp_second))

print(f'{hours}:{minutes}:{second}')
