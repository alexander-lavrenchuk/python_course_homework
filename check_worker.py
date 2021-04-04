"""
3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

from worker_position import *
emp_1 = Position('Leo', 'Tought', 'Programmer', {'wage': 10000, 'bonus': 11000})
emp_2 = Position('Max', 'Flint', 'Head', {'wage': 20000, 'bonus': 12000})
emp_3 = Position('Lui', 'Lee', 'CEO', {'wage': 30000, 'bonus': 13000})

print(emp_1.get_full_name(), emp_1.position, emp_1.get_total_income())
print(emp_2.get_full_name(), emp_2.position, emp_2.get_total_income())
print(emp_3.get_full_name(), emp_3.position, emp_3.get_total_income())
