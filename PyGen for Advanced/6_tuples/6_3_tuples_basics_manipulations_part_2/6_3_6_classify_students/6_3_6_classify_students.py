'''
TODO:
    Write a program that prints a list of good and excellent students
    in the class.

    Input format:
        The program receives a natural number n as input, followed by n lines
        with the student's last name and his grade on each of them.

    Output format:
        The program should first print all the input lines with the students'
        last names and grades in the same order.

        Then there is an empty line, and then the lines with the last names
        and grades of good and excellent students are printed
        (in the same order).

NOTE:
    A student's grade is a natural number from 1 to 5.

    It is guaranteed that there is at least one good student
    (with a grade of 4) or an excellent student (with a grade of 5)
    in the class.
'''
from typing import List, Tuple


def get_student_data(n: int) -> List[Tuple[str, int]]:
    """
    Reads the student data from input, converting the grade to an integer.

    Args:
    n (int): Number of students.

    Returns:
    List[Tuple[str, int]]: A list of tuples with student last names and grades.
    """
    students = []

    for _ in range(n):
        last_name, grade = input().split()
        students.append((last_name, int(grade)))

    return students


def classify_students(
    students: List[Tuple[str, int]]
) -> List[Tuple[str, int]]:
    """
    Classifies students into good and excellent based on their grades.

    A student is considered good if their grade is 4, and excellent
    if their grade is 5.

    Args:
    students (List[Tuple[str, int]]): List of tuples containing student
    last names and grades.

    Returns:
    List[Tuple[str, int]]: A list of good and excellent students.
    """
    good_students = [student for student in students if student[1] >= 4]
    return good_students


def print_students(students: List[Tuple[str, int]]):
    """
    Prints the student data.

    Args:
    students (List[Tuple[str, int]]): List of tuples with student last names
                                      and grades.
    """
    for student in students:
        print(*student)


def main():
    n = int(input())  # Number of students

    # Get student data
    students = get_student_data(n)

    # Print all student data
    print_students(students)

    print()

    # Get and print good and excellent students
    good_students = classify_students(students)
    print_students(good_students)


# Run the program
main()
