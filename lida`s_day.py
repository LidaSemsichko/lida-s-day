'''
Lida`s day edition
'''

start = '\n\
  _____                         _ _   _       _      _     _        \n\
 |  __ \                       (_) | | |     | |    (_)   | |         \n\
 | |  | | __ _ _   _  __      ___| |_| |__   | |     _  __| | __ _     \n\
 | |  | |/ _` | | | | \ \ /\ / / | __|  _ \  | |    | |/ _` |/ _` |    \n\
 | |__| | (_| | |_| |  \ V  V /| | |_| | | | | |____| | (_| | (_| |     \n\
 |_____/ \__,_|\__, |   \_/\_/ |_|\__|_| |_| |______|_|\__,_|\__,_|      \n\
                __/ |                                                  \n\
               |___/                                                      \n\
'

import random
import time

def prime(fn):
    '''
    decorator. starting generator
    '''
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class LidaDay:
    '''
    Lida`s day
    '''
    def __init__(self) -> None:

        self.hour = 8
        self.study_hours = 0
        self.sleep_time = 0
        self.doom_hours = 0
        self.day_end = False

        self.start = self._start()

        self.relaxing = self._relaxing()
        self.sleep = self._sleep()
        self.eat_ice_cream = self._eat_ice_cream()
        self.studying_descrete = self._studying_descrete()
        self.reading_calculus = self._reading_calculus()

        self.state = self.start

    @prime
    def _start(self):
        """
        choose the start
        """
        while True:

            event = yield
            print(typing("Привіт! Ось і початок дня Ліди."))
            print(typing("_"*30))
            print(typing("_"*30))
            print(typing("_"*30))

            print(typing("Ліда прокинулася. Потягнулася. Цікаво, який же сьогодні буде день"))
            print(typing(f"Першим ділом Ліда вирішила- {event}"))
            self.hour += 1

            if event == "Подивитися Ютуб":
                print(typing("Ого, тільки ранок, а вже відпочивати. На жаль, Ліда не може дивитися Ютуб, бо ще не повчилася сьогодні"))
                self.state = self.studying_descrete

            if event == "Справи буденні":
                print(typing("Ти ж тільки прокинулася, не час знову лягати. Краще прогулятися  у парку і поїсти Файні Льоди"))
                self.state = self.eat_ice_cream

            if event == "Навчання":
                print(typing("Гарна ідея, вже почалася сесія, треба повчитися. Сідаємо за дискретну математику"))
                self.state = self.studying_descrete

    @prime
    def _sleep(self):
        """
        Lida is sleeping
        """
        while True:

            event = yield
            print(typing("Ліда дуже втомилася і хоче спати"))
            print(typing("_"*30))
            print(typing("zzzz...."))
            print(typing("_"*30))
            print(typing("Ліда знову прокинулася"))
            print(typing(f"Що ж робити далі? Ліда вирішила- {event}"))
            self.hour += 1
            self.sleep_time += 1

            if event == "Подивитися Ютуб":
                print(typing("На жаль, Ліда не може дивитися Ютуб, бо тільки прокинулася"))
                self.state = self.studying_descrete

            if event == "Справи буденні":
                print(typing("Що, знову спати? Ми ж тільки прокинулися. Давай краще почитаємо теореми з мат аналізу"))
                self.state = self.reading_calculus

            if event == "Навчання":
                print(typing("Навчання після сну не надто продуктивне. Давай краще поїмо Файних Льодів"))
                self.state = self.eat_ice_cream

    @prime
    def _relaxing(self):
        """
        Lida is Подивитися Ютуб
        """
        while True:

            event = yield
            print(typing("Зараз буде відпочинок. ООО, вийшло нове відео!"))

            print(typing(f"Ліда вирішила- {event}"))
            self.hour += 1
            self.doom_hours += 1

            if event == "Подивитися Ютуб" and self.study_hours:
                print(typing("Ще є трошки часу подивитися Ютуб."))
                self.state = self.relaxing

            if event == "Справи буденні":
                print(typing("Відео виявилося дуже нудним і Ліда заснула до наступного ранку"))
                print(typing("День закінчився"))
                break

            if event == "Навчання":
                print(typing("Ліда набралася сил та нарешті вирішила пійти вчити доведення з мат аналізу"))
                self.state = self.reading_calculus

    @prime
    def _eat_ice_cream(self):
        """
        Lida is eating Файні Льоди
        """
        while True:

            event = yield
            print(typing("Ліда пройшлася Стрийським парком. Поїла морозива"))
            print(typing(f"І тут раптово вирішила- {event}"))
            self.hour += 1

            if event == "Подивитися Ютуб":
                print(typing("Ліда не дуже хоче дивитися Ютуб. Вона стомилася, пійде спати"))
                self.state = self.sleep

            if event == "Справи буденні":
                print(typing("Ліда знову пішла спати. Отож, гарних снів)"))
                self.state = self.sleep

            if event == "Навчання":
                print(typing("Якась тяга до вивчення дискретної математики. Гайда вчитися"))
                self.state = self.studying_descrete

    @prime
    def _studying_descrete(self):
        """
        Lida is studying descrete
        """
        while True:

            event = yield
            print(typing("Ліда пішла вчити дискретну математику"))
            print(typing(f"Досконало освоїла новий алгоритм і вирішила -  {event}"))
            self.study_hours += 1
            self.hour += 1

            if event == "Подивитися Ютуб" and self.study_hours >= 4:
                print(typing("Нарешті Ліда достатньо повчилася і може подивитися Ютуб"))
                self.state = self.relaxing

            if event == "Подивитися Ютуб" and self.study_hours < 4:
                print(typing("Ой, сесія на носі. Треба спочатку повчитися"))
                event = self.reading_calculus

            if event == "Справи буденні":
                print(typing("Ух, як стомилася. Ліда пішла спати"))
                self.state = self.sleep

            if event == "Навчання":
                print(typing("Давай тепер повчимо мат аналіз"))
                self.state = self.reading_calculus

    @prime
    def _reading_calculus(self):
        """
        Lida is reading calculus theoremes
        """
        while True:

            event = yield
            print(typing("Ліда пішла вчити доведення"))
            print(typing(f"Прочитала 3 і вирішила- {event}"))
            self.started = True
            self.study_hours += 1
            self.hour += 1

            if event == "Подивитися Ютуб" and self.study_hours >= 4:
                print(typing("Можна і відпочити"))
                self.state = self.relaxing

            if event == "Подивитися Ютуб" and self.study_hours < 4:
                print(typing("Ще рано відпочивати. Треба повчитися, сессія на носі"))
                event = self.studying_descrete

            if event == "Справи буденні" or event == "Навчання":
                print(typing("Ліда зголодніла, час поїсти морозива і прогулятися парком"))
                self.state = self.eat_ice_cream

    def send(self, action):
        '''
        send
        '''
        try:
            self.state.send(action)
        except StopIteration:
            self.day_end = True

def typing(text: str, indent_level: int = 0, interval: float = 0.005):
    """
    Creative text output in terminal with indentation
    """
    indent = "    " * indent_level
    for i in text:
        if i == " ":
            print(" ", end="", flush=True)
            time.sleep(interval * 0.5)
        else:
            print(i, end="", flush=True)
            time.sleep(interval)
    print()
    return indent


def Lida_day(hours: int):
    """
    lida`s day
    """
    print(start)
    day = LidaDay()

    for i in range(hours):

        if day.day_end:
            break

        print(typing(f"Година - {i + 1}:00"))
        event =  random.choice(["Подивитися Ютуб", "Справи буденні", "Навчання"])

        day.send(event)
        print(typing("-"*30))

    print(typing("Статистика дня :"))
    print(typing(f"Годинки в ютубчику: {day.doom_hours}"))
    print(typing(f"Годинки навчання: {day.study_hours}"))
    print(typing(f"Годинки сну: {day.sleep_time}")) 

if __name__ == "__main__":
    Lida_day(24)
