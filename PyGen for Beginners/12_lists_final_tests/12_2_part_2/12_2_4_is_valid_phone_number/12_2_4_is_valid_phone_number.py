'''
TODO:
    The input to the program is a string of text.

    Write a program that determines if an input string is a valid phone number.

    A string of text is a valid phone number if it has the format:
        - abc-def-hijk or
        - 7-abc-def-hijk,
    where a, b, c, d, e, f, h, i, j, k are numbers from 0 to 9.
'''


def is_valid_phone_number(phone: str) -> str:
    """
    Determines if the input string is a valid phone number.

    A valid phone number follows these formats:
        - abc-def-hijk
        - 7-abc-def-hijk

    Where each letter is a digit (0-9).

    Args:
        phone (str): The input phone number as a string.

    Returns:
        str: "YES" if the phone number is valid, "NO" otherwise.
    """
    seq = phone_number.split("-")
    lens = [len(el) for el in seq]

    if lens == [3, 3, 4] and "".join(seq).isdigit():
        return "YES"
    elif lens == [1, 3, 3, 4] and seq[0] == "7" and "".join(seq[1:]).isdigit():
        return "YES"
    else:
        return "NO"


# Input string
phone_number = input()

# Output whether the phone number is valid
print(is_valid_phone_number(phone_number))
