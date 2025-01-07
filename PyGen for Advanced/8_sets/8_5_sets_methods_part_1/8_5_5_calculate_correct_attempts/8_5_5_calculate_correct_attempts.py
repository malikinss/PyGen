'''
TODO:
    Each task on Stepik has a widget with the percentage of correct solutions
    and the total number of solutions.

    Recently, Stepik has been having problems with the algorithm that updates
    this widget.

    Help Stepik and write a program that will count how many students have
    solved a task and how many correct attempts make up the total number
    of attempts.

    Your program receives the number n as input - the total number of attempts
    to solve the task.

    Then, n lines are input, each in the following format:
        <nickname>: <result of the checking system>
    where <result of the checking system> can only take two values:
        - Correct (the task was solved correctly)
        - Wrong (the task was solved incorrectly).

    Your program should count and output how many students solved the task
    correctly and how many correct attempts out of all in the following
    formats:
        - Correctly solved <number of students who solved correctly> students
        - Of all attempts <percentage of correct solutions>% correct
    where <number of students who solved correctly> - the number of unique
    students who solved the task correctly.

    In this case, if the task has no correct solutions yet, the program should
    output the text:
        - You can be the first to solve this task

    Your program should round the percentage of correct solutions to
    an integer according to mathematical rules.

NOTE:
    The percentage of solutions should be rounded according to mathematical
    rules:
        the number is rounded down if the fractional part is less than 0.5,
        or up otherwise.
        For example:
            8.25≈8
            8.5≈9
            8.75≈9

    It is guaranteed that the nickname cannot be the same for different
    students.

    It is guaranteed that the student's nickname cannot contain the colon
    symbol (:).
'''


def custom_round(number: float) -> int:
    """
    Rounds a number according to the following rules:
    - Round down if the fractional part is less than 0.5.
    - Round up if the fractional part is 0.5 or greater.

    Args:
        number (float): The number to round.

    Returns:
        int: The rounded number.
    """
    fractional_part = number - int(number)
    if fractional_part >= 0.5:
        return int(number) + 1
    else:
        return int(number)


def calculate_correct_attempts(n: int) -> tuple[int, float]:
    """
    Processes the attempts and returns the number of unique students who
    solved the task correctly and the percentage of correct solutions.

    Args:
        n (int): The total number of attempts.

    Returns:
        tuple[int, float]: The number of students who solved correctly and
                            the percentage of correct solutions.
    """
    correct_students = set()
    correct_attempts = 0

    for _ in range(n):
        attempt_data = input().split(': ')
        if attempt_data[1] == 'Correct':
            correct_students.add(attempt_data[0])
            correct_attempts += 1

    if correct_attempts == 0:
        return 0, 0.0

    correct_percentage = custom_round(correct_attempts / (n / 100))
    return len(correct_students), correct_percentage


def print_result(students_amount: int, percentage: float):
    """
    Prints the results based on the number of students who solved correctly
    and the percentage of correct attempts.

    Args:
        students_amount (int): The number of students who solved the task
                                correctly.
        percentage (float): The percentage of correct attempts.
    """
    if students_amount > 0:
        print(f'Correctly solved {students_amount} students')
        print(f'Of all attempt {percentage}% correct')
    else:
        print('You can be the first to solve this task')


n = int(input())
students_amount, correct_percentage = calculate_correct_attempts(n)
print_result(students_amount, correct_percentage)
