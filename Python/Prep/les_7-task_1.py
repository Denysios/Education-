# Нужно перевести 'слово' в 'СлОвО' (Нечетные буквы в слове изменить на заглавные)
word = 'слово'
result = []

for i in range(len(word)):
    # Решение с помощью конструкции if, else
    # if i%2 != 0:
    # letter = word[i].lower()
    # else:
    # letter = word[i].upper()

    # Решение с помощью тернарного оператора
    letter = word[i].lower() if i % 2 != 0 else word[i].upper()

    result.append(letter)

result = ''.join(result)
print(result)