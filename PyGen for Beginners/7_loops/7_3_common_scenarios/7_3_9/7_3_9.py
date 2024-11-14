'''
TODO:
    The input to the program is a natural number n, and then n different
    natural numbers of the sequence, each on a separate line.

    Write a program that prints the largest and second largest number
    in a sequence.
'''


def find_largest_and_second_largest(n: int) -> None:
    """
    Finds and prints the largest and second largest numbers in a sequence
    of n natural numbers.

    Args:
        n (int): The number of elements in the sequence.
    """
    if n < 2:
        print("At least two numbers are required.")
        return

    max1, max2 = -1, -1

    for _ in range(n):
        num = int(input())

        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    print(f"Largest: {max1}")
    print(f"Second Largest: {max2}")


# Input
n = int(input("Enter the number of elements: "))
find_largest_and_second_largest(n)
