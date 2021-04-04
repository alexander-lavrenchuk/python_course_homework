"""
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from trafficlight import *

dt = 0.5  # Modeling time interval in seconds. Use dt = 7.5 for error check state test.
test_period = 300  # Maximum modeling time in seconds
tl_1 = TrafficLight()
msg_beg = '\nWrong state for traffic light with id: '
msg_end = ' detected. Try to run the model with less time interval dt.'

t_0 = time()
gen_tl_1 = tl_1.running()
print("\033[?25l", end='', flush=True)  # Hide cursor
while True:
    s = '\r'
    s += ' ' * 5
    s += next(gen_tl_1)
    print(s, end='', flush=True)

    if tl_1.is_running() and not tl_1.is_check_ok():
        print(msg_beg + str(tl_1.get_id()) + msg_end)
        break
    if time() - t_0 > test_period:
        break
    sleep(dt)
print('\nThe program has been terminated.')
print("\033[?25h", end='\n', flush=True)  # Show cursor
