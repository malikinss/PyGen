'''
TODO:
    The program receives three strings as input: first name,\
    last name, and patronymic. Write a program that prints out the
    initials of a person.

NOTE:
    It is guaranteed that the first name, last name and patronymic
    begin with a capital letter.
'''


def get_initials(first_name: str, last_name: str, middle_name: str) -> str:
    """
    Given a first name, last name, and patronymic, this function returns
    the initials of the person in the format:
        LastName FirstInitial MiddleInitial.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        middle_name (str): The patronymic of the person.

    Returns:
        str: The initials in the format "Lastname FirstInitial MiddleInitial".
    """
    return last_name[0] + first_name[0] + middle_name[0]


# Input from the user
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
middle_name = input("Enter patronymic: ")

# Output the initials
initials = get_initials(first_name, last_name, middle_name)
print(initials)
