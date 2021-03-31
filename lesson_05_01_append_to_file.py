"""
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""
output_file_name = 'data_1.log'
print('Enter string for log or empty string to end the program.')
string_num = 0
file_mode = 'w'
while True:
    string_num += 1
    file_mode = 'a' if string_num > 1 else file_mode
    user_input = input(f'String {string_num}: ')
    if not user_input:
        break
    try:
        with open(output_file_name, file_mode) as file_obj:
            file_obj.write(user_input + '\n')
    except IOError:
        print('I/O Error!')
print(f'Check file {output_file_name} for saved inputs.')
