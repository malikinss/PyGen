'''
TODO:
    Write a function is_correct_bracket(text) that takes as an argument
    a non-empty string text consisting of the characters ( and ) and
    returns True if the input string is a correct bracket sequence
    and False otherwise.

NOTE:
    A regular bracket sequence is a string consisting only of the
    characters ( and ), where each opening bracket has a matching closing
    bracket (and each opening bracket must be to the left of its corresponding
    closing bracket).
'''


def is_correct_bracket(text: str) -> bool:
    """
    Checks if the given text has a correct bracket sequence.

    A correct bracket sequence consists only of the characters '(' and ')',
    where each opening bracket '(' has a matching closing bracket ')'
    and no closing bracket comes before its matching opening bracket.

    Args:
        text (str): The string containing the bracket sequence to check.

    Returns:
        bool: True if the sequence is correct, False otherwise.
    """
    balance = 0

    for char in text:
        if char == '(':
            balance += 1  # Increment for an opening bracket
        elif char == ')':
            balance -= 1  # Decrement for a closing bracket

            # If balance goes negative, there is a closing bracket without
            # a matching opening
            if balance < 0:
                return False

    # The sequence is correct if balance ends up at 0
    # (all opening brackets have matching closing brackets)
    return balance == 0


# Example usage
txt = input()
print(is_correct_bracket(txt))
