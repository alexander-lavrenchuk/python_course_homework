# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('Please, enter a time in seconds: '))
max_time_in_seconds = 100 * 60 * 60 - 1
while time_in_seconds > max_time_in_seconds:
    print(f'Value should be less than {max_time_in_seconds + 1}. Try again.')
    time_in_seconds = int(input('Please, enter a time in seconds: '))
hours = time_in_seconds // 60 // 60
minutes = time_in_seconds // 60 - hours * 60
seconds = time_in_seconds % 60
print(f'{time_in_seconds} seconds is {hours:02d}:{minutes:02d}:{seconds:02d}')
