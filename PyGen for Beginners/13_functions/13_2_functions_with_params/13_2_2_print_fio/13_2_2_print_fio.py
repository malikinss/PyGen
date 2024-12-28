'''
TODO:
    Write a print_fio(name, surname, patronymic) function that takes three
    parameters:
        - name - the name of the person;
        - surname - the surname of the person;
        - patronymic - patronymic of a person;

    and then prints out the name of the person.

NOTE:
    Provide for the fact that all three letters in the full name must
    be uppercase.
'''


def print_fio(name: str, surname: str, patronymic: str) -> None:
    """
    Prints the initials of a person's full name in uppercase.

    The function takes three parameters: name, surname, and patronymic,
    and prints out the initials (the first letter of each) in uppercase.

    Args:
    name (str): The person's first name.
    surname (str): The person's surname.
    patronymic (str): The person's patronymic.

    Returns:
    None
    """
    # Print the initials of the name, surname, and patronymic in uppercase
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


# Example usage:
name = input()
surname = input()
patronymic = input()

print_fio(name, surname, patronymic)
