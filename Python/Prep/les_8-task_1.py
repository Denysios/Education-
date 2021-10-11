# Консольный файловый менеджер

import os
import sys
from game import game_user
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, chdir

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду. Воспользуйтесь командой help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует аргумент: название нового файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует аргумент: название новой папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует аргумент: название файла который нужно удалить')
        else:
            delete_file(name)
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует аргумент: введите название папки')
        except FileNotFoundError:
            print('Отсутствует указанная директория')
        else:
            chdir(name)
    elif command == 'copy':
        if len(sys.argv) < 3:
            print('Отсутствуют аргументы [2][3]: название файлов, нового и копируемого')
        elif len(sys.argv) < 4:
            print('Отсутствует аргумент [3]: название копируемого файла')
        else:
            if sys.argv[2] in os.listdir():
                try:
                    name = sys.argv[2]
                    new_name = sys.argv[3]
                except Exception as err:
                    print(f'Что-то пошло не так. Доп. инфо: {err}')
                else:
                    copy_file(name, new_name)
            else:
                print('Название копируемого файла указано не верно')
    elif command == 'game':
        try:
            name = sys.argv[1]
        except IndexError:
            print('Oops')
        else:
            game_user()
    elif command == 'help':
        print('list - список папок и файлов')
        print('create_file - создать файл')
        print('create_folder - создать папку')
        print('delete - удалить папку или файл')
        print('copy - копирование папки или файла')
        print('change_dir - сменить директорию')
        print('game - игра "Угадай число"')


save_info('Конец')
