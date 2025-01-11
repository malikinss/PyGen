'''
TODO:
    The head of the online school BEEGEEK wanted to know which of his students
    attended all the lessons since the beginning of the school year.

    For each lesson, there is a sheet with a list of the students who attended.

    Write a program that determines the names of the students who attended
    all the lessons.

NOTE:
    It is guaranteed that there are no students with the same last name
    at BEEGEEK.

    It is guaranteed that at least one student attended all lessons.
'''


def get_students_from_input() -> set:
    """
    Reads the list of students from input and returns it as a set.

    Returns:
        set: A set containing students' names.
    """
    return {input() for _ in range(int(input()))}


def get_students_attending_all_lessons(lessons_number: int) -> set:
    """
    Determines the students who attended all lessons.

    Args:
        lessons_number (int): The number of lessons.

    Returns:
        set: A set of students who attended all lessons.
    """
    # Initialize the set with students from the first lesson
    result = get_students_from_input()

    # Process each subsequent lesson
    for _ in range(lessons_number - 1):
        result &= get_students_from_input()

    return result


def print_students(students: set) -> None:
    """
    Prints the sorted list of students who attended all lessons.

    Args:
        students (set): A set of students who attended all lessons.
    """
    print(*sorted(students), sep="\n")


# Main execution
lessons_number = int(input())
students_attending_all = get_students_attending_all_lessons(lessons_number)
print_students(students_attending_all)
