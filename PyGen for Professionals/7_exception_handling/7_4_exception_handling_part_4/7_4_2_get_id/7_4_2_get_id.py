'''
TODO:
    In the BEEGEEK online school, a student's name is considered correct if it
    begins with a capital Latin letter followed by lowercase Latin letters.

    For example, the names Timur and Yo are considered correct, but the names
    timyrik, Yo17, TimuRRR are not.

    Also, each student has an identification number, represented by a natural
    number, which is issued upon admission to the school.

    For example, if there are 10 students in the school, then a new arriving
    student will receive an identification number equal to 11.

    Implement the get_id() function, which takes two arguments:
        names - a list of names of students studying at the school
        name - the name of the incoming student

    The function should return the identification number that the incoming
    student will receive.

    In this case:
        If the student name is not a string (type str), the function should
        throw an exception:
            TypeError('Name is not a string')

        If the student name is a string (type str), but does not represent
        a valid name, the function should throw an exception:
            ValueError('Name is not valid')
'''
from typing import List


def is_name_correct(name: str) -> bool:
    """
    Checks if the given name is valid.
    A valid name starts with a capital letter followed by lowercase letters.

    Args:
        name (str): The name to check.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return name.isalpha() and name[0].isupper() and name[1:].islower()


def get_id(names: List[str], name: str) -> int:
    """
    Returns the identification number for a new student.
    The ID is the current number of students plus one.

    Args:
        names (List[str]): A list of current students' names.
        name (str): The name of the new student.

    Returns:
        int: The new student's identification number.

    Raises:
        TypeError: If name is not a string.
        ValueError: If name is not a valid student name.
    """
    if not isinstance(name, str):
        raise TypeError("Name is not a string")

    if not is_name_correct(name):
        raise ValueError("Name is not valid")

    return len(names) + 1
