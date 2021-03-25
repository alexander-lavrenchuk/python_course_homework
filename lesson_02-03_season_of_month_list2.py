"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""
season_list = ['winter', 'winter',
               'spring', 'spring', 'spring',
               'summer', 'summer', 'summer',
               'autumn', 'autumn', 'autumn',
               'winter']
month_num = int(input('Input month number form 1 to 12: '))
while month_num < 1 or month_num > 12:
    print('Wrong month number. Try again.')
    month_num = int(input('Input month number form 1 to 12: '))
season = season_list[month_num - 1]
print(f'Season of month with number {month_num} is {season}')
