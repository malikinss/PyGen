'''
TODO:
        Given a list of student names and their exam grades.

        Write a program that determines the second lowest grade student.

        The program is given an arbitrary number of lines, each containing the
        name of the next student and his grade, separated by a space.

        The program should determine the second lowest grade student and print
        his name.

NOTE:
        It is guaranteed that all students have different names and grades.
'''
import sys
from collections import defaultdict, Counter


def read_input() -> str:
    """Reads input from stdin and returns it as a single string."""
    return sys.stdin.read().strip()


def get_students_grades(input_data: str) -> Counter:
    """
    Parses input data containing student names and grades.

    Args:
        input_data (str): Input data in the format of "name grade" per line.

    Returns:
        Counter: A Counter object where keys are student names and values are
        lists of grades.
    """
    student_grades = defaultdict(list)
    lines = input_data.splitlines()

    for line in lines:
        student, grade = line.split()
        student_grades[student].append(int(grade))

    return Counter(student_grades)


def get_second_lowest_grade_student(grades: Counter) -> str:
    """
    Finds the student with the second lowest grade based on the provided
    Counter object.

    Args:
        grades (Counter): Counter object where keys are student names and
        values are lists of grades.

    Returns:
        str: Name of the student with the second lowest grade.
    """
    return grades.most_common()[-2][0]


def parse_student_grades(input_data: str) -> str:
    """
    Parses input data and returns the name of the student with the second
    lowest grade.

    Args:
        input_data (str): Input data in the format of "name grade" per line.

    Returns:
        str: Name of the student with the second lowest grade.
    """
    grades = get_students_grades(input_data)

    return get_second_lowest_grade_student(grades)


if __name__ == "__main__":
    input_data = read_input()
    second_lowest_student = parse_student_grades(input_data)
    print(second_lowest_student)
