'''
TODO:
    A well-known Courier in the wastelands of Mojave has wandered
    into Hidden Valley, the secret bunker of the Brotherhood of Steel,
    and kindly agrees to help them solve their problems.

    One such problem was a strange computer virus that manifested itself
    in the form of program comments appearing on the
    Brotherhood of Steel's terminals.

    The Brotherhood programmers are known to never leave comments on the code
    and write programs in Python, so removing all these comments will not harm
    them in any way.

    Help the scribe Ibsen remove all comments from the program.
'''
from typing import List


def remove_comments(lines: List[str]) -> List[str]:
    """
    Removes all comments (marked by '#') from a given list of code lines.

    Args:
        lines (List[str]): A list of strings representing lines of code.

    Returns:
        List[str]: A list of strings with comments removed, preserving code
        before the '#' symbol.
    """
    cleaned_lines = []
    for line in lines:
        # Remove everything after '#' and strip trailing spaces
        cleaned_line = line.split('#', 1)[0].rstrip()
        cleaned_lines.append(cleaned_line)
    return cleaned_lines


# Input: Read the number of lines and the lines of code
n = int(input("Enter the number of lines: "))
code_lines = [input("Enter line: ") for _ in range(n)]

# Process: Remove comments
result = remove_comments(code_lines)

# Output: Print the cleaned lines
for line in result:
    print(line)
