'''
TODO:
    Three students are given grades in physics on a 10-point scale.

    Write a program that outputs the set of grades for the third student that
    are not found in either the first or second student.
NOTE:
    The student's grade is in the range from 0 to 10 inclusive.
'''
from typing import Set


def get_unique_grades(
    student_1: Set[str], student_2: Set[str], student_3: Set[str]
) -> Set[str]:
    """
    Returns the grades of the third student that are not present in the first
    or second student's grades.

    Args:
        student_1 (Set[str]): Grades of the first student.
        student_2 (Set[str]): Grades of the second student.
        student_3 (Set[str]): Grades of the third student.

    Returns:
        Set[str]: The set of unique grades of the third student.
    """
    # Calculate grades exclusive to the third student
    return student_3 - (student_1 | student_2)


# Input grades for three students
student_1 = set(input().split())
student_2 = set(input().split())
student_3 = set(input().split())

# Get unique grades for the third student
unique_grades_student_3 = get_unique_grades(student_1, student_2, student_3)

# Output the result in descending order
print(*sorted(unique_grades_student_3, reverse=True, key=int))
