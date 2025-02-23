# Zoo Animal Count

## Description 📝

This Python program reads a JSON file containing data about the inhabitants of a zoo.
Each animal's name is used as a key in the JSON objects, and the corresponding value represents the number of animals of that species in the zoo.
The program calculates the total number of animals in the zoo by summing up the values of all animals across multiple records.

## Purpose 🎯

The purpose of this program is to calculate and print the total number of animals in the zoo based on data from a JSON file, making it easier to track the population of various species in the zoo.

## How It Works 🔍

1. **Reading the JSON File**: The program reads a JSON file containing a list of dictionaries, where each dictionary represents a record with animal names as keys and their counts as values.
2. **Counting Total Animals**: The program merges all dictionaries into a single collection and sums up the values to get the total number of animals in the zoo.
3. **Output**: The total number of animals is printed to the console.

## Output 📜

The program outputs a single integer: the total number of animals in the zoo.

### Example:

#### Input:

Assume the `zoo.json` file contains the following data:

```json
[
    {
        "Axolotl": 11,
        "Poison Frog": 12,
        "Sonoran Toad": 6,
        "Tiger Salamander": 16
    },
    {
        "African Fish Eagle": 6,
        "Andean Condor": 8,
        "Black Vulture": 8,
        "Bufflehead Duck": 9,
        "Flamingo": 8,
        "Great Horned Owl": 16,
        "Hornbill": 1
    }
]
```

#### Output:

```
Total number of animals in the zoo: 95
```

## Usage 📦

1. The program expects a JSON file with a list of dictionaries, where each dictionary contains animal species as keys and the number of animals as values.
2. The program will read the data from the specified file, calculate the total number of animals, and print the result.

### Example:

```bash
python zoo_animal_count.py
```

#### Input Example:

`zoo.json`:

```json
[
    {
        "Axolotl": 11,
        "Poison Frog": 12,
        "Sonoran Toad": 6,
        "Tiger Salamander": 16
    },
    {
        "African Fish Eagle": 6,
        "Andean Condor": 8,
        "Black Vulture": 8,
        "Bufflehead Duck": 9,
        "Flamingo": 8,
        "Great Horned Owl": 16,
        "Hornbill": 1
    }
]
```

#### Output Example:

```
Total number of animals in the zoo: 95
```

## Conclusion 🚀

This program efficiently calculates the total number of animals in the zoo from a JSON file.
It is useful for quickly assessing the zoo's population and can be easily adapted for different datasets.
