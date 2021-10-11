# Десериализация

import pickle
import json


# открытие и чтение объекта байт из файла модуля pickle, записанного ранее
with open('music_bytes.pickle', 'rb') as f:
    my_favorite_group = pickle.load(f)
    print(type(my_favorite_group), my_favorite_group)

# открытие и чтение объекта из файла модуля json, записанного ранее
with open('music_bytes.json', 'r') as f:
    json_group = json.load(f)
    print(type(json_group), json_group)
