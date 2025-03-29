'''
TODO:
        Let's call a bracket sequence a string consisting of the
        characters ( and ).

        We will consider a bracket sequence correct if:
            - for each opening bracket there is a closing bracket
            - brackets are closed in the correct order, that is, in each
            pair of opening and closing brackets, the opening one is to
            the left

        Write a program that determines whether a bracket sequence is
        correct.

        Input:
            The program receives a string representing a bracket
            sequence as input.

        Output:
            The program should output True if the input bracket sequence
            is correct, or False otherwise.
'''


def is_valid_parentheses(bracket_sequence: str) -> bool:
    """
    Checks if the bracket sequence is valid, i.e., each opening bracket
    has a corresponding closing bracket, and they are in correct order.

    Args:
        bracket_sequence (str): The input string consisting of
        '(', ')', '[', ']', '{', and '}'.

    Returns:
        bool: True if the sequence is valid, False otherwise.
    """
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in bracket_sequence:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack


if __name__ == "__main__":
    print(is_valid_parentheses(input()))
