# Program to Generate Random Name Pairs 🎲👤

## Description 📝

This program reads two text files, **"first_names.txt"** and **"last_names.txt"**, and generates 3 random pairs of first names and last names.
It outputs each randomly generated name pair on a separate line.

## Purpose 🎯

To combine random first and last names from two separate lists and output them as full names.

## How It Works 🔍

1. **Reading Files (`get_data_from_file`)**:

    - The program reads the content of the files **"first_names.txt"** and **"last_names.txt"**. Each file contains a list of first names and last names, respectively. The content is stored as a list of strings (one for each line).

2. **Generating Random Name Pair (`generate_random_person`)**:

    - Using the `random.choice()` function, the program randomly selects one first name and one last name from their respective lists and combines them into a full name.

3. **Generating Multiple Name Pairs (`generate_random_persons`)**:

    - The program generates the required number of random full names (in this case, 3) by repeatedly calling the `generate_random_person` function.

4. **Output**:
    - Each randomly generated full name is printed on a new line.

## Example Usage:

**File 1 (`first_names.txt`):**

```
John
Alice
Michael
```

**File 2 (`last_names.txt`):**

```
Smith
Johnson
Brown
```

**Program Output:**

```python
John Johnson
Alice Smith
Michael Brown
```

## Conclusion 🚀

This program effectively generates and outputs random combinations of first and last names, which could be useful for various scenarios such as creating user profiles, mock data, or simply for fun!
