'''
TODO:
    Three students are given computer science grades on a 10-point scale.

    Write a program that outputs the set of grades that both the first
    and second students have, but the third student does not have.
NOTE:
    The student's grade is in the range from 0 to 10 inclusive.
'''
from typing import List


def find_grades(student1: set, student2: set, student3: set) -> List:
    """
    Finds the grades common to the first and second students but not present
    in the third student.

    Args:
        student1 (set): Grades of the first student.
        student2 (set): Grades of the second student.
        student3 (set): Grades of the third student.

    Returns:
        List: Sorted list of grades meeting the criteria, in descending order.
    """
    common_grades = student1 & student2
    result = common_grades - student3
    return sorted(result, reverse=True, key=int)


grades_student1 = set(input("Enter grades for student 1: ").split())
grades_student2 = set(input("Enter grades for student 2: ").split())
grades_student3 = set(input("Enter grades for student 3: ").split())

output_grades = find_grades(grades_student1, grades_student2, grades_student3)
print(*output_grades)
