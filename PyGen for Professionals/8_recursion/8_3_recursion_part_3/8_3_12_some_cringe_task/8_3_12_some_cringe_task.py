'''
TODO:
    Write a program using recursion that takes a number n as input and
    subtracts 5 from it until it is no longer positive, and then adds 5 to it
    until it is equal to n again.
'''


def some_cringe_task(n: int) -> None:
    """
    Recursively subtracts 5 from n until it becomes non-positive,
    then adds 5 until n equals its original value.

    Args:
        n (int): The number to process.

    Returns:
        None: This function does not return a value, it only prints numbers.
    """
    if n > 0:
        # Print the current value of n and recurse by subtracting 5
        print(n)
        some_cringe_task(n - 5)

    # Print the value of n during the unwinding phase of recursion
    print(n)
