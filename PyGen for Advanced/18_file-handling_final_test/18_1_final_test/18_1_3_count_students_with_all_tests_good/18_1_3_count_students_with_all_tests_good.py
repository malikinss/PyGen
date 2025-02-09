'''
TODO:
    A text file is available to you "grades.txt ", containing the student's
    grades for three tests in each of the trimesters.

    The lines of the file have the form:
        "last name evaluation_1 evaluation_2 evaluation_3"

    Write a program to count the number of students who have passed all three
    tests.

    The test is considered passed if the number of points on it is not less
    than 65.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def read_data_from_file(file_name: str):
    """
    Reads the content of a file and returns a list of lines.

    Args:
        file_name (str): The name of the file.

    Returns:
        list: A list of lines from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return file.readlines()


def process_student_data(data: list):
    """
    Processes the student data into a list of tuples with the student's name
    and their grades.

    Args:
        data (list): A list of lines from the file, each containing a
                     student's name and grades.

    Returns:
        list: A list of tuples where each tuple contains a student's name and
              their grades.
    """
    return [
        (row.split()[0], list(map(int, row.split()[1:])))
        for row in data
    ]


def has_passed_all_tests(grades: list) -> bool:
    """
    Checks if a student has passed all tests (each grade must be >= 65).

    Args:
        grades (list): A list of grades for a student.

    Returns:
        bool: True if all grades are >= 65, False otherwise.
    """
    return all(grade >= 65 for grade in grades)


def count_students_with_all_tests_good(file_name: str) -> int:
    """
    Counts the number of students who have passed all three tests.

    Args:
        file_name (str): The name of the file containing the student grades.

    Returns:
        int: The number of students who have passed all tests.
    """
    data = read_data_from_file(file_name)
    student_data = process_student_data(data)
    return sum(1 for _, grades in student_data if has_passed_all_tests(grades))


# Calculate and print the result
result = count_students_with_all_tests_good('grades.txt')
print(result)
