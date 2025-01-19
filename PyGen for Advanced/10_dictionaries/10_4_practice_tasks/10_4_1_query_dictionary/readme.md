# Developer Dictionary 📝

## Description 📝

This program creates and queries a small dictionary of programming slang expressions. It allows users to input terms and their definitions, storing them in a dictionary for future reference. Users can then query the dictionary to retrieve definitions of the terms.

## Purpose 🎯

The program helps programmers organize and reference their growing lexicon of slang and technical jargon. It systematizes terms and ensures quick access to their definitions.

## How It Works 🔍

1. **Input Dictionary**:
    - The user specifies the number of terms they want to add to the dictionary.
    - For each term, the user provides the term and its definition in the format `term: definition`.
    - The program processes these inputs, storing them in a dictionary.
2. **Query Dictionary**:
    - The user specifies how many terms they want to query.
    - For each query, the user inputs a term, and the program retrieves and prints its definition. If the term is not found, it prints "Not Found."

## Output 📜

The program outputs definitions for queried terms or "Not Found" if a term is not in the dictionary.

### Example Input/Output:

**Input**:

```text
3
DRY: Don't Repeat Yourself
KISS: Keep It Simple, Stupid
YAGNI: You Aren't Gonna Need It
2
KISS
SOLID
```

**Output**:

```text
Keep It Simple, Stupid
Not Found
```

## Usage 📦

1. Copy the code into a Python file, e.g., `developer_dictionary.py`.
2. Run the program.
3. Follow the prompts to:
    - Input the dictionary size and terms in the format `term: definition`.
    - Input the number of queries and the terms to look up.

### Example Run:

```python
# Adding terms
Enter dictionary size: 3
DRY: Don't Repeat Yourself
KISS: Keep It Simple, Stupid
YAGNI: You Aren't Gonna Need It

# Querying terms
Enter query count: 2
KISS
Output: Keep It Simple, Stupid
SOLID
Output: Not Found
```

## Conclusion 🚀

This program is a handy tool for developers to create and maintain a personal dictionary of slang and technical terms. It ensures easy access to definitions and supports efficient knowledge management.
