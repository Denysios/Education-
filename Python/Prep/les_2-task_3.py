# Вывести эл-ты списка, кот не повторяются
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
unique_number = []

for i in my_list_1:
    if my_list_1.count(i) < 2:
        unique_number.append(i)

print(unique_number)
