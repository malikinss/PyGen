'''
TODO:
    Write a program that will convert a natural number to a string,
    replacing all digits in the number with words:
        0 to zero;
        1 to one;
        2 to two;
        3 to three;
        4 to four;
        5 to five;
        6 to six;
        7 to seven;
        8 to eight;
        9 to nine.

NOTE:
    Use a dictionary instead of the conditional operator.
'''

# Dictionary for mapping digits to words
NUMBERS_LUT = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}


def convert_number_to_words(number_string: str) -> str:
    """
    Converts a string representation of a number to a string where the digits
    are replaced by words.

    Arguments:
    number_string: (str) -- a string containing digits

    Returns:
    (str) -- a string with digits replaced by corresponding words
    """
    text_nums = [NUMBERS_LUT[digit] for digit in number_string]
    return ' '.join(text_nums)


# Taking user input and printing the result
given_number_string = input("Enter a number: ")
result = convert_number_to_words(given_number_string)
print(result)
