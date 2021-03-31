"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
in_file = 'data_4_en.log'
out_file = 'data_4_ru.log'
num_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
             'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
num_trans_keys = list(num_trans.keys())
try:
    with open(in_file) as file_obj:
        content_en = file_obj.readlines()
except IOError:
    print('I/O Error!')
if content_en:
    content_ru = []
    for line in content_en:
        for i in range(len(num_trans)):
            line = line.replace(num_trans_keys[i], num_trans.get(num_trans_keys[i]))
        content_ru.append(line)
    try:
        with open(out_file, 'w') as out_file_obj:
            out_file_obj.writelines(content_ru)
    except IOError:
        print('I/O Error!')
