'''
TODO:
    Modify the above code so that it outputs a "reversed" list
    of languages (i.e. the elements will go in reverse order).
'''
from typing import List

# original code
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
             'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

# fixed code


def reverse_list(lst: List[str]) -> List[str]:
    """
    Returns the reversed version of the provided list of strings.
    """
    return lst[::-1]


# Original list of languages
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
             'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

# Call the function and print the reversed list
print(reverse_list(languages))
