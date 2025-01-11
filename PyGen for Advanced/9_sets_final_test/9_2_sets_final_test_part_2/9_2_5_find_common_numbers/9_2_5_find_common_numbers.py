'''
TODO:
    As you know, mathematicians are strange people 🤪.

    Timur, the author of this course, is no exception. Every day, Timur solves
    exactly two difficult math problems.

    While solving the first problem, he writes down all the numbers that
    appear in it on the first piece of paper.

    Then he pauses and takes up the second problem.

    Then he writes down all the numbers that appear in it on the second piece
    of paper.

    After that, he takes another piece of paper and writes down all
    the matching numbers from the first two pieces of paper.

    If there are such numbers, the day was a success;
    If there are no common numbers, Timur considers the day unlucky.

    Write a program that finds the common numbers of two pieces of paper
    or reports that the day was a failure. 😏
'''


def find_common_numbers(task1_numbers: set, task2_numbers: set) -> set:
    """
    Finds the common numbers between two sets of numbers.

    Args:
        task1_numbers (set): A set containing numbers from the first task.
        task2_numbers (set): A set containing numbers from the second task.

    Returns:
        set: A set containing the common numbers between the two input sets.
    """
    return task1_numbers & task2_numbers


def print_common_numbers(common_numbers: set) -> None:
    """
    Prints the common numbers in descending order if any are found, otherwise
    prints "BAD DAY".

    Args:
        common_numbers (set): A set containing the common numbers between
                              tasks.

    Returns:
        None: This function only prints the result.
    """
    if common_numbers:
        print(*sorted(common_numbers, reverse=True, key=int))
    else:
        print("BAD DAY")


def main() -> None:
    """
    Main function to read input and output the common numbers between
    two tasks.
    """
    numbers_from_task1 = set(input().split())
    numbers_from_task2 = set(input().split())

    common_numbers = find_common_numbers(
        numbers_from_task1, numbers_from_task2
    )
    print_common_numbers(common_numbers)


if __name__ == "__main__":
    main()
