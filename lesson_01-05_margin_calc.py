# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток —
# издержки больше выручки. Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = float(input('Input Revenue: '))
costs = float(input('Input Costs: '))
profit = revenue - costs
if profit > 0:
    print(f'Profit is {profit}')
    if revenue > 0:
        margin = profit / revenue
        print(f'Margin is {margin * 100:.1f}%')
        employees = int(input('Input employees number: '))
        if employees > 0:
            print(f'Profit per one employee is {profit / employees:.1f}')
elif profit < 0:
    print(f'Loss is {-profit}')
else:
    print('Financial result is zero, Costs equal Revenue')
