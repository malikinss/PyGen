'''
TODO:
    n people, numbered from 1 to n, stand in a circle.

    They begin to count, every kth person in a row leaves the circle,
    after which the count continues with the next person.

    Write a program to determine the number of the person who will remain
    in the circle last.
'''


def find_last_person(n: int, k: int) -> int:
    """
    This function solves the Josephus problem. Given `n` people standing
    in a circle, every `k`-th person is eliminated in each round until
    only one person remains.

    Parameters:
    - n (int): The total number of people in the circle.
    - k (int): The step size, i.e., every k-th person is eliminated.

    Returns:
    - int: The position (1-indexed) of the last person remaining in the circle.
    """
    res = 0  # Position of the last person remaining (0-indexed)

    # Iterate through the process of elimination
    for i in range(1, n + 1):
        res = (res + k) % i  # Update position of the survivor

    return res + 1  # Convert to 1-indexed and return


# Example usage
n = int(input())  # Number of people
k = int(input())  # Every k-th person is eliminated

print(find_last_person(n, k))
