'''
TODO:
    Given a string of text consisting of the letters "H" and "T".

    The letter "H" corresponds to the appearance of Heads, and the letter "T"
    to the appearance of Tails.

    Write a program that counts the greatest number of consecutive Heads.

NOTE:
    If there are no Tails, then you need to output the number 0.
'''


def count_max_heads(s: str) -> int:
    """
    Counts the greatest number of consecutive 'H's in the given string.

    Parameters:
    - s (str): The input string consisting of 'H' and 'T'.

    Returns:
    - int: The maximum number of consecutive 'H's.
    """
    max_heads = 0  # To track the maximum consecutive heads
    current_heads = 0  # To track the current streak of heads

    for char in s:
        if char == 'H':
            current_heads += 1  # Increase the current streak of heads

            # Update the maximum streak
            max_heads = max(max_heads, current_heads)
        else:
            current_heads = 0  # Reset the streak when 'T' is encountered

    return max_heads


# Input the string of 'H' and 'T'
s = input()

# Output the result
print(count_max_heads(s))
