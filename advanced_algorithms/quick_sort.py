from typing import Union

from numpy import ndarray

from helpers.timeit import timeit


@timeit
def quick_sort(input_array: Union[int, ndarray[int]]):
    # Checking if the array is empty
    if len(input_array) == 0:
        return []

    pivot = input_array[0]
    left = []
    right = []
    # Iterate over the input array from 2nd element
    for number in range(1, len(input_array)):
        if input_array[number] < pivot:
            # If the current element is less than the pivot, add it to the left partition.
            left.append(input_array[number])
        else:
            # If the current element is greater than or equal to the pivot, add it to the right partition.
            right.append(input_array[number])
    # Recursively sort the left and right partitions using the same quicksort algorithm.
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Combine the sorted left partition, pivot, and sorted right partition into a single sorted array.
    return sorted_left + [pivot] + sorted_right
