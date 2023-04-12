from typing import Union

from numpy import ndarray

from helpers.timeit import timeit


@timeit
def counting_sort(input_array: Union[int, ndarray[int]]):
    #
    # if len(input_array) <= 1:
    #     return input_array
    #
    # count = [0] * (max(input_array) + 1)
    # output = []
    #
    # for number in input_array:
    #     count[number] += 1
    #
    # for index, number in enumerate(count):
    #     if number != 0:
    #         for i in range(number):
    #             output.append(index)
    #
    # return output

    # Find maximal element from array
    max_element = max(input_array)

    # Creating counting array and make it start from 0
    counting_array = [0] * (max_element + 1)

    # Count number of occurrences, each element
    for element in input_array:
        counting_array[element] += 1

    # Create a sorted array and populate it using a counting array
    sorted_array = [0] * len(input_array)
    for element, number in enumerate(sorted_array):
        if number != 0:
            for i in range(number):
                sorted_array.append(element)

    return sorted_array
