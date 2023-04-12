# Importing the copy method to make deep copies of the test arrays
from copy import copy
import sys
import numpy
from matplotlib import pyplot

from advanced_algorithms.counting_sort import counting_sort
from advanced_algorithms.merge_sort import merge_sort
# Importing the sorting algorithms and plotting library
from advanced_algorithms.quick_sort import quick_sort

sys.setrecursionlimit(5000)


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


def get_time_for_asc_array(size_of_array: int, list_of_algorithms: list) -> dict:
    dict_asc_times = {}
    number_of_runs = 1

    random_array = numpy.random.randint(0, 5000, size_of_array)
    asc_array = sorted(random_array)

    for algo in list_of_algorithms:
        algo((asc_array), total_time_per_function=dict_asc_times)

    for key in dict_asc_times.keys():
        time = sum(dict_asc_times[key]) / number_of_runs
        print(f"ASCENDING ARRAY: mean time for {key} is: {time}s")

    return dict_asc_times


def get_time_for_desc_array(size_of_array: int, list_of_algorithms: list) -> dict:
    dict_desc_times = {}
    number_of_runs = 1

    random_array = numpy.random.randint(0, 5000, size_of_array)
    desc_array = numpy.sort(random_array)[::-1]

    for algo in list_of_algorithms:
        algo((desc_array), total_time_per_function=dict_desc_times)

    for key in dict_desc_times.keys():
        time = sum(dict_desc_times[key]) / number_of_runs
        print(f"DESCENDING ARRAY: mean time for {key} is: {time}s")

    return dict_desc_times


def get_time_for_duplicate_array(size_of_array: int, list_of_algorithms: list) -> dict:
    dict_dupli_times = {}
    number_of_runs = 1

    dupli_array = numpy.full(size_of_array, 7)

    for algo in list_of_algorithms:
        algo(dupli_array, total_time_per_function=dict_dupli_times)

    for key in dict_dupli_times.keys():
        time = sum(dict_dupli_times[key]) / number_of_runs
        print(f"DUPLI ARRAY: mean time for {key} is: {time}s")

    return dict_dupli_times


# A function to create a line chart for the mean times of each sorting algorithm
def create_chart(size_of_arrays, algorithms, data):
    fig, ax = pyplot.subplots(2, 2)
    pyplot.title("Mean times per algorithm, random array")
    pyplot.xlim(min(size_of_arrays), max(size_of_arrays))
    fig.text(0.5, 0.04, 'size of arrays', ha='center')
    fig.text(0.04, 0.5, 'Time of work [s]', va='center', rotation='vertical')

    # Looping through each algorithm and plotting its mean time for each array size
    position = 0
    for algo in algorithms:
        # start of subplot
        for array_type in data:
            ax[int(position / 2), position % 2].plot(size_of_arrays, data[array_type][algo.__name__], label=array_type)
            ax[int(position / 2), position % 2].legend()
            ax[int(position / 2), position % 2].set_title([algo.__name__])

        position += 1
        # end of subplot

    pyplot.show()


# Main function
if __name__ == '__main__':
    # Parameters
    size_of_arrays = [100, 500, 1_000, 3_000, 5_000]
    list_of_algo = [quick_sort, merge_sort, counting_sort]

    # Logic
    results = dict()
    for algo in list_of_algo:
        results[algo.__name__] = list()

    results_asc = dict()
    for algo in list_of_algo:
        results_asc[algo.__name__] = list()

    results_desc = dict()
    for algo in list_of_algo:
        results_desc[algo.__name__] = list()

    results_dupli = dict()
    for algo in list_of_algo:
        results_dupli[algo.__name__] = list()

    for value in size_of_arrays:
        print('size of sorted array is', value)
        mean_times_for_current_iteration = get_mean_time_for_algorithms(value, list_of_algo)
        mean_times_for_asc_array = get_time_for_asc_array(value, list_of_algo)
        mean_times_for_desc_array = get_time_for_desc_array(value, list_of_algo)
        mean_times_for_dupli_array = get_time_for_duplicate_array(value, list_of_algo)

        for algo_name in mean_times_for_current_iteration:
            results[algo_name].append(mean_times_for_current_iteration[algo_name])
            results_asc[algo_name].append(mean_times_for_asc_array[algo_name])
            results_desc[algo_name].append(mean_times_for_desc_array[algo_name])
            results_dupli[algo_name].append(mean_times_for_dupli_array[algo_name])

    create_chart(size_of_arrays, list_of_algo, {"random": results,
                                                "asc": results_asc,
                                                "desc": results_desc,
                                                "dupli": results_dupli})
