'''
TODO:
    The file data.txt is given.
    It was necessary to write a program that determines how many lines are
    contained in this file and displays the result.

    The programmer was in a hurry and wrote the program incorrectly.

    Find and correct all the errors made in this program (there are exactly 3).

NOTE:
    It is known that each error affects only one line and can be corrected
    without changing other lines.
'''
# original code
total = 0

with open('', encoding='utf-8') as file:
    for _ in file.readlines:
        total == total + 1

print(total)


# fixed code
def count_lines(filename: str) -> int:
    """
    Counts the number of lines in a given file.

    Args:
        filename (str): The path to the file.

    Returns:
        int: The number of lines in the file.
    """
    with open(filename, encoding='utf-8') as file:
        return sum(1 for _ in file)


print(count_lines('data.txt'))
