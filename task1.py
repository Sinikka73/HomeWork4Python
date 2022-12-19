"""
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary_func(arg_b, arg_c, arg_d):
    """
    функция расчёта з.п
    :param arg_b: выработка в часах
    :param arg_c: ставка в час
    :param arg_d: премия
    """

    print(f'выработка в часах: {arg_b} ')
    print(f'ставка в чaс, руб: {arg_c} ')
    print(f'премия, руб: {arg_d} ')
    print(f'заработная плата: {int(arg_b) * int(arg_c) + int(arg_d)} '
          f'руб')


script_name, work_time, hourly_rate, premium = argv
print("Имя скрипта", script_name)
try:
    salary_func(work_time, hourly_rate, premium)
except ValueError:
    print("Вы ввели недостаточно данных")


