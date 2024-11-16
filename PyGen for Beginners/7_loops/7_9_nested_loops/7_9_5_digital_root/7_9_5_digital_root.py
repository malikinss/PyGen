'''
TODO:
    The input to the program is a natural number n.

    Write a program that finds the digital root of a given number.

    The digital root of the number n is obtained as follows:
        if you add all the digits of this number, then all the digits
        of the found sum and repeat this process until the result
        is a single-digit number (digit), which is called the digital root
        of the original number.

NOTE:
    Use nested while loops.
'''


def digital_root(n: int) -> int:
    """
    Calculates the digital root of a given number.
    The digital root is the result of repeatedly summing the digits
    of a number until the result is a single-digit number.

    Args:
    n (int): The number for which the digital root is calculated.

    Returns:
    int: The digital root of the number.
    """
    while n > 9:
        new_n = 0

        # Sum the digits of the current number
        while n > 0:
            new_n += n % 10
            n //= 10

        # Update n with the sum of its digits
        n = new_n

    return n


# Input the number n
n = int(input())

# Output the digital root
print(digital_root(n))
