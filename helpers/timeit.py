import time
from functools import wraps


# Define a decorator function "timeit" that measures the execution time of the wrapped function.
def timeit(func):
    """
    Generic decorator to calculate time of run for decorated algorithm function.
    If total_time_per_function is provided it updates this dictionary with total times
    otherwise it prints the total time in the console
    """

    # Use the @wraps decorator to preserve the original function's metadata.
    @wraps(func)
    # Define a wrapper function that measures the execution time of the decorated function.
    def timeit_wrapper(*args, total_time_per_function=None, **kwargs):
        # Get the start time of the decorated function's execution.
        start_time = time.perf_counter()

        # Call the decorated function with its arguments and keyword arguments.
        result = func(*args, **kwargs)

        # Get the end time of the decorated function's execution.
        end_time = time.perf_counter()

        # Calculate the total time taken by the decorated function's execution.
        total_time = end_time - start_time

        # If a dictionary of total times per function is provided, update it with the total time taken by this function.
        if total_time_per_function is None:
            # Print the total time taken by the function.
            # print(f'Function {func.__name__} Took {total_time:.6f} seconds')
            return result

        if func.__name__ in total_time_per_function:
            total_time_per_function.get(func.__name__).append(total_time)
        else:
            total_time_per_function[func.__name__] = []
            total_time_per_function.get(func.__name__).append(total_time)

        return result

    return timeit_wrapper
