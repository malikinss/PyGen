'''
TODO:
    The input to the program is a string of text.

    Write a program that determines whether a text tint is good or not.

    The text has a good tone if it contains the substring "good" in all
    possible cases.

    The program should output "YES" if the text has a good hue
    and "NO" otherwise.
'''


def has_good_tone(text: str) -> str:
    """
    Determines whether a given text has a 'good' tone. The text is considered
    to have a good tone if it contains the substring 'good' in any case.

    Args:
        text (str): The input text to check.

    Returns:
        str: "YES" if the text contains 'good' (case-insensitive),
        "NO" otherwise.
    """
    # Convert the text to lowercase and check if 'good' is in the text
    return "YES" if "good" in text.lower() else "NO"


# User input
input_text = input("Enter the text: ")

# Check and display the result
print(has_good_tone(input_text))
