from typing import Union
from numpy import ndarray

from helpers.timeit import timeit


@timeit
def selection_sort(input_array: Union[int, ndarray[int]]):
    # get the length of the input array
    size = len(input_array)

    # iterate through each element of the array
    for i in range(size):
        # assume the current index is the minimum
        min_idx = i
        # check each element after the current index to find the minimum value
        j = i + 1
        while j < size:
            if input_array[j] < input_array[min_idx]:
                min_idx = j
            j += 1
        # if the minimum value is not at the current index, swap the two values
        if min_idx != i:
            temp = input_array[i]
            input_array[i] = input_array[min_idx]
            input_array[min_idx] = temp

    return input_array
