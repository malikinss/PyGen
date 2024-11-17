'''
TODO:
    The input to the program is a string consisting of the person's first
    and last name, separated by a single space.

    Write a program that checks that the first and last names begin
    with a capital letter.
'''


def check_name_capitalization(name: str) -> str:
    """
    Checks if the first and last name in the given string begin
    with a capital letter.

    Args:
        name (str): The full name consisting of the first and last name,
        separated by a space.

    Returns:
        str: "YES" if both names start with a capital letter, otherwise "NO".
    """
    # Convert the string to title case
    # (capitalizing the first letter of each word)
    title_case_name = name.title()

    # Compare the original string with the title case version
    if name == title_case_name:
        return "YES"
    else:
        return "NO"


# User input
full_name = input("Enter your full name: ")

# Call the function and display the result
print(check_name_capitalization(full_name))
