# Group Dogs by Owner 🐾

## Description 📝

This program groups dogs by their owners, creating a dictionary where each key is a tuple containing the owner's first name, last name, and age, and the value is a list of dog names owned by that person. The program handles cases where an owner has multiple dogs and ensures the original order of dog names is preserved.

## Purpose 🎯

The purpose of this program is to organize a list of pets into a dictionary that groups dogs by their owners. This can be useful for managing pet data, finding all pets owned by a specific person, or performing analysis on pet ownership.

## How It Works 🔍

1. **Input**:
    - A list of tuples where each tuple contains the dog’s name, the owner's first name, last name, and age.
2. **Processing**:
    - The function iterates over each tuple, creating a dictionary where the key is a tuple of the owner's information (first name, last name, and age), and the value is a list of dog names.
    - If an owner has multiple dogs, their dogs are added to the list under the same key.
3. **Output**:
    - A dictionary where each key is a tuple representing the owner, and the value is a list of dog names owned by that person.

## Output 📜

The program stores the result in the `result` variable, which is a dictionary that groups dogs by their owners. The dictionary does not need to be printed.

### Example:

**Input**:

```python
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
```

**Output**:

```python
{
    ('Parker', 'Wilson', 50): ['Hatiko'],
    ('Josh', 'King', 25): ['Rusty', 'Balto', 'Barry', 'Lassie'],
    ('John', 'Smith', 28): ['Fido'],
    ('Jake', 'Smirnoff', 18): ['Butch'],
    ('Emma', 'Wright', 18): ['Odi'],
    ('Hannah', 'Taylor', 40): ['Snape'],
    ('Martha', 'Robinson', 73): ['Horry', 'Chase'],
    ('Alex', 'Martinez', 65): ['Giro'],
    ('Simon', 'Nevel', 32): ['Zooma', 'Rocky'],
    ('Martha', 'Williams', 38): ['Ace']
}
```

## Usage 📦

1. Save the code in a Python file, e.g., `group_dogs_by_owner.py`.
2. Define the list of pets with each pet's information.
3. Call the function `group_dogs_by_owner(pets)` to get the result.

### Example Run:

```python
result = group_dogs_by_owner(pets)
```

## Conclusion 🚀

This function groups dogs by their owners, making it easy to see all pets owned by a specific person. It can be used in scenarios where organizing pets by ownership is necessary, such as in databases or pet tracking systems.
