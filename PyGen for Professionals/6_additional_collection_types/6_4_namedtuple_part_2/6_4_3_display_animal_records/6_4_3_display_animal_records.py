'''
TODO:
    You have access to a named tuple Animal, which contains data about
    an animal.

    The first element of the named tuple is the animal's name
    The second is the family
    The third is the sex
    The fourth is the color.

    There is also a file data.pkl, which contains a serialized
    list of such tuples.

    Complete the code below so that for each tuple in this list, it prints
    the names of its fields and the values of these fields in
    the following format:
        name: <value>
        family: <value>
        sex: <value>
        color: <value>

    There must be an empty line between the fields and values of two
    different tuples.

NOTE:
    The contents of the first tuple in the list must come first, then the
    second, and so on.

    For example, if the data.pkl file contained the following
    serialized list:

    [Animal(name='Alex', family='dogs', sex='m', color='brown'),
    Animal(name='Nancy', family='dogs', sex='w', color='black')]
    then the program would output:

        name: Alex
        family: dogs
        sex: m
        color: brown

        name: Nancy
        family: dogs
        sex: w
        color: black
'''
import pickle
from typing import List, Any
from collections import namedtuple

# Define the named tuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])


def deserialize_pickle_file(pickle_file_path: str) -> Any:
    """
    Deserializes an object from the given pickle file.

    Args:
        pickle_file_path (str): Path to the pickle file.

    Returns:
        Any: The deserialized object, typically a list of Animal namedtuples.
    """
    with open(pickle_file_path, 'rb') as file:
        return pickle.load(file)


def print_namedtuple_fields(animal: Animal) -> None:
    """
    Prints the fields and values of a namedtuple in the specified format.

    Args:
        animal (Animal): The namedtuple containing animal data.
    """
    for field, value in animal._asdict().items():
        print(f'{field}: {value}')


def display_animal_records(animals: List[Animal]) -> None:
    """
    Displays the formatted records of a list of namedtuples, with an empty line
    between each animal's information.

    Args:
        animals (List[Animal]): The list of namedtuples containing animal data.
    """
    for i, animal in enumerate(animals):
        print_namedtuple_fields(animal)
        if i < len(animals) - 1:
            print()  # Add an empty line after each animal except the last one


if __name__ == '__main__':
    pickle_file_path = './tests/data.pkl'

    try:
        # Deserialize the pickle file into a list of Animal namedtuples
        animals = deserialize_pickle_file(pickle_file_path)

        # Display each animal record
        display_animal_records(animals)

    except FileNotFoundError:
        print(f"Error: The file {pickle_file_path} was not found.")
    except pickle.UnpicklingError:
        print("Error: Failed to deserialize the pickle file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
