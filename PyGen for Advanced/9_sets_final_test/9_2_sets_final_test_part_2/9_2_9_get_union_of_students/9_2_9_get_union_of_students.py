'''
TODO:
    The head of the online school BEEGEEK and his assistant remember
    the students of their school.

    To do this, each of them made a list of the students they remembered.

    Write a program that will output the names of all the students that
    the head and his assistant remembered.

NOTE:
    It is guaranteed that there are no students with the same last name
    at BEEGEEK.
'''


def get_union_of_students(
    managers_list: frozenset, assistant_list: frozenset
) -> frozenset:
    """
    Returns the union of two sets of student names, representing all students
    remembered by both the head and the assistant.

    Args:
        managers_list (frozenset): A frozenset of students remembered by
                                    the head.
        assistant_list (frozenset): A frozenset of students remembered by
                                    the assistant.

    Returns:
        frozenset: A frozenset containing all unique students from both lists.
    """
    return managers_list.union(assistant_list)


def main() -> None:
    """
    Main function to read input, compute, and output the union of remembered
    students' names.
    """
    # Read input for students remembered by the head and assistant
    managers_list = frozenset(input().split())
    assistant_list = frozenset(input().split())

    # Get the union of both sets
    result_list = get_union_of_students(managers_list, assistant_list)

    # Output the sorted list of students
    print(*sorted(result_list))


if __name__ == "__main__":
    main()
