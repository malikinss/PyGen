'''
TODO:
    Write a greet() function that takes an arbitrary number of name string
    arguments (at least one) and returns a greeting according to the sample.

NOTE:
    Note that the function should take an arbitrary number of arguments,
    not a list.

    The code below:
        print(greet('Timur'))
        print(greet('Timur', 'Roman'))
        print(greet('Timur', 'Roman', 'Ruslan'))
    should output:
        Hello, Timur!
        Hello, Timur and Roman!
        Hello, Timur and Roman and Ruslan!

    The greet() function must take at least one mandatory argument!

    You don't need to call the greet() function, you just need to implement it.
'''


def greet(name: str, *names: str) -> str:
    """
    Returns a greeting string for one or more names.

    Args:
        name (str): The first name (mandatory).
        *names (str): Additional names (optional).

    Returns:
        str: A greeting in the format "Hello, name and name and ...!"
    """
    return f"Hello, {' and '.join([name] + list(names))}!"
