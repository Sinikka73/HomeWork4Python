"""
 Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения. Например, в первом задании
выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle
from itertools import count


def my_func_one(start_num, end_num):
    """
    функция генерирует целые числа
    :param start_num: начало
    :param end_num: завершение
    """
    for i in count(start_num):
        if i > end_num:
            break
        print(i)


def my_func_two(param_one, param_two):
    """
    функция повторяет элементы заданного списка
    :param param_one: список
    :param param_two: количество повторений
    """
    k = 1
    for j in cycle(param_one):
        if k > param_two:
            break
        print(j)
        k += 1



my_func_one(start_num=int(input("Задайте начальное значение: ")),
            end_num=int(input("Задайте конечное значение: ")))
my_lst = ["abc", "hello", "hi", "world"]
my_iter = int(input(f"Введите число итераций для заданного списка {my_lst}: "))
my_func_two(my_lst, my_iter)