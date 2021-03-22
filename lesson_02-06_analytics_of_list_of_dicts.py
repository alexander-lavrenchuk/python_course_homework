"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ
— характеристика товара, например, название. Тогда значение — список значений-характеристик, например,
список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""
# dict_1 = {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}
# dict_2 = {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}
# dict_3 = {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}
# tuple_1 = (1, dict_1)
# tuple_2 = (2, dict_2)
# tuple_3 = (3, dict_3)
# products_list = [tuple_1, tuple_2, tuple_3]

product_num = 0
products_list = list()
product_dict = dict()
is_entering_new_product = True
while is_entering_new_product:
    product_num += 1
    print(f'Entering characteristics dictionary for product number {product_num} ...')
    user_answer = ''
    is_entering_new_characteristics = True
    while is_entering_new_characteristics:
        key = input("Enter product's characteristics name: ")
        value = input("Enter product's characteristics value: ")
        product_dict.update({key: value})
        print(f"Product's number {product_num} characteristics dictionary has updated {(product_num, product_dict)}")
        while user_answer.lower() != 'y' and user_answer.lower() != 'n':
            user_answer = input("Would You like to add/update another product's characteristics (y/n)? ")
        is_entering_new_characteristics = (False, True)[user_answer == 'y']
        user_answer = ''
    products_list.append((product_num, product_dict))
    print(f'Products list has updated {products_list}')
    product_dict = dict()
    while user_answer.lower() != 'y' and user_answer.lower() != 'n':
        user_answer = input('Would You like to add another product (y/n)? ')
    is_entering_new_product = (False, True)[user_answer == 'y']
print(f"You've entered characteristics dictionar{('y', 'ies')[product_num>1]} for {product_num} "
      f"{('product', 'products')[product_num>1]}.")
print(f'Product list is {products_list}')

analytics_dict = dict()
keys_set = set()
value_set = set()
for product in products_list:
    product_dict = product[1]
    for key in product_dict.keys():
        keys_set.add(key)
for key in keys_set:
    value_set.clear()
    for product in products_list:
        product_dict = product[1]
        value = product_dict.get(key)
        value_set.add(value)
        analytics_dict.update({key: list(value_set)})
print('\nAnalyzing products data...\n\nProducts data analitics:')
print(analytics_dict)
