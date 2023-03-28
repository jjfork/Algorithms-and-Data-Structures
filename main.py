# Importing the copy method to make deep copies of the test arrays
from copy import copy

import numpy
from matplotlib import pyplot

from advanced_algorithms.counting_sort import counting_sort
from advanced_algorithms.merge_sort import merge_sort
from algorithms.bubble_sort import bubble_sort
# Importing the sorting algorithms and plotting library
from advanced_algorithms.quick_sort import quick_sort


# A function to get the mean time for each sorting algorithm for a given array size
def get_mean_time_for_algorithms(size_of_array: int, list_of_algorithms: list) -> dict:
    dict_times = {}
    number_of_runs = 1  # Number of times each algorithm will run for a given array size

    # Looping through each algorithm and the number of runs
    for i in range(number_of_runs):
        # Creating a random test array for each iteration
        random_array = numpy.random.randint(0, 5000, size_of_array)

        # Looping through each algorithm and calculating the total time taken by each
        for algo in list_of_algorithms:
            algo(copy(random_array), total_time_per_function=dict_times)

    # Looping through the results and calculating the mean time for each algorithm
    for key in dict_times.keys():
        mean = sum(dict_times[key]) / number_of_runs
        print(f"mean time for {key} is: {mean}s")
        dict_times[key] = mean

    return dict_times


# A function to create a line chart for the mean times of each sorting algorithm
def create_chart(size_of_arrays, data):
    pyplot.title("Mean times per algorithm")
    pyplot.xlabel('size of arrays')
    pyplot.ylabel('Time of work [s]')
    pyplot.xlim(min(size_of_arrays), max(size_of_arrays))

    # Looping through each algorithm and plotting its mean time for each array size
    for name in data:
        pyplot.plot(size_of_arrays, data[name], label=name)

    pyplot.legend()
    pyplot.show()


# Main function
if __name__ == '__main__':
    # Parameters
    size_of_arrays = [100, 500, 1_000, 3_000, 5_000]
    list_of_algo = [counting_sort, merge_sort, quick_sort]

    # Logic
    results = dict()
    for algo in list_of_algo:
        results[algo.__name__] = list()

    for value in size_of_arrays:
        print('size of sorted array is', value)
        mean_times_for_current_iteration = get_mean_time_for_algorithms(value, list_of_algo)

        for algo_name in mean_times_for_current_iteration:
            results[algo_name].append(mean_times_for_current_iteration[algo_name])

    create_chart(size_of_arrays, results)
