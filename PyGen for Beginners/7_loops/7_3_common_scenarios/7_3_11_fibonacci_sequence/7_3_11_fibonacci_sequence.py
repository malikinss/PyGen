'''
TODO:
    Write a program that reads a natural number n and prints the first n
    numbers of the Fibonacci sequence.
'''


def fibonacci_sequence(n: int) -> None:
    """
    Prints the first n numbers of the Fibonacci sequence.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    # Edge case: if n is less than or equal to 0, we print nothing
    if n <= 0:
        return

    a, b = 1, 1

    # If n == 1, print only the first number
    if n == 1:
        print(a)
        return

    # Print the Fibonacci sequence
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # For a new line after the sequence


# Input
n = int(input("Enter a natural number n: "))

# Call the function to print the Fibonacci sequence
fibonacci_sequence(n)
