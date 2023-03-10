"""
 Реализовать формирование списка, используя функцию range() и возможности
 генератора. В список должны войти четные числа от 100 до 1000
 (включая границы). Необходимо получить результат вычисления произведения
 всех элементов списка.
Подсказка: использовать функцию reduce().

"""

from functools import reduce

my_lst = [i for i in range(100, 1001) if i % 2 == 0]

my_res_sum = reduce((lambda x, y: x + y), my_lst)
my_res_mult = reduce((lambda x, y: x * y), my_lst)

print(my_res_sum)
print(my_res_mult)