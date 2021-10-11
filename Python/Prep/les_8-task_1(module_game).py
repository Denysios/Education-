# Скрипт. Задача-игра, Юзер угадывает число
import random


def game_user():
    print('Компьютер загадал число от 1 до 100, попробуйте отгадать')
    random_number = random.randint(1, 100)
    user_answer = None

    while user_answer != random_number:
        user_answer = int(input('Введите число: '))
        if user_answer > random_number:
            print(f'Число {user_answer}, больше загаданного')
        elif user_answer < random_number:
            print(f'Число {user_answer}, меньше загаданного')

    print(f'Вы победили! Загаданное число {random_number}. Сыграем ещё?')

if __name__ == '__main__':
    game_user()
