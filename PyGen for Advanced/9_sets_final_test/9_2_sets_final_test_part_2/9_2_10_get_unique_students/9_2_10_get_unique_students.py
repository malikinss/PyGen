'''
TODO:
    Each student studying at the BEEGEEK online school studies either math
    or computer science, or both.

    The school principal has lists of students studying each subject.

    By chance, the lists of all students are mixed up.

    Write a program that will allow the principal to find out how many
    students study only one subject.

NOTE:
    It is guaranteed that there are no students with the same last name
    at BEEGEEK.
'''


def get_unique_students(math_students: set, informatics_students: set) -> int:
    """
    Returns the number of students studying only one subject.

    Args:
        math_students (set): A set containing students studying math.
        informatics_students (set): A set containing students studying
                                    informatics.

    Returns:
        int: The number of students studying only one subject.
    """
    # Students studying only math
    only_math = math_students - informatics_students
    # Students studying only informatics
    only_informatics = informatics_students - math_students

    # Total number of students studying only one subject
    return len(only_math) + len(only_informatics)


def get_set_from_input(size: int) -> set:
    """
    Reads input for a set of students.

    Args:
        size (int): The number of students to input.

    Returns:
        set: A set of student names.
    """
    return {input(f"Enter student {i+1}: ") for i in range(size)}


def main() -> None:
    """
    Main function to read input, compute, and output the number of students
    studying only one subject (either math or informatics).
    """
    # Read number of students in math and informatics
    math_students_number = int(input())
    informatics_students_number = int(input())

    # Read the students for each subject
    print(f"Enter {math_students_number} math students' names:")
    math_students = get_set_from_input(math_students_number)

    print(f"Enter {informatics_students_number} informatics students' names:")
    informatics_students = get_set_from_input(informatics_students_number)

    # Get the number of students studying only one subject
    result = get_unique_students(math_students, informatics_students)

    # Output the result
    if result == 0:
        print("NO")
    else:
        print(result)


if __name__ == "__main__":
    main()
