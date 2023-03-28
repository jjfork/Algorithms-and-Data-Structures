from copy import copy
from typing import Union

import numpy
from numpy import ndarray

from helpers.timeit import timeit


@timeit
def quick_sort(input_array: Union[int, ndarray[int]]):
    if len(input_array) < 2:
        return input_array

    position = 0

    for i in range(1, len(input_array)):
        if input_array[i] <= input_array[0]:
            position += 1
            temp = input_array[i]
            input_array[i] = input_array[position]
            input_array[position] = temp

    temp = input_array[0]
    input_array[0] = input_array[position]
    input_array[position] = temp

    left = quick_sort(input_array[0:position])
    right = quick_sort(input_array[position + 1:len(input_array)])

    input_array = left + [input_array[position]] + right

    return input_array


# dict_times = {}
# test = numpy.random.randint(0, 100, 100)
# print(test)
# print(quick_sort(copy(test)))