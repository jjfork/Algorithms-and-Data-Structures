from typing import Union

from numpy import ndarray

from helpers.timeit import timeit


@timeit
def quick_sort(input_array: Union[int, ndarray[int]]):
    if len(input_array) == 0:
        return []

    pivot = input_array[0]
    left = []
    right = []

    for number in range(1, len(input_array)):
        if input_array[number] < pivot:
            left.append(input_array[number])
        else:
            right.append(input_array[number])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + [pivot] + sorted_right
