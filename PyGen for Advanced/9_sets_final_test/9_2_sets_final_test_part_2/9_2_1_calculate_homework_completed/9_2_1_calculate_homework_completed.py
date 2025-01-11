'''
TODO:
    A teacher is checking homework in a class and has received the following
    answers:
        out of n students, m had their homework eaten by a dog,
        k had their power cut off, and p students suffered both misfortunes.

    Write a program that determines how many people have completed their
    homework.
'''


def calculate_homework_completed(n: int, m: int, k: int, p: int) -> int:
    """
    Calculates the number of students who have completed their homework.

    Args:
        n (int): Total number of students in the class.
        m (int): Number of students whose homework was eaten by a dog.
        k (int): Number of students who had their power cut off.
        p (int): Number of students who suffered both misfortunes.

    Returns:
        int: The number of students who completed their homework.
    """
    return n - (m - p + k)


# Inputs from the teacher
n = int(input())
m = int(input())
k = int(input())
p = int(input())

# Calculate and print the number of students who completed their homework
print(calculate_homework_completed(n, m, k, p))
