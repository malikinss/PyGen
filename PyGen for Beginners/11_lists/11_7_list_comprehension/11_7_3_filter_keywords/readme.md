# Filter Keywords by Length

## Description 📝

This Python script filters a list of keywords and returns a new list containing only words that are **at least five characters long**.
The filtering is achieved using **list comprehension** for efficiency and readability.

## Purpose 🎯

-   Demonstrate the use of **list comprehensions** to filter data based on specific conditions.
-   Create a list of Python keywords with lengths greater than or equal to five.
-   Provide a concise and elegant solution to filtering lists.

## How It Works 🔍

1. **Function Definition**:  
   The function `filter_keywords` takes a list of strings as input.
2. **Filtering with List Comprehension**:  
   The function filters out strings shorter than five characters by using `len(i) >= 5` inside the list comprehension.
3. **Execution**:  
   The function is applied to a list of Python keywords, and the filtered list is printed.

### Key Points:

-   **Efficiency**: List comprehensions offer a more efficient way to filter data compared to traditional loops.
-   **Readability**: The one-liner solution makes the code clean and easy to understand.

## Output 📜

The program outputs a list of keywords that have at least five characters.

**Example Output:**

```
['False', 'assert', 'break', 'class', 'continue', 'except', 'finally', 'global', 'import', 'lambda', 'nonlocal', 'raise', 'return', 'while', 'yield']
```

## Usage 📦

1. Copy the code into a file named `filter_keywords.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python filter_keywords.py
    ```
5. The filtered list of keywords will be printed in the terminal.

## Conclusion 🚀

This script highlights the power and simplicity of **list comprehensions** in Python, making it easy to filter data based on specific conditions. Such techniques improve code readability and maintainability, essential for developing efficient Python applications. 🌟
