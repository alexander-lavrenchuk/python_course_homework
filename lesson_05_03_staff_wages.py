"""
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
wage_level = 2e4
try:
    with open('data_3.log') as file_obj:
        staff_wages = file_obj.readlines()
except IOError:
    print('I/O Error!')
if staff_wages:
    staff_dict = dict()
    staff_under_level = []
    for line in staff_wages:
        name, wage = line.split()
        if staff_dict.keys().__contains__(name):
            print(f'There more than one staff persons with the same name {name}. '
                  f'Only the last entry has been taken into account.')
        staff_dict.update({name: float(wage)})
    avg_wage = sum(staff_dict.values()) / len(staff_wages)
    staff_under_level = [staff for staff in staff_dict.items() if staff[1] < wage_level]
    print(f'These employees has wage under {wage_level:.2f} rubles per month:')
    for el in range(len(staff_under_level)):
        print(staff_under_level[el][0])
    print(f'Average wage is {avg_wage:.2f}')
