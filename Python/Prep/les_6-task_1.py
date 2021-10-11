# Сериализация

# 1: Создать модуль music_serialize.py. В этом модуле определить словарь
# для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json,
# group.pickle соответственно. В файле group.json указать кодировку utf-8.


import pickle
import json

# словарь данных о группе в виде списка
my_favorite_group = {
    'name': 'Кукрыниксы', 'year': '1997', 'style': 'pank-rock',
    'tracks': ['Движение', 'Дороги', 'Вертикаль', 'Обнимай', 'По раскрашенной душе'],
    'Albums': [{'name': "Раскрашенная душа", 'year': '2002'},
    {'name': "XXX", 'year': '2007'}]}

music_group = pickle.dumps(my_favorite_group)

# преобразуем объект в поток байтов с помощью pickle
with open('music_bytes.pickle', 'wb') as f:
    pickle.dump(music_group, f)

# преобразуем объект в формат json используя кодировку utf-8
with open('music_bytes.json', 'w', encoding='utf-8') as f:
    json_group = json.dump(my_favorite_group, f)

