'''
TODO:
    Implement the print_given() function, which accepts an arbitrary number of
    positional and named arguments and outputs all passed arguments,
    specifying the type of each.

    Argument-type pairs should be output each on a separate line, in the
    following format:
        - for positional arguments:
            <argument value> <argument type>
        - for named arguments:
            <variable name> <argument value> <argument type>

NOTE:
    When output, positional arguments should be arranged in the order of their
    transmission, named arguments in the lexicographic order of variable names.

    When output, all positional arguments must follow first, then all named
    arguments.

    If nothing is passed to the function, the function should not output
    anything.
'''


def print_given(*args, **kwargs):
    """
    Prints the given arguments and their types.

    Args:
        *args: Positional arguments.
        **kwargs: Named arguments.

    Output:
        Prints each argument value and its type. Positional arguments are
        printed first, followed by named arguments sorted lexicographically by
        variable name.
    """
    # Print positional arguments with their types
    for value in args:
        print(value, type(value))

    # Print named arguments with their names and types in lexicographic order
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))
