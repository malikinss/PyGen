'''
TODO:
    Each student studying at the BEEGEEK online school studies either math,
    computer science, or both.

    The school principal has lists of students studying each subject.

    Write a program that allows the principal to find out how many students
    study only math.

NOTE:
    It is guaranteed that there are no students with the same last name
    at BEEGEEK.
'''


def count_only_math_students(
    math_students: set, informatics_students: set
) -> int:
    """
    Determines how many students study only math, based on the given sets
    of math and informatics students.

    Args:
        math_students (set): A set of students studying math.
        informatics_students (set): A set of students studying informatics.

    Returns:
        int: The number of students studying only math.
    """
    # Students studying both subjects
    students_for_both_subjects = math_students & informatics_students

    # Students studying only math
    only_math_students = math_students - students_for_both_subjects

    return len(only_math_students)


def main() -> None:
    """
    Main function to read input, compute and output the number of students
    studying only math.
    """
    # Input reading
    math_students_number = int(input())
    informatics_students_num = int(input())

    math_students = {input() for _ in range(math_students_number)}
    informatics_students = {input() for _ in range(informatics_students_num)}

    # Compute and print the result
    result = count_only_math_students(math_students, informatics_students)
    print(result)


if __name__ == "__main__":
    main()
