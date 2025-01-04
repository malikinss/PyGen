'''
TODO:
    Programmer Timur wrote a program to work with biographical data
    of Russian poets.

    The data is contained in tuples of the form (surname, year of birth,
    city of birth).

    During the program's operation, an error was detected in a tuple
    poet_data: ('Pushkin', 1799, 'Saint Petersburg').

    The place of birth is incorrectly indicated here, since Alexander Pushkin
    was born in Moscow.

    Complete the code below so that the variable poet_data contains
    the correct tuple (with the corrected value), and then output it.
'''
from typing import Tuple


def correct_poet_data(poet_data: Tuple) -> Tuple:
    """
    Corrects the place of birth of a poet in the given tuple.

    Args:
        poet_data (Tuple): A tuple containing the poet's surname,
                           year of birth, and city of birth.

    Returns:
        Tuple: A new tuple with the corrected city of birth.
    """
    poet_data_lst = list(poet_data)
    poet_data_lst[-1] = 'Москва'  # Correcting the city of birth

    return tuple(poet_data_lst)


# Initial data
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

# Correct the data
corrected_poet_data = correct_poet_data(poet_data)

# Output the corrected poet data
print(corrected_poet_data)
