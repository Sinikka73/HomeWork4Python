"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]..
"""

first_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_lst = [first_lst[i] for i in range(1, len(first_lst)) if first_lst[i] >
           first_lst[i - 1]]
print(f'Исходный список: {first_lst}')
print(f'Результат: {new_lst}')