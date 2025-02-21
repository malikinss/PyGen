'''
TODO:
    Find and correct the errors in the program below so that it serializes
    the dogs dictionary and writes the result to the dogs.pkl file.
'''
import pickle
from typing import Any


def create_pickle(data: Any, filename: str) -> None:
    """
    Serializes the given data to a pickle file.

    Args:
        data (Any): The data to be serialized.
        filename (str): The name of the pickle file.

    Raises:
        IOError: If the file cannot be opened or written.
        pickle.PickleError: If serialization fails.
    """
    try:
        with open(filename, mode='wb') as file:
            pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
    except (IOError, pickle.PickleError) as error:
        print(f"Error while writing to {filename}: {error}")


dogs = {
    'Ozzy': 2, 'Filou': 7,
    'Luna': 4, 'Skippy': 11,
    'Barco': 13, 'Balou': 10,
    'Laika': 15
}

create_pickle(dogs, 'dogs.pkl')
