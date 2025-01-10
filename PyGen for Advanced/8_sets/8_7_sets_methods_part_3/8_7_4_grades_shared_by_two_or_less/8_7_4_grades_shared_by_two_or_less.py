'''
TODO:
    Given are the math grades of three students on a 10-point scale.

    Write a program that outputs grades that are shared by no more than
    two students.
NOTE:
    The student's grade is in the range from 0 to 10 inclusive.
'''


def grades_shared_by_two_or_less(
    student1: set, student2: set, student3: set
) -> set:
    """
    Finds grades shared by no more than two students.

    Args:
        student1 (set): Grades of the first student.
        student2 (set): Grades of the second student.
        student3 (set): Grades of the third student.

    Returns:
        set: Grades shared by no more than two students.
    """
    # All grades
    all_grades = student1 | student2 | student3

    # Grades shared by all three students
    shared_by_all = student1 & student2 & student3

    # Result: Grades shared by no more than two students
    return all_grades - shared_by_all


# Input data
student1_grades = set(input("Enter grades for student 1: ").split())
student2_grades = set(input("Enter grades for student 2: ").split())
student3_grades = set(input("Enter grades for student 3: ").split())

# Process and output result
result_grades = grades_shared_by_two_or_less(
    student1_grades, student2_grades, student3_grades
)
print(*sorted(result_grades, key=int))
