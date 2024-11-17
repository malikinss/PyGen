'''
TODO:
    The input to the program is a string of text.

    Write a program that checks if a string ends with
    the substring .com or .co.il.
'''


def check_domain(given_text: str) -> str:
    """
    Checks if the string ends with the substring '.com' or '.co.il'.

    Args:
        given_text (str): The string to check.

    Returns:
        str: 'YES' if the string ends with '.com' or '.co.il', 'NO' otherwise.
    """
    if given_text.endswith('.com') or given_text.endswith('.co.il'):
        return 'YES'
    else:
        return 'NO'


# User input
given_text = input("Enter a string: ")

# Check and print the result
result = check_domain(given_text)
print(result)
