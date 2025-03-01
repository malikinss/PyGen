'''
TODO:
    Write a program that determines the minimum and maximum values of
    a function on a segment in integer points.

    The program receives a valid function f(x) on the first line, and two
    integers a and b, separated by a space, on the next line, representing
    the boundaries of the segment [a; b].

    The program must determine the minimum and maximum values of the
    function f(x) on the segment [a; b] in integer points and output the
    result in the following format:
    - The min value of the function <function f(x)> on the segment <segment>
      is <min. value>
    - The max value of the function <function f(x)> on the segment <segment>
      is <max. value>

NOTE:
    A valid function is an expression that fully complies with the
    Python syntax.
'''
import sys


def get_values(function_expression: str, start: int, end: int):
    """
    Calculate the values of a function on a segment.

    Args:
        function_expression (str): The string representing the function.
        start (int): The starting integer value of the segment.
        end (int): The ending integer value of the segment.

    Returns:
        List[int]: A list containing values of the function on the segment.
    """
    try:
        values = []
        for x in range(start, end + 1):
            # Safely evaluate the function expression for each value of x
            values.append(eval(function_expression, {}, {"x": x}))
        return values
    except Exception as e:
        print(f"Error evaluating the function: {e}", file=sys.stderr)
        sys.exit(1)


def calculate_min_max_values(function_expression: str, start: int, end: int):
    """
    Calculate the minimum and maximum values of a function on a segment.

    Args:
        function_expression (str): The string representing the function.
        start (int): The starting integer value of the segment.
        end (int): The ending integer value of the segment.

    Returns:
        List[int]: A list containing the minimum and maximum values.
    """
    values = get_values(function_expression, start, end)
    return min(values), max(values)


def find_and_print_min_max_values():
    """
    Calculates and prints the minimum and maximum values of a function on
    a given segment.

    Reads the function and segment boundaries from input, evaluates the
    function at each integer point in the segment,
    and prints the minimum and maximum values.

    Args:
        None

    Returns:
        None
    """
    try:
        # Read the function expression and segment boundaries from input
        function_expression = input("Enter the function: ").strip()
        start, end = map(int, input("Enter the boundaries (a b): ").split())

        # Ensure that the boundaries are valid
        if start > end:
            print(
                f"Invalid segment: {start} is greater than {end}."
                f"Please ensure that the start is less than or equal"
                f" to the end."
            )
            return

        # Get min and max values of the function
        min_value, max_value = calculate_min_max_values(
            function_expression, start, end
        )

        # Output the results
        print(
            f"The min value of the function {function_expression}"
            f"on the segment [{start}; {end}] is {min_value}"
        )
        print(
            f"The max value of the function {function_expression}"
            f"on the segment [{start}; {end}] is {max_value}"
        )

    except ValueError:
        print(
            "Invalid input.",
            "Please enter valid integers for the segment boundaries.",
            file=sys.stderr
        )
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


# Run the function to find and print the min and max values
find_and_print_min_max_values()
