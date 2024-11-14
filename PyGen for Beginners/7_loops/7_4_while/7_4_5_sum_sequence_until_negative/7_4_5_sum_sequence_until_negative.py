'''
TODO:
    The input to the program is a sequence of integers,
    each number on a separate line.

    A sign of the end of the sequence is any negative number,
    while it is not included in the sequence itself.

    Write a program that prints the sum of all terms in a given sequence.
'''


def sum_sequence_until_negative() -> int:
    """
    Reads a sequence of integers from input, summing all non-negative integers.
    The sequence ends when a negative integer is entered, which
    is not included in the sum.

    Returns:
        int: The sum of all non-negative integers in the sequence.
    """
    sequence_sum = 0

    while True:
        num = int(input("Enter a number (negative to stop): "))
        if num < 0:
            break
        sequence_sum += num

    return sequence_sum


# Call the function and print the result
result = sum_sequence_until_negative()
print("Sum of the sequence:", result)
