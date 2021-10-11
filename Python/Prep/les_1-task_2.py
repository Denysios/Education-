# Цикл while с выходом break, если условие выполнится
while True:
    number = int(input('Enter number'))
    if 0 < number < 10:
        number = number ** 2
        print(number)
        break
    else:
        print('Введено неверное значение. Введите число от 1 до 9 включительно')