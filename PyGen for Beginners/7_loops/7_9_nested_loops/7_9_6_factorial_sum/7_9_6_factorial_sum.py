'''
TODO:
    Given a natural number n.

    Write a program that prints the value of the sum 1!+2!+3!+…+n!.
'''


def factorial_sum(n: int) -> int:
    """
    Calculates the sum of factorials from 1! to n!.

    Args:
    n (int): The upper limit of the factorial sum.

    Returns:
    int: The sum of the factorials from 1! to n!.
    """
    result = 0

    # Loop to calculate factorials from 1 to n
    for i in range(1, n + 1):
        cur_fact = 1

        # Calculate the factorial of the current number
        for j in range(1, i + 1):
            cur_fact *= j

        # Add the current factorial to the total sum
        result += cur_fact

    return result


# Input the number n
n = int(input())

# Output the sum of factorials
print(factorial_sum(n))
