from time import sleep
from trafficlight import *

dt = 0.5  # Modeling time interval in seconds. Use dt = 4.5 for error check state test for the second traffic light.
test_period = 300  # Maximum modeling time in seconds
stop_period = 25  # Time in seconds from model start to stop the second traffic light
tl_1 = TrafficLight()
tl_2 = TrafficLight(dt_red=3, dt_yellow=1, dt_green=3)
msg_beg = '\nWrong state for traffic light with id: '
msg_end = ' detected. Try to run the model with less time interval dt.'

t_0 = time()
gen_tl_1 = tl_1.running()
gen_tl_2 = tl_2.running()
print("\033[?25l", end='', flush=True)  # Hide cursor
while True:
    s = '\r'
    s += ' ' * 5
    s += next(gen_tl_1)
    s += ' ' * 5
    s += next(gen_tl_2)
    print(s, end='', flush=True)

    if tl_1.is_running() and not tl_1.is_check_ok():
        print(msg_beg + str(tl_1.get_id()) + msg_end)
        break
    if tl_2.is_running() and not tl_2.is_check_ok():
        print(msg_beg + str(tl_2.get_id()) + msg_end)
        break
    if time() - t_0 > stop_period:
        tl_2.stop()
    if time() - t_0 > test_period:
        break
    sleep(dt)
print('\nThe program has been terminated.')
print("\033[?25h", end='\n', flush=True)  # Show cursor
