'''
TODO:
    Three students are given grades in biology on a 10-point scale.

    Write a program that outputs the set of grades that none of the
    three students have.
NOTE:
    The student's grade is in the range from 0 to 10 inclusive.
'''
from typing import Set


def get_missing_grades(
    student_1: Set[str], student_2: Set[str], student_3: Set[str]
) -> Set[str]:
    """
    Returns the set of grades from 0 to 10 that none of the students have.

    Args:
        student_1 (Set[str]): Grades of the first student.
        student_2 (Set[str]): Grades of the second student.
        student_3 (Set[str]): Grades of the third student.

    Returns:
        Set[str]: The set of grades that are not present in any student's
                  grades.
    """
    # All possible grades from 0 to 10
    full_grade_range = {str(i) for i in range(11)}

    # Combine grades of all students
    all_student_grades = student_1 | student_2 | student_3

    # Return grades that are not in any student's grades
    return full_grade_range - all_student_grades


# Input grades for three students
student_1 = set(input().split())
student_2 = set(input().split())
student_3 = set(input().split())

# Calculate missing grades
missing_grades = get_missing_grades(student_1, student_2, student_3)

# Output the result in ascending order
print(*sorted(missing_grades, key=int))
