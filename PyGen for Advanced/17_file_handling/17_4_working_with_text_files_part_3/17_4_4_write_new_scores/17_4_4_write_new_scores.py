'''
TODO:
    A text file is available to you "class_scores.txt " with grades for the
    final test on lines like:
        - surname assessment (surname and assessment are separated by a space).

    The score is an integer from 0 to 100 inclusive.

    Write a program to add 5 points for each test result and output of
    surnames and new test results to a file "new_scores.txt ".

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''
from typing import List

SCORE_INCREMENT = 5  # Константа для увеличения баллов


def read_data_from_file(file_name: str) -> List[str]:
    """
    Reads the contents of a text file and returns a list of its lines without
    trailing newlines.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - List[str]: A list of strings representing the file's lines.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]


def write_data_to_file(file_name: str, data: List[str]) -> None:
    """
    Writes a list of strings to a file, each followed by a newline.

    Parameters:
    - file_name (str): The name of the file to write to.
    - data (List[str]): A list of strings to be written.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(f"{line}\n" for line in data)


def get_new_score(score: str, score_to_add: int) -> int:
    """
    Computes the new score after adding points, ensuring it does not exceed
    100.

    Parameters:
    - score (str): The original score as a string.
    - score_to_add (int): The number of points to add.

    Returns:
    - int: The updated score, capped at 100.
    """
    return min(int(score) + score_to_add, 100)


def add_scores(data: List[str], score_to_add: int) -> List[str]:
    """
    Increases each student's score by a given amount, ensuring it does not
    exceed 100.

    Parameters:
    - data (List[str]): A list of strings, each containing a surname and
                        a score.
    - score_to_add (int): The number of points to add to each score.

    Returns:
    - List[str]: A new list of formatted strings with updated scores.
    """
    return [f"{surname} {get_new_score(score_str, score_to_add)}"
            for surname, score_str in (row.split() for row in data)]


def write_new_scores(
    file_to_read: str, file_to_write: str, score_to_add: int
) -> None:
    """
    Reads scores from a file, adds a specified amount of points to each score,
    and writes the updated scores to a new file.

    Parameters:
    - file_to_read (str): The input file containing original scores.
    - file_to_write (str): The output file for the updated scores.
    - score_to_add (int): The number of points to add to each score.
    """
    data = read_data_from_file(file_to_read)
    updated_data = add_scores(data, score_to_add)
    write_data_to_file(file_to_write, updated_data)


write_new_scores('class_scores.txt', 'new_scores.txt', SCORE_INCREMENT)
