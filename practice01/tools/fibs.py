#!/usr/bin/env python3
from typing import List

#int, str, List
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def untyped_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def ret_str():
    return "a" * 5


""" I want a list
def singleton_list(a: int) -> List[int]:
    return [a]
"""


if __name__ == '__main__':
    variable_a = ret_str()
    variable_int: int = 6
    # play with mypy :)
    print(fib(5))
    #print(fib('a'))
    print(fib(variable_a))
    #print(untyped_fib(2))
    print(untyped_fib('a'))
