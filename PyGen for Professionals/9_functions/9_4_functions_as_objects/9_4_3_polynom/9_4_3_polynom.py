'''
TODO:
    Implement a function polynom() that takes one argument:
        x is a real number

    The function should return the value of the expression x ^2+1.

    The function should also have a values attribute that is a set of all
    the values of the function that have already been calculated.
'''


def polynom(x: float) -> float:
    """
    Computes the polynomial expression x^2 + 1 and stores the result.

    Args:
        x (float): The input real number.

    Returns:
        float: The result of the polynomial expression.
    """
    # Using setdefault to initialize 'values' attribute
    polynom.__dict__.setdefault('values', set())

    computed_value = x**2 + 1
    polynom.values.add(computed_value)

    return computed_value
