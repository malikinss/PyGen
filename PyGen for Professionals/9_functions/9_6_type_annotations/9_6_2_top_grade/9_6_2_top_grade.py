'''
TODO:
    Implement the top_grade() function using type annotations that takes
    one argument:
        grades - a dictionary containing student data, namely the name
        and the grades.

    The function should return a dictionary containing the student's name
    and the highest grade in the top_grade key.

NOTE:
    Use built-in types (list, tuple, ...) rather than types from
    the typing module.

    Also use the | notation rather than the Union type from
    the typing module.

    The dictionary returned by the function should start with the name and
    then the highest grade.
'''


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    """
    Calculate the top grade for a student.

    Args:
        grades (dict[str, list[int]]): A dictionary with the student's name
        and a list of grades.

    Returns:
        student_result (dict[str, int]): A dictionary containing the student's
        name and their highest grade.
    """
    student_result = {}

    student_result['name'] = grades['name']

    student_result['top_grade'] = max(grades['grades'])

    return student_result
