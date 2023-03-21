from helpers.timeit import timeit
from typing import Union
from numpy import ndarray



@timeit
def bubble_sort(input_array: Union[int, ndarray[int]]):
    # determine the length of the input array
    size = len(input_array)

    # iterate over the input array
    for i in range(size):

        # iterate over the unsorted part of the input array
        for j in range(0, size - i - 1):

            # if the current element is greater than the next element
            if input_array[j] > input_array[j + 1]:
                # swap the current and next elements
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]

    return input_array
