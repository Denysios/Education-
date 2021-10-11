# Подключаемый модуль к программе файл. менеджера

import os
import shutil
import datetime


# Step by 1
# Create file
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Step by 2
# Create folder
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'Папка "{name}" уже существует')


# Step by 3
# Просмотр списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Step by 4
# Функция удаления файла или папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Step by 5
# Функция копирования файла или папки
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print(f'Папка "{new_name}" уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


# Проверяем работу (при импорте if __name__ == '__main__' не будет выполняться)
if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('folder_1')
    get_list()
    get_list(True)
    delete_file('folder_1')
    delete_file('text.dat')
    copy_file('new_folder', 'copy_new_folder')
    copy_file('just_file.dat', 'new_just_file.dat')
    save_info('Проверка работы функции save_info')
