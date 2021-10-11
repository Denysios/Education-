# Игра сражение

# запрос имени пользователя
player_name = input('Введите имя игрока')
# создание словаря игрока
player = {
    'name' : player_name,
    'health' : 100,
    'damage' : 50,
    'armor' : 1.2
}
# запрос имени врага
enemy_name = input('Введите имя врага')
# создание словаря врага
enemy = {
    'name' : enemy_name,
    'health' : 50,
    'damage' : 30,
    'armor' : 1.2
}
# health - здоровье; damage - урон; armor - броня

# функция атаки
def attack (unit, target):
    target ['health'] -= unit ['damage'] / unit ['armor']
    # так же можно записать вот так
    # target ['health'] = target ['health'] - unit ['damage'] / unit ['armor']

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)