'''
TODO:
    At the BEEGEEK online school, we are always monitoring how our popularity
    is growing.

    To do this, we collect posts from various social networks that contain
    occurrences of the string beegeek in lowercase.

    We rate a post:
        - 3 points if it begins and ends with the string beegeek
        - 2 points if it only begins or ends with the string beegeek
        - 1 point if it contains the string beegeek only inside
        - 0 points if it does not contain the string beegeek

    Write a program that determines the popularity of the BEEGEEK online
    school by summing up the points of all posts.

    The program is given an arbitrary number of lines as input, each of which
    represents a subsequent post.

    The program must determine how many points each entered post is worth and
    output the sum of all the points received.

NOTE:
    If a post is just the string beegeek, then it is worth 2 points.
'''
import re
import sys
from typing import List


def read_lines_from_input() -> List[str]:
    """
    Reads input lines from stdin.

    This function reads all input lines, strips trailing
    whitespace, and returns them as a list of strings.

    Returns:
        List[str]: A list of strings representing the input lines.
    """
    return [line for line in sys.stdin.readlines()]


def calculate_popularity_score(lines: List[str]) -> None:
    """
    Determines the popularity score based on occurrences of 'beegeek'.

    Points are assigned as follows:
    - 3 points if the post begins and ends with 'beegeek'
    - 2 points if the post starts or ends with 'beegeek'
    - 1 point if 'beegeek' appears inside the text
    - 0 points if 'beegeek' is absent

    Args:
        lines (List[str]): A list of posts.

    Returns:
        None: Outputs the total score.
    """
    total_score = 0

    patterns = {
        3: r'^beegeek$|^beegeek.*beegeek$',
        2: r'^beegeek.*$|^.*beegeek$',
        1: r'beegeek'
    }

    for line in lines:
        for points, regex in patterns.items():
            if re.search(regex, line):
                total_score += points
                break

    print(total_score)


calculate_popularity_score(read_lines_from_input())
