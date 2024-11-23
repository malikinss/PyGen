'''
TODO:
    The input to the program is a text string containing the name,
    patronymic and surname of the person.

    Write a program that prints out the initials of a person.
'''


def print_initials(full_name: str) -> None:
    """
    This function takes a full name containing the first name, patronymic,
    and surname, and prints the initials in the format: F.P.S.

    Args:
        full_name (str): The full name of a person, consisting of first name,
        patronymic, and surname.

    Returns:
        None: The function prints the initials in the format "F.P.S." without
        a newline at the end.
    """
    name_parts = full_name.split()
    print(name_parts[0][0], name_parts[1][0], name_parts[2][0], sep=".", end=".")


# Input the full name
name = input()

# Call the function with the input name
print_initials(name)
