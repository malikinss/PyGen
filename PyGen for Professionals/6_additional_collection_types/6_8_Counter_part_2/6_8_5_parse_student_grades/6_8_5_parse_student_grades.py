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
from collections import Counter


def read_input() -> str:
    """
    Reads all input from standard input (stdin) and returns it as a single
    string.

    This function will capture all lines of input provided by the user and
    combine them into one string, with each line separated by a newline
    character.

    Returns:
        str: A single string containing all the lines of input provided
        by the user.
    """
    return sys.stdin.read().strip()


def get_students_grades(input_data: str):
    """
    Parses input data containing student names and grades.

    Args:
        input_data (str): Input data in the format of "name grade" per line.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a
        student's name and their grade.
    """
    student_grades = []
    lines = input_data.splitlines()

    for line in lines:
        student, grade = line.split()
        student_grades.append((student, int(grade)))

    return student_grades


def get_second_lowest_grade_student(grades):
    """
    Finds the student with the second lowest grade based on the provided
    list of grades.

    Args:
        grades (List[Tuple[str, int]]): A list of tuples where each tuple
        contains a student's name and grade.

    Returns:
        str: Name of the student with the second lowest grade.
    """
    # Create a Counter to count occurrences of each grade
    grade_counter = Counter(grade for student, grade in grades)

    # Get sorted list of unique grades
    sorted_grades = sorted(grade_counter.keys())

    # The second lowest grade will be the second item in the sorted list
    second_lowest_grade = sorted_grades[1]

    # Find all students with the second lowest grade
    second_lowest_students = [
        student for student, grade in grades if grade == second_lowest_grade
    ]

    # Return the name of the student with the second lowest grade
    return second_lowest_students[0]


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
