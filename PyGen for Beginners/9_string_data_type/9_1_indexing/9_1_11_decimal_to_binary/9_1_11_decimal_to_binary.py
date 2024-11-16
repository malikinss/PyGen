'''
TODO:
    The input to the program is a natural number written in
    the decimal number system.

    Write a program that converts a given number to the binary number system.
'''


def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal number to its binary representation.

    Args:
        n (int): The decimal number to be converted.

    Returns:
        str: The binary representation of the decimal number.
    """
    if n == 0:
        return "0"

    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2

    return res


# User input
number = int(input("Enter a decimal number: "))

# Call the function and print the result
binary_representation = decimal_to_binary(number)
print(binary_representation)
