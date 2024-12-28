'''
TODO:
    Recall that the string find('a') method returns the location of
    the first occurrence of the character 'a' in the string.

    The problem is that this method does not find the location of all "a"'s.

    Write a function called find_all(target, symbol) that takes two arguments:
        the string target and the symbol symbol, and returns a list containing
        all locations of that symbol in the string.

NOTE:
    If the specified character does not occur in the string,
    then an empty list should be returned.
'''


def find_all(target: str, symbol: str) -> list[int]:
    """
    Returns a list containing all the indices of the specified symbol
    in the given string.

    This function iterates through the string and checks each character.
    If the character matches the specified symbol, its index is added
    to the result list.

    Args:
    target (str): The string in which to search for the symbol.
    symbol (str): The character to search for in the string.

    Returns:
    list[int]: A list of indices where the symbol appears in the string.
    """
    return [i for i in range(len(target)) if target[i] == symbol]


# Example usage
s = input()  # Read the input string
char = input()  # Read the character to find
print(find_all(s, char))  # Call the function and print the result
