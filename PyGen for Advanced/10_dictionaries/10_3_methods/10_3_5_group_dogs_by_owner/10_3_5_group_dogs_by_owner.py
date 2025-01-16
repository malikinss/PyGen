"""
TODO:
    You have a list of pets containing information about dogs and their owners.

    Each element of the list is a tuple of the form (dog name, owner first
    name, owner last name, owner age).

    Complete the code below so that the variable result stores a dictionary
    that lists the dogs for each owner.

    The key of the dictionary should be a tuple of (owner first name, owner
    last name, owner age), and the value should be a list of dog names
    (preserving the original order).

NOTE:
    Remember: tuples are immutable, so they can be keys of a dictionary.

    Note that some owners have multiple dogs.

    There is no need to print the contents of the dictionary result.
"""
from typing import List, Dict, Tuple


def group_dogs_by_owner(
    pets: List[Tuple[str, str, str, int]]
) -> Dict[Tuple[str, str, int], List[str]]:
    """
    Groups dogs by their owners.

    Args:
        pets (List[Tuple[str, str, str, int]]): A list of tuples containing
        dog information.
        Each tuple is of the form (dog name, owner first name, owner last name,
        owner age).

    Returns:
        Dict[Tuple[str, str, int], List[str]]: A dictionary where the key
        is a tuple representing the owner's information (first name, last name,
        age) and the value is a list of dog names
        wned by that person.
    """
    result: Dict = {}

    for dog_name, first_name, last_name, age in pets:
        owner = (first_name, last_name, age)
        if owner not in result:
            result[owner] = []
        result[owner].append(dog_name)

    return result


# Example usage
pets = [
    ('Hatiko', 'Parker', 'Wilson', 50),
    ('Rusty', 'Josh', 'King', 25),
    ('Fido', 'John', 'Smith', 28),
    ('Butch', 'Jake', 'Smirnoff', 18),
    ('Odi', 'Emma', 'Wright', 18),
    ('Balto', 'Josh', 'King', 25),
    ('Barry', 'Josh', 'King', 25),
    ('Snape', 'Hannah', 'Taylor', 40),
    ('Horry', 'Martha', 'Robinson', 73),
    ('Giro', 'Alex', 'Martinez', 65),
    ('Zooma', 'Simon', 'Nevel', 32),
    ('Lassie', 'Josh', 'King', 25),
    ('Chase', 'Martha', 'Robinson', 73),
    ('Ace', 'Martha', 'Williams', 38),
    ('Rocky', 'Simon', 'Nevel', 32)
]

result = group_dogs_by_owner(pets)
