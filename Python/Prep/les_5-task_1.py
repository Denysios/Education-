# Функции создания директорий и удаления
import os

def create_dir():
    for i in range(1, 10):
        name_dir = f'dir_{i}'
        os.mkdir(name_dir)

#create_dir()

def del_dir():
    for i in range(1, 10):
        name_dir = f'dir_{i}'
        os.rmdir(name_dir)

#del_dir()