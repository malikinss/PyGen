'''
TODO:
    The input to the program is one line.

    Write a program that outputs:
        - the third character of this line;
        - penultimate character of this line;
        - the first five characters of this string;
        - the entire line, except for the last two characters;
        - all characters with even indices;
        - all characters with odd indices;
        - all characters in reverse order;
        - all characters of the string through one in reverse order,
          starting with the last one.
'''


def analyze_string(input_string: str) -> None:
    """
    Analyzes the input string and performs the following tasks:
        - Outputs the third character.
        - Outputs the penultimate character.
        - Outputs the first five characters.
        - Outputs the string except the last two characters.
        - Outputs all characters with even indices.
        - Outputs all characters with odd indices.
        - Outputs all characters in reverse order.
        - Outputs every second character in reverse order starting
        from the last.

    Args:
        input_string (str): The string to be analyzed.

    Returns:
        None: Outputs the results directly.
    """
    # The third character of this line
    print(input_string[2])

    # Penultimate character of this line
    print(input_string[-2])

    # The first five characters of this string
    print(input_string[:5])

    # The entire line, except for the last two characters
    print(input_string[:-2])

    # All characters with even indices
    print(input_string[::2])

    # All characters with odd indices
    print(input_string[1::2])

    # All characters in reverse order
    print(input_string[::-1])

    # All characters of the string through one in reverse order,
    # starting with the last one
    print(input_string[::-1][::2])


# User input
user_string = input("Enter a string: ")

# Call the function
analyze_string(user_string)
