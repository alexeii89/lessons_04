from functools import reduce


def my_foo(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]
print(reduce(my_foo, my_list))