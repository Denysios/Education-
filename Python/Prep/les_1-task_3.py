#“Медицинская анкета”
name = input('Введите Ваше имя')
surname = input('Введите Вашу фамилию')
age = int(input('Введите Ваш возраст'))
weight = int(input('Введите Ваш вес'))

if age <= 30 and 50 <= weight < 120:
    print(name, surname, ' Вы в хорошем состоянии')
elif (30 < age <= 40) and (50 > weight or weight > 120):
    print(name, surname, ' Вам требуется заняться собой')
elif (age > 40) and (50 > weight or weight > 120):
    print(name, surname, ' Вам требуется врачебный осмотр')
else:
    print(name, surname, ' Вам бог поможет')