'''
TODO:
    The input to the program is a natural number n.

    Write a program that displays a graphical representation of the
    divisibility of numbers from 1 to n inclusive.

    In each line, you need to print the next number and as many “+”
    characters as there are divisors for this number.
'''


def display_divisibility(n: int) -> None:
    """
    Displays a graphical representation of the divisibility of numbers
    from 1 to n.
    For each number from 1 to n, the program prints the number followed
    by as many "+" characters
    as there are divisors of that number.

    Args:
    n (int): The upper limit of the range of numbers to check for divisibility.

    Returns:
    None: Prints the number and its divisors in graphical format.
    """
    for i in range(1, n + 1):
        count = 0

        # Count divisors of i
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        # Print the number followed by the '+' characters based on
        # divisor count
        print(i, '+' * count, sep='')


# Input the number n
n = int(input())

# Call the function
display_divisibility(n)
