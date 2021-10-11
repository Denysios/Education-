# Пользователь вводит дату в формате dd.mm.yyyy, программа выводит буквенное значение даты
date = input('Введите дату чрез точку в формате dd.mm.yyyy, например 13.07.1968')
dd, mm, yyyy = date.split('.')
print(f'Вы ввели {dd}, {mm}, {yyyy}')
days = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое',
    '08': 'восьмое', '09': 'девятое',
    '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
    '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое',
    '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
months = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
    '08': 'августа', '09': 'сентября',
    '10': 'октября', '11': 'ноября', '12': 'декабря'}

result = f'{days[dd]} {months[mm]} {yyyy} года'
print(result)
