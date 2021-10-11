# Удаление одного списка из другого
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)
print(my_list_1 - my_list_2)

print(my_list_1)