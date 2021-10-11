# игра, Юзер угадывает число на несколько инроков

import random

print('Компьютер загадал число от 1 до 100, попробуйте отгадать')
random_number = random.randint(1, 100)
user_answer = None
count = 0
level_dict = {1: 3, 2: 5, 3: 10 }

level = int(input('Выберете уровень сложности от 1 до 3: '))
max_count = level_dict[level]

users_count = int(input('Введите количество пользователей: '))
users = []
for i in range(users_count):
    user_name = input(f'Введите имя пользователя {i + 1}: ')
    users.append(user_name)
print(f'Играют: {users}')

is_winner = False
winner_name = None

while not is_winner:
    count = count + 1
    print(f'Попытка №{count}')
    if count > max_count:
        print('В следующий раз повезёт')
        break
    for user in users:
        print(f'Ход {user}')
        user_answer = int(input('Введите число:'))
        if user_answer == random_number:
            is_winner = True
            winner_name = user
        elif user_answer > random_number:
            print(f'Число {user_answer}, больше загаданного')
        elif user_answer < random_number:
            print(f'Число {user_answer}, меньше загаданного')
else:
    print(f'Победил {winner_name}! Загаданное число {random_number}. Сыграем ещё?')
