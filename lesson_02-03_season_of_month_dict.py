"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""
season_dict = {12: 'winter', 1: 'winter', 2: 'winter',
               3: 'spring', 4: 'spring', 5: 'spring',
               6: 'summer', 7: 'summer', 8: 'summer',
               9: 'autumn', 10: 'autumn', 11: 'autumn'}
month_num = int(input('Input month number form 1 to 12: '))
while month_num < 1 or month_num > 12:
    print('Wrong month number. Try again.')
    month_num = int(input('Input month number form 1 to 12: '))
season = season_dict.get(month_num)
print(f'Season of month with number {month_num} is {season}')
