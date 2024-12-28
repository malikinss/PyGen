'''
TODO:
    A natural number is given as input to the program.

    Write a program that inserts commas into a given number according
    to the standard American convention for commas in large numbers.
'''


def format_number_with_commas(n: int) -> str:
    """
    Takes a natural number and returns the number with commas
    inserted according to the standard American convention for
    large numbers.

    Args:
        n (int): The input natural number.

    Returns:
        str: The formatted number with commas.
    """
    # Convert the number to a string
    n_str = str(n)

    # Create a list to hold the result
    result = []

    # Process the number from the end, adding commas every 3 digits
    while len(n_str) > 3:
        result.append(n_str[-3:])
        n_str = n_str[:-3]

    # Append the remaining digits
    result.append(n_str)

    # Join the result and reverse it, then add commas
    return ','.join(result[::-1])


# Input
n = int(input())

# Output
print(format_number_with_commas(n))
