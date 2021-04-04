from time import time
from termcolor import colored


class TrafficLight:
    __dt = {'red': 7.0, 'yellow': 2.0, 'green': 5.0, 'off': 0.5}
    __color = 'red'
    __is_running = False
    __is_check_ok = True
    __icons_str = {'red': u'\u25a1', 'yellow': u'\u25cb', 'green': u'\u25b7'}
    __id = list()

    def __init__(self, id_num=None, dt_red=None, dt_yellow=None, dt_green=None, dt_off=None):
        if id_num:
            if id_num not in TrafficLight.__id:
                self.__id = int(id_num)
            else:
                self.__id = max(TrafficLight.__id) + 1
        else:
            if TrafficLight.__id:
                self.__id = max(TrafficLight.__id) + 1
            else:
                self.__id = 1
        TrafficLight.__id.append(self.__id)
        if any([dt_red, dt_yellow, dt_green, dt_off]):
            self.__dt = dict()
            self.__dt['red'] = TrafficLight.__dt['red']
            self.__dt['yellow'] = TrafficLight.__dt['yellow']
            self.__dt['green'] = TrafficLight.__dt['green']
            self.__dt['off'] = TrafficLight.__dt['off']
        if dt_red:
            self.__dt['red'] = dt_red
        if dt_yellow:
            self.__dt['yellow'] = dt_yellow
        if dt_green:
            self.__dt['green'] = dt_green
        if dt_off:
            self.__dt['off'] = dt_off
        self.__cycle_period = sum(self.__dt.values()) - self.__dt['off']

    def get_id(self):
        return self.__id

    def running(self):
        start_time = time()
        self.__is_running = True
        prev_color = self.__color
        self.__is_check_ok = True
        while True:
            current_time = time()
            if self.__is_running:
                if (current_time - start_time) % self.__cycle_period < self.__dt['red']:
                    self.__color = 'red'
                    if prev_color != 'green' and prev_color != self.__color:
                        self.__is_check_ok = False
                    prev_color = 'red'
                    state_str = colored(f"{TrafficLight.__icons_str['red']}", 'red') + ' '
                    state_str += f"{TrafficLight.__icons_str['yellow']}" + ' '
                    state_str += f"{TrafficLight.__icons_str['green']}"
                elif (current_time - start_time) % self.__cycle_period - self.__dt['red'] < self.__dt['yellow']:
                    self.__color = 'yellow'
                    if prev_color != 'red' and prev_color != self.__color:
                        self.__is_check_ok = False
                    prev_color = 'yellow'
                    state_str = f"{TrafficLight.__icons_str['red']}" + ' '
                    state_str += colored(f"{TrafficLight.__icons_str['yellow']}", 'yellow') + ' '
                    state_str += f"{TrafficLight.__icons_str['green']}"
                else:
                    self.__color = 'green'
                    if prev_color != 'yellow' and prev_color != self.__color:
                        self.__is_check_ok = False
                    prev_color = 'green'
                    state_str = f"{TrafficLight.__icons_str['red']}" + ' '
                    state_str += f"{TrafficLight.__icons_str['yellow']}" + ' '
                    state_str += colored(f"{TrafficLight.__icons_str['green']}", 'green')
            else:
                if (current_time - start_time) % (2 * self.__dt['off']) < self.__dt['off']:
                    state_str = f"{TrafficLight.__icons_str['red']}" + ' '
                    state_str += f"{TrafficLight.__icons_str['yellow']}" + ' '
                    state_str += f"{TrafficLight.__icons_str['green']}"
                else:
                    state_str = f"{TrafficLight.__icons_str['red']}" + ' '
                    state_str += colored(f"{TrafficLight.__icons_str['yellow']}", 'yellow') + ' '
                    state_str += f"{TrafficLight.__icons_str['green']}"
            yield state_str

    def stop(self):
        self.__is_running = False
        self.__is_check_ok = False

    def is_check_ok(self):
        return self.__is_check_ok

    def is_running(self):
        return self.__is_running
