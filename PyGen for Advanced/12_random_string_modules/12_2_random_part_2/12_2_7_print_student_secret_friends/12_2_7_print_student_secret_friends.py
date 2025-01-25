'''
TODO:
    Write a program that randomly assigns each student a secret friend who
    will work with them on programming problems.

NOTE:
    Note that you cannot be a secret friend to yourself and you cannot be
    a secret friend to more than one student.
'''
import random


def get_students_list(number_of_students: int) -> list[str]:
    """
    Reads the names of students from input and returns a list of students.

    Args:
        number_of_students (int): The number of students.

    Returns:
        list[str]: A list containing the names of the students.
    """
    students_list = [input() for _ in range(number_of_students)]
    return students_list


def get_students_pairs(students_list: list[str]) -> dict[str, str]:
    """
    Randomly assigns a secret friend to each student, ensuring no one is
    paired with themselves and no one is assigned more than one secret friend.

    Args:
        students_list (list[str]): A list of students.

    Returns:
        dict[str, str]: A dictionary where keys are student names and values
                        are their secret friends.
    """
    number_of_students = len(students_list)
    student_pairs = dict()

    # Shuffle students list to ensure randomness
    shuffled_students = students_list[:]
    random.shuffle(shuffled_students)

    for i in range(number_of_students):
        # Pairing with the previous student
        student_pairs[students_list[i]] = shuffled_students[i - 1]

    return student_pairs


def print_student_secret_friends(student_friends: dict[str, str]) -> None:
    """
    Prints the secret friend assignment.

    Args:
        student_friends (dict[str, str]): A dictionary where keys are student
                                          names and values are their secret
                                          friends.
    """
    for student, friend in student_friends.items():
        print(f"{student} - {friend}")


# Main execution
n = int(input("Enter the number of students: "))
students = get_students_list(n)
pairs = get_students_pairs(students)

print_student_secret_friends(pairs)
