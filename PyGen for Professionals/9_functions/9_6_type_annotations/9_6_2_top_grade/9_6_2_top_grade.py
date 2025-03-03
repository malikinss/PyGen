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


def top_grade(grades: dict[str, list[int]]) -> dict[str, str | int]:
    """
    Calculate the top grade for a student.

    Args:
        grades (dict[str, list[int]]): A dictionary where the keys are student
        names and the values are lists of grades.

    Returns:
        dict[str, str | int]: A dictionary containing the student's name and
        their highest grade.
    """
    student_result = {}

    for student_name, student_grades in grades.items():
        student_result['name'] = student_name
        student_result['top_grade'] = max(student_grades)

    return student_result
