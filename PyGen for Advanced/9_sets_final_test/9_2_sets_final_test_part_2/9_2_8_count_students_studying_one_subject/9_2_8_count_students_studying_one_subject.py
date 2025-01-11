'''
TODO:
    Each student at the BEEGEEK online school studies either math or computer
    science, or both.

    The school principal has lists of students studying each subject.

    Write a program that allows the principal to find out how many students
    study only one subject.

NOTE:
    It is guaranteed that there are no students with the same last name
    at BEEGEEK.
'''


def count_students_studying_one_subject(
    math_students: set, informatics_students: set
) -> int:
    """
    Count how many students study only one subject (either math or informatics)

    Args:
        math_students (set): A set of students studying math.
        informatics_students (set): A set of students studying informatics.

    Returns:
        int: The number of students studying only one subject.
    """
    # Students studying both subjects
    students_for_both_subj = math_students & informatics_students

    # Students studying only math or only informatics
    only_math_students = math_students - students_for_both_subj
    only_informatics_students = informatics_students - students_for_both_subj

    # Total students studying only one subject
    return len(only_math_students) + len(only_informatics_students)


def main() -> None:
    """
    Main function to read input, compute and output the number of students
    studying only one subject.
    """
    # Input reading
    math_students_number = int(input())
    informatics_students_number = int(input())

    # Read names of math and informatics students
    math_students = {input() for _ in range(math_students_number)}
    informatic_students = {input() for _ in range(informatics_students_number)}

    # Compute and print the result
    result = count_students_studying_one_subject(
        math_students, informatic_students
    )

    # Output the result
    if result == 0:
        print("NO")
    else:
        print(result)


if __name__ == "__main__":
    main()
