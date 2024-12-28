'''
TODO:
    Write a function is_one_away(word1, word2) that takes two words word1
    and word2 as arguments and returns True if the words are the same length
    and differ by exactly 1 character and False otherwise.
'''


def is_one_away(word1: str, word2: str) -> bool:
    """
    Check if two words differ by exactly one character and have
    the same length.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        bool: True if the words differ by exactly one character and
              are the same length, False otherwise.
    """
    if len(word1) != len(word2):
        return False

    diff_count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                # No need to check further if more than 1 mismatch
                return False

    return diff_count == 1


# Example usage
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))
