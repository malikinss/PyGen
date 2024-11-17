'''
TODO:
    The input to the program is one word written in lower case.

    Write a program that determines if it is a palindrome.

    The program should output "YES" if the word is a palindrome
    and "NO" otherwise.
'''


def is_palindrome(word: str) -> str:
    """
    Determines if the given word is a palindrome.

    Args:
        word (str): The word to be checked, in lowercase.

    Returns:
        str: "YES" if the word is a palindrome, "NO" otherwise.
    """
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return "NO"
        i += 1
        j -= 1
    return "YES"


# User input
word = input("Enter a word: ")

# Call the function and print the result
print(is_palindrome(word))
