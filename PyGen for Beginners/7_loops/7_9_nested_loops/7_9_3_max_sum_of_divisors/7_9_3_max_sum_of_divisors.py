'''
TODO:
    The program receives two natural numbers a and b (a< b) as input.

    Write a program that finds a natural number from the interval [a; b]
    with the maximum sum of divisors.

    If there are several such numbers, then print the largest of them.
'''


def max_sum_of_divisors(a: int, b: int) -> None:
    """
    Finds the natural number in the interval [a, b] with the maximum sum
    of divisors.
    If there are multiple such numbers, the largest one is selected.

    Args:
    a (int): The lower bound of the interval (a < b).
    b (int): The upper bound of the interval.

    Returns:
    None: Prints the number with the maximum sum of divisors and the sum.
    """

    max_sum = 0
    number_with_max_sum = 0

    # Iterate through the range [a, b]
    for i in range(a, b + 1):
        total_sum = 0

        # Find divisors and sum them up
        for j in range(1, i + 1):
            if i % j == 0:
                total_sum += j

        # If the sum of divisors is greater, or if it's the same but
        # the number is larger
        if total_sum >= max_sum:
            max_sum = total_sum
            number_with_max_sum = i

    print(number_with_max_sum, max_sum)


# Input the values for a and b
a = int(input())
b = int(input())

# Call the function
max_sum_of_divisors(a, b)
