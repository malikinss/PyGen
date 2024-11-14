'''
TODO:
    The input to the program is a natural number n.

    Write a program that calculates the sum of all its divisors.
'''


def sum_of_divisors(n: int) -> int:
    """
    Calculates the sum of all divisors of a given natural number n.

    Args:
        n (int): The number for which divisors will be calculated.

    Returns:
        int: The sum of divisors of n.
    """
    sum_of_divs = 0

    # Loop from 1 to square root of n to find divisors efficiently
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divs += i
            if i != n // i:  # Avoid adding the square root twice
                sum_of_divs += n // i

    return sum_of_divs


# Input
n = int(input("Enter a natural number: "))

# Call the function and print the result
result = sum_of_divisors(n)
print(result)
