'''
TODO:
    Implement a function calculate_it() that takes one or more arguments in
    the following order:
        func - arbitrary function
        *args - a variable number of positional arguments, each of which is
                an arbitrary object

    The function must return a tuple whose first element is the return value
    of func when called with *args, and the second element is the estimated
    time (in seconds) it took to calculate that value.
'''
import timeit
import time


def calculate_it(func, *args):
    """
    Executes a function with arbitrary arguments and returns the result along
    with the time it took to execute the function.

    Args:
        func (function): The function to be executed.
        *args: Arbitrary positional arguments to be passed to the function.

    Returns:
        tuple: A tuple containing the result of the function and the time it
               took to execute.
    """
    start_time = time.perf_counter()
    func_result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return (func_result, execution_time)


def calculate_it_2(func, *args):
    """
    Executes a function with arbitrary arguments and returns the result along
    with the time it took to execute the function, using timeit for timing.

    Args:
        func (function): The function to be executed.
        *args: Arbitrary positional arguments to be passed to the function.

    Returns:
        tuple: A tuple containing the result of the function and the time it
               took to execute.
    """
    # Wrapping the function execution to avoid calling it twice
    def wrapper():
        return func(*args)

    execution_time = timeit.timeit(wrapper, number=1)
    func_result = wrapper()  # Execute once after timing
    return (func_result, execution_time)
