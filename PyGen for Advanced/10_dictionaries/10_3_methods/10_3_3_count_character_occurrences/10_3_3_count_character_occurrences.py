"""
TODO:
    Complete the code below so that the result variable stores a dictionary
    that counts the number of occurrences of each character in the text string.

NOTE:
    You don't need to print the contents of the result dictionary.
"""
from typing import Dict


def count_character_occurrences(text: str) -> Dict[str, int]:
    """
    Counts the number of occurrences of each character in the given text
    string.

    Args:
        text (str): The input string to analyze.

    Returns:
        Dict[str, int]: A dictionary where keys are characters, and values are
        their counts.
    """
    result: Dict = {}
    for symbol in text:
        result[symbol] = result.get(symbol, 0) + 1
    return result


# Example usage
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = count_character_occurrences(text)
