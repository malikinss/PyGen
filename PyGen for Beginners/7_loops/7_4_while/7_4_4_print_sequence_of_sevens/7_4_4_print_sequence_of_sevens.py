'''
TODO:
    The input to the program is a sequence of integers divisible by 7,
    each number on a separate line.

    The end of the sequence is any number that is not divisible by 7
    (this number itself is not included in the sequence,
    only symbolizing its end).

    Write a program that prints the terms of a given sequence.
'''


def print_sequence_of_sevens():
    """
    Reads a sequence of integers from input, each on a new line.
    Prints each integer as long as it is divisible by 7.
    Stops printing when a number not divisible by 7 is encountered.
    """
    while True:
        num = int(input("Enter a number: "))
        if num % 7 != 0:
            break
        print(num)


# Call the function
print_sequence_of_sevens()
