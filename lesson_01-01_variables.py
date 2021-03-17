"""
Поработайте с переменными, создайте несколько, 
выведите на экран. Запросите у пользователя 
некоторые числа и строки и сохраните в переменные, 
затем выведите на экран.
"""

name = 'Computer'
age = 2
weight = 1.7
is_human = False

print(f"Hello, my name is {name}. I'm {age} years old. My weight is {weight} kg. Am I a human being? {is_human}")

name = input("What's your name? ")
age = int(input('How old are you? '))
weight = float(input('What is your weight? '))
is_human = not is_human
print(f"Your name is {name}. You're {age} years old. Your weight is {weight:.1f} kg. Are You a human being? {is_human}")
