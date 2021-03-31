"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
data_file_name = 'data_7.log'
report_file_name = 'firms_results.json'
report_totals = 'average_profit'
with open(data_file_name) as file_obj:
    report = []
    firms_results = dict()
    avg_profit = 0
    for line in file_obj:
        firm_par = line.split()
        firms_results.update({firm_par[0]: float(firm_par[2]) - float(firm_par[3])})
        sum_profit_results = 0
        count_profit_results = 0
    for i in range(len(firms_results)):
        profit = firms_results.get(list(firms_results.keys())[i])
        if profit > 0:
            sum_profit_results += profit
            count_profit_results += 1
        avg_profit = sum_profit_results / count_profit_results if count_profit_results > 0 else avg_profit
    report.append(firms_results)
    report.append({report_totals: avg_profit})
    with open(report_file_name, 'w') as out_file:
        json.dump(report, out_file)
