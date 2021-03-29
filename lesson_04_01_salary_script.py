"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
params = argv
try:
    this_script_name = params[0]
    worked_hours = int(params[1])
    hour_rate = float(params[2])
    bonus = float(params[3])
    print(f'Worked hours: {worked_hours}\n'
          f'Hour rate: {hour_rate}\n'
          f'Bonus: {bonus}\n'
          f'Total wages: {worked_hours * hour_rate + bonus}')
except ValueError:
    print('Entered wrong script params.\n'
          'This script use only free params:\n'
          'integer number of worked hours,\n'
          'float value of hour rate and\n'
          'float value of bonus.\n'
          'Please, restart the script with correct parameters entered.')
