'''
TODO:
    Teacher Timur was checking math tests in several classes of the online
    school BEEGEEK and decided to make sure that each class had at least one
    excellent student - a student with a grade of 5 on the test.

    Write a program using the built-in functions all(), any() to help Timur
    check.
'''
from typing import Dict


def get_grades_for_one_group(group_size: int) -> Dict:
    """
    Reads grades for a single group and returns a dictionary of student names
    and their grades.

    Args:
        group_size (int): The number of students in the group.

    Returns:
        Dict: A dictionary where keys are student names and values are their
              grades.
    """
    data = input().split()
    return {
        record[0]: record[1] for _ in range(group_size) for record in [data]
    }


def has_group_excellent_student(group_grades: Dict) -> bool:
    """
    Checks if a group has at least one student with a grade of 5.

    Args:
        group_grades (Dict): A dictionary of student names and their grades.

    Returns:
        bool: True if at least one student has a grade of 5, False otherwise.
    """
    return any(grade == '5' for grade in group_grades.values())


def is_excellent_student_in_each_group(groups_number: int) -> bool:
    """
    Determines whether each group has at least one student with a grade of 5.

    Args:
        groups_number (int): The number of groups.

    Returns:
        bool: True if every group has at least one excellent student,
              False otherwise.
    """
    return all(
        has_group_excellent_student(
            get_grades_for_one_group(int(input()))
        ) for _ in range(groups_number)
    )


# Read input and check for excellent students in all groups
print("YES" if is_excellent_student_in_each_group(int(input())) else "NO")
