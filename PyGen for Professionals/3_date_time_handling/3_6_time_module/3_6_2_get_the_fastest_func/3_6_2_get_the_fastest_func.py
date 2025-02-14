'''
TODO:
    Implement a function get_the_fastest_func() that takes two arguments
    in the following order:
        funcs — list of arbitrary functions
        arg - arbitrary object

    The get_the_fastest_func() function should return the function from the
    list of funcs that took the least amount of time to calculate the value
    when called with the arg argument.
'''
import timeit


def get_execution_time(func, *args):
    """
    Returns the time it takes to execute the given function with the provided
    arguments.

    Args:
        func (function): The function to be executed.
        *args: Arbitrary positional arguments to be passed to the function.

    Returns:
        float: The time in seconds it took to execute the function.
    """
    return timeit.timeit(lambda: func(*args), number=1)


def get_the_fastest_func(funcs, *arg):
    """
    Returns the function from the list that takes the least amount of time to
    execute when called with the given argument.

    Args:
        funcs (list): A list of functions to test.
        *arg: Arbitrary positional arguments to be passed to each function.

    Returns:
        function: The function that takes the least time to execute.
    """
    fastest_func = min(funcs, key=lambda func: get_execution_time(func, *arg))
    return fastest_func
