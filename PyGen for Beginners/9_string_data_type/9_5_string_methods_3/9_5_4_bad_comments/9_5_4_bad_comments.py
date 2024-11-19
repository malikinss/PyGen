'''
TODO:
    On the Stepik platform, users leave comments, but not all of them comply
    with the rules.

    For example, moderator Sam considers inappropriate comments that
    are an empty line or consist only of spaces.

    He deletes such comments - there is no need to pollute the course with
    useless material!

    Your task is to write a program that will help Sam check comments.

    The program should accept a natural number n as input, and then n lines
    representing the texts of comments.

    For each comment, your program should output the number of this comment
    (starting with 1), then a colon (:), then its text after a space
    or the message "COMMENT SHOULD BE DELETED" (without quotes) if the comment
    should be deleted by Sam.
'''


def is_bad_comment(text: str) -> bool:
    """
    Checks whether a comment is inappropriate.

    Args:
        text (str): The text of the comment.

    Returns:
        bool: True if the comment is empty or contains only spaces,
        otherwise False.
    """
    return text.strip() == ""


def mark_bad_comments():
    """
    Validates and marks comments, printing their number and text,
    or "COMMENT SHOULD BE DELETED" for inappropriate comments.
    """
    number_of_comments = int(input())

    for i in range(1, number_of_comments + 1):
        comment = input()

        if is_bad_comment(comment):
            comment = "COMMENT SHOULD BE DELETED"

        print(f"{i}: {comment}")


# Run the program
mark_bad_comments()
