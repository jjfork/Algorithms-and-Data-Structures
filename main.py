import numpy

from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from matplotlib import pyplot
from copy import copy


def get_mean_time_for_algorithms(size_of_array: int, list_of_algorithms: list) -> dict:
    dict_times = {}
    numer_of_runs = 1

    for i in range(numer_of_runs):
        test_array = numpy.random.randint(-5000, 5000, size_of_array)

        for algo in list_of_algorithms:
            algo(copy(test_array), total_time_per_function=dict_times)

    for key in dict_times.keys():
        mean = sum(dict_times[key])/numer_of_runs
        print(f"mean time for {key} is: {mean}s")
        dict_times[key] = mean

    return dict_times


def create_chart(size_of_arrays, data):
    pyplot.title("Mean times per algorithm")
    pyplot.xlabel('size of arrays')
    pyplot.ylabel('Time of work [s]')
    pyplot.xlim(min(size_of_arrays), max(size_of_arrays))

    for name in data:
        pyplot.plot(size_of_arrays, data[name], label=name)

    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    # Parameters
    size_of_arrays = [100, 500, 1_000, 3_000, 5_000]
    list_of_algo = [selection_sort, insertion_sort, bubble_sort]

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

