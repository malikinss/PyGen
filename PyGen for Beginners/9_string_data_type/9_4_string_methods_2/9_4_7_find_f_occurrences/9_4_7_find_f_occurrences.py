'''
TODO:
    The input to the program is a string of text.

    If the letter "f" occurs only once in this string, print its index.

    If it occurs two or more times, print the index of its first and
    last occurrence on the same line, separated by a space character.

    If the letter "f" does not occur in the given string, print "NO".
'''


def find_f_occurrences(given_string):
    # Initialize variables for storing the first and last occurrence
    first_index = -1
    last_index = -1

    # Loop through the string to find the first and last occurrence of 'f'
    for i, char in enumerate(given_string):
        if char == 'f':
            if first_index == -1:
                first_index = i
            last_index = i

    # Output the result based on the occurrences
    if first_index == -1:
        return "NO"
    elif first_index == last_index:
        return str(first_index)
    else:
        return f"{first_index} {last_index}"


# Input from the user
given_string = input()

# Call the function and print the result
print(find_f_occurrences(given_string))
