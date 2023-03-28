from typing import Union

from numpy import ndarray

from helpers.timeit import timeit


@timeit
def counting_sort(input_array: Union[int, ndarray[int]]):
    # Find maximal element from array
    max_element = max(input_array)

    # Creating counting array and make it start from 0
    counting_array = [0] * (max_element + 1)

    # Count number of occurrences, each element
    for element in input_array:
        counting_array[element] += 1

    # Calculate the cumulative sum of the counts
    for i in range(1, len(input_array)):
        counting_array[i] += counting_array[i - 1]

    # Create a sorted array and populate it using a counting array
    sorted_array = [0] * len(input_array)
    for element in input_array:
        sorted_array[counting_array[element - 1]] = element
        counting_array[element] -= 1

    input_array = sorted_array

    return input_array
