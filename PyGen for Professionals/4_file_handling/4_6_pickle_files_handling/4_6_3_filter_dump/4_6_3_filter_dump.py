'''
TODO:
    Implement a filter_dump() function that takes three arguments in
    the following order:
        filename — the name of the pickle file, such as data.pkl
        objects — a list of arbitrary objects
        typename — the type of data

    The function should create a pickle file named filename that contains
    a serialized list of only those objects in the objects list
    whose type is typename.
NOTE:
    For example, calling the filter_dump() function as follows:
        filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
    should create a file numbers.pkl containing the serialized list:
        [1, 3, 4].
'''
import pickle
from typing import List, Any, Type


def filter_dump(
    filename: str, objects: List[Any], typename: Type[Any]
) -> None:
    """
    Filters objects by type and serializes the result to a pickle file.

    Args:
        filename (str): The name of the pickle file.
        objects (List[Any]): The list of objects to be filtered.
        typename (Type[Any]): The type to filter elements by.

    Raises:
        IOError: If the file cannot be opened or written to.
        pickle.PickleError: If an error occurs during pickling.
    """
    try:
        filtered_objects = [
            obj for obj in objects if isinstance(obj, typename)
        ]

        with open(filename, 'wb') as file:
            pickle.dump(filtered_objects, file)

    except (IOError, pickle.PickleError) as error:
        print(f"Error while writing to {filename}: {error}")
