import random

import numpy

size_of_arrays = [100, 500, 1_000, 3_000, 5_000]
minimum_number = 0
maximum_number = 5_000


def generate_ascending_array(size_of_array):
    return numpy.arange(minimum_number, maximum_number, size_of_array)


def generate_descending_array(size_of_array):
    return numpy.arange(minimum_number, maximum_number, size_of_array)[::-1]


def random_array(size_of_array):
    return numpy.random.randint(minimum_number, maximum_number, size_of_array)


def same_numbers_array(size_of_array):
    return numpy.full(size_of_array, random.randint(minimum_number, maximum_number))
