'''
TODO:
    Write a program that takes as input a valid non-empty list, a valid
    non-empty tuple, or a valid set of arbitrary length, and does the
    following:
        - if the input is a list, output its last element
        - if the input is a tuple, output its first element
        - if the input is a set, output the number of its elements
'''


def process_input(data: str) -> None:
    """
    Processes the input string by converting it using eval to a list, tuple,
    or set, and performs the respective operation based on the type.

    Args:
        data (str): The input data in string format, which should represent
        a list, tuple, or set.

    Returns:
        None: Outputs the last element of a list, the first element of
        a tuple, or the number of elements in a set.
    """
    try:
        parsed_data = eval(data)  # Convert string to list, tuple, or set
    except (ValueError, SyntaxError):
        raise ValueError(
            "Input string must represent a valid list, tuple, or set."
        )

    operations = {
        list: lambda x: x[-1],  # Last element of list
        tuple: lambda x: x[0],  # First element of tuple
        set: lambda x: len(x)   # Length of set
    }

    data_type = type(parsed_data)

    if data_type in operations:
        print(operations[data_type](parsed_data))
    else:
        raise TypeError(
            "Unsupported data type. Please input correct data type."
        )


# Example usage
process_input("[1, 2, 3]")
process_input("(1, 2, 3)")
process_input("{1, 2, 3}")
