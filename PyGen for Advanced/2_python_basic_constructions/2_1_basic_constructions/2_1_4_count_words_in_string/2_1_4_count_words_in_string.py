'''
TODO:
    Given a string consisting of words separated by spaces.
    Write a program that counts the number of words in this string.

NOTE:
    In addition to words, the text may contain only spaces (one or more).
'''


def count_words_in_string(text: str) -> int:
    """
    Counts the number of words in a given string. Words are separated
    by spaces.

    Args:
        text (str): The input string containing words separated by spaces.

    Returns:
        int: The number of words in the string.
    """
    # Split the string by spaces and filter out empty parts
    # caused by multiple spaces
    words = text.split()

    return len(words)


def main() -> None:
    """
    Main function to take input, count the words in the input string,
    and print the result.
    """
    input_string = input("Enter the text: ")
    print(count_words_in_string(input_string))


if __name__ == "__main__":
    main()
