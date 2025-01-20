'''
TODO:
    Given three lists student_ids, student_names, student_grades, containing
    information about students.

    Complete the above code using the generator to obtain a result list
    containing nested dictionaries according to the pattern:
        [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].

NOTE:
    You can use the built-in zip() function to iterate through all three lists
    in parallel.

    There is no need to print the contents of the result list.
'''
from typing import List, Dict


def generate_student_info(
    student_ids: List[str],
    student_names: List[str],
    student_grades: List[int]
) -> List[Dict[str, Dict[str, int]]]:
    """
    This function takes three lists: student_ids, student_names, and
    student_grades, and returns a list of nested dictionaries where each
    dictionary contains the student ID as the key and a dictionary of the
    student's name and grade as the value.

    Args:
        student_ids (List[str]): A list of student IDs.
        student_names (List[str]): A list of student names.
        student_grades (List[int]): A list of student grades.

    Returns:
        List[Dict[str, Dict[str, int]]]: A list of nested dictionaries where
                                         each dictionary contains the student
                                         ID as the key and another dictionary
                                         with the student's name and grade as
                                         the value.
    """
    # Using zip and assigning it to a variable
    zipped_data = zip(student_ids, student_names, student_grades)

    # Using a list comprehension to iterate through zipped_data
    result = [
        {student_id: {student_name: grade}}
        for student_id, student_name, grade in zipped_data
    ]

    return result


# Sample data
student_ids = [
    'S001', 'S002', 'S003', 'S004',
    'S005', 'S006', 'S007', 'S008',
    'S009', 'S010', 'S011', 'S012', 'S013'
]
student_names = [
    'Camila Rodriguez', 'Juan Cruz', 'Dan Richards',
    'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
    'Khalid Hussain', 'Ethan Hawke', 'David Bowman',
    'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'
]
student_grades = [
    86, 98, 89,
    92, 45, 67,
    89, 90, 100,
    98, 10, 96, 93
]

# Calling the function to generate the result
result = generate_student_info(student_ids, student_names, student_grades)
