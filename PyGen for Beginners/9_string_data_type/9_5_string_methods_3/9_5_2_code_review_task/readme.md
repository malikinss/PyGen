# Code Review Task 🪲

## Description 📝

This task updates a Python script to output a formatted string using **f-string formatting**.
The program dynamically inserts variables into the text to produce:  
`"In 2010, someone paid 10K Bitcoin for two pizzas."`

## Purpose 🎯

The purpose of this program is to:

1. Demonstrate the use of **f-strings** for clean and efficient string formatting.
2. Dynamically insert variables into a string for readability and simplicity.
3. Provide an alternative to traditional formatting methods like `format()`.

## How It Works 🔍

-   The program defines the variables `year`, `amount`, and `currency` with specific values.
-   An **f-string** is used to construct the string by embedding the variables directly within curly braces `{}`.
-   The formatted string is printed, showcasing the simplicity and readability of **f-strings**.

## Output 📜

-   The program outputs:  
    `"In 2010, someone paid 10K Bitcoin for two pizzas."`

## Identified Errors in the Original Code 🕵🏾:

1. **Missing Variable Integration**:

    - Original: `print('In {}, someone paid {} {} for two pizzas.')`
    - Issue: The string does not include any variable references, resulting in unformatted output.
    - Fix: Use **f-strings** to integrate the variables into the string.

2. **Static Formatting**:
    - The original code lacks dynamic formatting for the text output.
    - Fix: Replace the static string with an **f-string** for clarity and efficiency.

## Fixed Code 🛠:

```python
# Define the variables
year = 2010
amount = '10K'
currency = 'Bitcoin'

# Use an f-string for formatting
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
# Outputs: 'In 2010, someone paid 10K Bitcoin for two pizzas.'
```

## Explanation of Changes 🧾:

1. **Defined variables**: `year`, `amount`, and `currency` are clearly defined with specific values.
2. **Implemented f-string formatting**: Used `f'...'` to dynamically insert the variables into the string for concise and readable code.
3. **Simplified syntax**: Leveraged f-strings to reduce complexity compared to traditional formatting methods.

## Conclusion 🚀

This task highlights the use of f-strings for dynamic and efficient string formatting.
By addressing the issues in the original code, the script now outputs the desired text accurately and elegantly.
