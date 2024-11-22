'''
TODO:
    The program is given a string of text in which the letter "h" occurs
    at least twice.

    Write a program that returns the original string and reverses the sequence
    of characters between the first and last occurrences of the letter "h".
'''


def reverse_between_h(s: str) -> str:
    # Find the index of the first and last occurrences of 'h'
    first_h_index = s.find('h')
    last_h_index = s.rfind('h')

    # Reverse the substring between the first and last 'h'
    reversed_substring = s[first_h_index + 1:last_h_index][::-1]

    # Return the string with the reversed part
    return s[:first_h_index + 1] + reversed_substring + s[last_h_index:]


# Read the input and call the function
print(reverse_between_h(input()))
