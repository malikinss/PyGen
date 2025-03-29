# Bracket Sequence Validator 🛠️

## Description 📝

This program checks whether a given **bracket sequence** is valid.
A valid sequence means that each opening bracket has a corresponding closing bracket and that brackets are closed in the correct order.
The sequence only consists of the characters `(` and `)`.

## Purpose 🎯

The purpose of this program is to determine if the input string of parentheses follows the rules of a correct bracket sequence, making it useful for tasks like syntax checking or validating expressions.

## How It Works 🔍

1. **Input**:

    - The program takes a string consisting of only `(` and `)` characters as input.

2. **Validation**:

    - It uses a **stack** to track opening brackets.
    - When encountering an opening bracket `(`, it is added to the stack.
    - When encountering a closing bracket `)`, the program checks if it correctly matches the most recent opening bracket by popping from the stack.
    - If the stack is empty after processing all characters, the sequence is valid.

3. **Output**:
    - The program outputs `True` if the sequence is valid, or `False` otherwise.

## Output 📜

### Example Input:

```sh
(())
```

### Example Output:

```sh
True
```

### Example Input:

```sh
())(
```

### Example Output:

```sh
False
```

## Usage 📦

1. Run the script:
    ```sh
    python bracket_validator.py
    ```
2. Input the bracket sequence (e.g., `(())`).
3. The output will be `True` if the sequence is valid or `False` otherwise.

## Conclusion 🚀

This program provides an efficient way to check whether a bracket sequence is correct, making it valuable for parsing and validating expressions in programming, compilers, or data validation tasks.
