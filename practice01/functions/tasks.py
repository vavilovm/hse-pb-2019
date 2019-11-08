from typing import List


"""
Задание 1.
Дан массив целых чисел. 
Необходимо изменить его, оставив числа из отрезка [l, r] и возведя их в квадрат.
"""


def transform_simple(arr: List[int], l: int, r: int) -> List[int]:
    result = []
    for el in arr:
        if l <= el <= r: #(l <= el) and (el <= r)
            result.append(el ** 2)
    return result


def transform_list_comprehensions(arr: List[int], l: int, r: int) -> List[int]:
    return [el**2 for el in arr if l <= el <= r]


def transform_generators(arr: List[int], l: int, r: int) -> List[int]:
    return list(map(lambda x: x ** 2, filter(lambda x: l <= x <= r, arr)))


"""
Задание 2.
Дан двумерный массив чисел. 
Нужно посчитать сумму квадратов чисел, кратных двум.
"""


def conditional_sum_2d_simple(arr: List[List[int]]) -> int:
    pass


def conditional_sum_2d(arr: List[List[int]]) -> int:
    pass


"""
Задание 3.
Дан массив. 
Требуется перевернуть подотрезок массива [l, r].
"""


def reverse_array(arr: list, l: int, r: int) -> list:
    pass


"""
Задание 4.
Дана строка. 
Если ее длина хотя бы 3, добавить в конец 'ing. 
Если же строка уже заканчивается на 'ing', то добавить в конец 'ly'.
Пример входа: 'read'
Пример выхода: 'reading'
"""


def verbing(s: str) -> str:
    pass


""" 
Задание 5.
Даны два списка a и b.
Требуется разбить оба списка на две части, а затем склеить их в порядке
a-front + b-front + a-back + b-back,
где front и back - это первые и последние элементы списков.
Если список четной длины, то front и back должны быть равны.
В противном случае front должен быть на 1 больше back.
Пример входа: [1, 2, 3, 4] [5, 6]
Пример выхода: [1, 2, 5, 3, 4, 6]
"""


def front_back(a: list, b: list) -> list:
    pass


"""
Задание 6.
Удалить соседние равные элементы
Пример входа: [1, 2, 2, 3]
Пример выхода: [1, 2, 3]
"""


def remove_adjacent(a: list) -> list:
    return [x for x, y in zip(a, a[1:]) if x != y] + [a[-1]]

