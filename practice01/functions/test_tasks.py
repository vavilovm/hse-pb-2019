from tasks import *

def helper_test_transform(f):
    assert f([], 2, 3) == []
    assert f([1, 2, 3, 4], 2, 3) == [4, 9]
    assert f([-566, 239, 30], 228, 322) == [239 ** 2]


def test_transform_simple():
    helper_test_transform(transform_simple)

def test_transform_list_comprehensions():
    helper_test_transform(transform_list_comprehensions)


def test_transform_generators():
    helper_test_transform(transform_generators)


def test_conditional_sum_2d_simple():
    pass


def teest_conditional_sum_2d():
    pass


def test_reverse_array():
    pass


def test_verbing():
    pass


def test_front_back():
    pass


def test_remove_adjacent():
    pass
