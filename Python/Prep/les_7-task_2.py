# Создать список случайных чисел

import random


# С помощью генератора списков
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# Классический метод
numbers_1 = []

for i in range(10):
    number = random.randint(1, 100)
    numbers_1.append(number)

print(numbers_1)
