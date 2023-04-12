from typing import Union

from numpy import ndarray

from helpers.timeit import timeit

"""
Non commented code is algorithm without recursion
"""


@timeit
def quick_sort(input_array: Union[int, ndarray[int]]):
    if len(input_array) <= 1:
        return input_array

    # Create an empty stack and push the initial range onto it
    stack = []
    stack.append((0, len(input_array) - 1))

    while stack:
        # Pop the next range from the stack
        start, end = stack.pop()

        # Partition the array around the pivot
        pivot = input_array[end]
        i = start - 1
        for j in range(start, end):
            if input_array[j] < pivot:
                i += 1
                input_array[i], input_array[j] = input_array[j], input_array[i]
        i += 1
        input_array[i], input_array[end] = input_array[end], input_array[i]

        # Push the left and right subranges onto the stack
        if i - 1 > start:
            stack.append((start, i - 1))
        if i + 1 < end:
            stack.append((i + 1, end))

    return input_array

# @timeit
# def quick_sort(input_"""arr"""ay: Union[int, ndarray[int]]):
#     # Checking if the array is empty
#     if len(input_array) <= 1:
#         return input_array
#
#     pivot = input_array[0]
#     left, equal, right = [], [], []
#     # Iterate over the input array from 2nd element
#     for number in input_array:
#         if number < pivot:
#             # If the current element is less than the pivot, add it to the left partition.
#             left.append(number)
#             # If current element is equal to pivot, make it pivot
#         elif number == pivot:
#             equal.append(number)
#         else:
#             # If the current element is greater than or equal to the pivot, add it to the right partition.
#             right.append(number)
#
#     # Combine the sorted left partition, pivot, and sorted right partition into a single sorted array.
#     return quick_sort(left, skip=True) + equal + quick_sort(right, skip=True)
