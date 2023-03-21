from helpers.timeit import timeit
from typing import Union
from numpy import ndarray


@timeit
def insertion_sort(input_array: Union[int, ndarray[int]]):
    # iterate through each element of the array, starting from the second element
    for i in range(1, len(input_array)):
        # store the current element as the key
        key = input_array[i]
        # iterate backwards through the sorted portion of the array to find the correct position for the key
        j = i - 1
        while j >= 0 and key < input_array[j]:
            # shift elements to the right to make room for the key
            input_array[j + 1] = input_array[j]
            j -= 1
        # place the key in the correct position
        input_array[j + 1] = key

    return input_array
