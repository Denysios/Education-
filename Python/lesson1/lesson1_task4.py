# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


user_number = int(input('Введите целое положительное число: '))
result = 0

while user_number > 0:
    if user_number % 10 > result:
        result = user_number % 10
    user_number = user_number//10


# while True:
#     user_number = int(input('Введите целое положительное число: '))
#     if user_number <= 0:
#         print('Вы ввели некорректное значение')
#     else:
#         result = max(str(user_number))
#         break

# while True:
#     user_number = int(input('Введите целое положительное число: '))
#     if user_number <= 0:
#         print('Вы ввели некорректное значение')
#     else:
#         list_num = list(str(user_number))
#         i = 0
#         result = 0
#         while i < len(list_num):
#             if int(list_num[i]) > result:
#                 result = int(list_num[i])
#             i += 1
#         break

print(result)
