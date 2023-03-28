from typing import Union

from numpy import ndarray

from helpers.timeit import timeit


@timeit
def merge_sort(input_array: Union[int, ndarray[int]]):
    if len(input_array) > 1:
        mid = len(input_array) // 2
        left = input_array[:mid]
        right = input_array[mid:]

        # Recursive call
        merge_sort(left)
        merge_sort(right)

        # Merge halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                input_array[k] = left[i]
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            k += 1
        # copy element from left(remaining)
        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1
        # copy element from right(remaining)
        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1

        return input_array
