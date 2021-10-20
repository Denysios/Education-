# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

my_name = 'Denis'
print(type(my_name))
print(my_name)

my_age = 33
print(type(my_age))
print(my_age)

im_student = True
print(type(im_student))
print(im_student)

just_var = None
print(type(just_var))
print(just_var)

username = input('Как Вас зовут?: ')
print(f'Добро пожаловать {username}!')
like_num = int(input('Какое Ваше любимое число?: '))
print(f'Какое совпадение! Сегодня Бог единиц, ноликов и прочей неразберихи благоволит всем, у кого любимое число {like_num}!')
