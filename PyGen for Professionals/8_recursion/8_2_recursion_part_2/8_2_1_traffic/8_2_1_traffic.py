'''
TODO:
    You can see the traffic() function implemented using a while loop that
    takes a number n as an argument and prints the string "Do not park"
    n times.

    Rewrite this function using recursion to do the same thing.
'''

'''
def traffic(n):
    while n > 0:
        print("Do not park")
        n -= 1
'''


def traffic(n: int) -> None:
    """
    Prints the message "Do not park" a specified number of times using
    recursion.

    Args:
        n (int): The number of times the message should be printed.
    """
    if n <= 0:
        # Base case: Stop recursion when n reaches 0
        return
    else:
        # Print the message and call the function recursively
        print("Do not park")
        traffic(n - 1)
