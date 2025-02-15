# Progression Type Checker

## Description 📝

This Python program checks if a sequence of integers forms a progression, and if so, determines whether it is an arithmetic progression, geometric progression, or neither.
The program uniquely identifies the type of progression or indicates if it is not a progression.

## Purpose 🎯

The purpose of this program is to analyze a given sequence of integers and determine if it forms a progression (either arithmetic or geometric).
It helps to easily classify sequences for further analysis.

## How It Works 🔍

1. **Function `get_list_of_nums_from_input()`**:

    - Reads the input data, which is a sequence of integers, and returns it as a list.

2. **Function `is_arithmetic_progression(nums)`**:

    - Checks if the sequence of numbers forms an arithmetic progression, where the difference between consecutive terms is constant.

3. **Function `is_geometric_progression(nums)`**:

    - Checks if the sequence of numbers forms a geometric progression, where each term after the first is obtained by multiplying the previous term by a constant ratio.

4. **Function `print_progressions(nums)`**:
    - Determines whether the sequence is an arithmetic progression, a geometric progression, or neither, and prints the corresponding result.

### Example:

For input:

```
2
4
6
8
10
```

The program will output:

```
Arithmetic progression
```

For input:

```
2
4
8
16
32
```

The program will output:

```
Geometric progression
```

## Output 📜

The program will output one of the following:

-   "Arithmetic progression" if the sequence follows an arithmetic progression.
-   "Geometric progression" if the sequence follows a geometric progression.
-   "Not a progression" if the sequence does not follow either progression.

Example output:

```
Arithmetic progression
```

## Usage 📦

1. Save the code in a file named `progression_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script and provide input via standard input.

### Example usage:

```bash
$ python progression_checker.py
2
4
6
8
10
```

The output will be:

```
Arithmetic progression
```

## Conclusion 🚀

This program helps classify a sequence of integers as either an arithmetic progression, geometric progression, or as not being a progression at all. It is a useful tool for analyzing sequences and identifying patterns.
