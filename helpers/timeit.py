from functools import wraps
import time


def timeit(func):
    """
    Generic decorator to calculate time of run for decorated algorithm function.
    If total_time_per_function is provided it updates this dictionary with total times
    otherwise it prints the total time in the console
    """
    @wraps(func)
    def timeit_wrapper(*args, total_time_per_function=None, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        if total_time_per_function is None:
            print(f'Function {func.__name__} Took {total_time:.6f} seconds')
            return result

        if func.__name__ in total_time_per_function:
            total_time_per_function.get(func.__name__).append(total_time)
        else:
            total_time_per_function[func.__name__] = []
            total_time_per_function.get(func.__name__).append(total_time)

        return result
    return timeit_wrapper
