"""
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
data_file_name = 'data_6.log'


def dig_trunc(str_num):
    res = ''
    for d in str_num:
        if d.isdigit():
            res += d
        else:
            break
    return int(res) if len(res) > 0 else 0


with open(data_file_name) as file_obj:
    subjects = dict()
    for line in file_obj:
        sub_name, lec_hours, pra_hours, lab_hours = line.split()
        subjects.update({sub_name: dig_trunc(lec_hours) + dig_trunc(pra_hours) + dig_trunc(lab_hours)})
print(subjects)
