'''
TODO:
    Write a program using recursion that takes a number n as input and
    subtracts 5 from it until it is no longer positive, and then adds 5 to it
    until it is equal to n again.
'''


def some_cringe_task(n: int, original: int = None) -> None:
    """
    Recursively subtracts 5 from n until it becomes non-positive,
    then adds 5 until n equals its original value.

    Args:
        n (int): The number to process.
        original (int, optional): The original value of n to track when
                                  to stop.

    Returns:
        None: This function does not return a value, it only prints numbers.
    """
    if original is None:  # Set the original value only once
        original = n

    print(n)  # Print the current value

    if n > 0:
        some_cringe_task(n - 5, original)  # Recur with n - 5

    if n < original:
        print(n + 5)  # Print the increasing sequence while unwinding


# Example usage:
some_cringe_task(16)
