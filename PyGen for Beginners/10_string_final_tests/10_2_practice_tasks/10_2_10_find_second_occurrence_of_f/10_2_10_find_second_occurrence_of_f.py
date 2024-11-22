'''
TODO:
    The program is given a string of text as input.

    Write a program that prints the index of the second occurrence
    of the letter "f".

    If the letter "f" occurs only once, print the number -1, and
    if it does not occur at all, print the number -2.
'''


def find_second_occurrence_of_f(text: str) -> int:
    first_index = text.find('f')

    # If 'f' doesn't exist at all
    if first_index == -1:
        return -2

    # Find the second occurrence by searching after the first found index
    second_index = text.find('f', first_index + 1)

    # Will return -1 if not found, or the actual index if found
    return second_index


# Read input and call the function
print(find_second_occurrence_of_f(input()))
