# Find the Youngest Living Swedish Male

## Description 📝

This script processes a list of `Person` named tuples to find and print the first and last name of the youngest living Swedish male.

## Purpose 🎯

The function efficiently filters and selects the youngest living Swedish male using generator pipelines, making it both memory-efficient and performant.

## How It Works 🔍

1. **Filtering**: A generator filters only those who are:
    - Swedish (`nationality == 'Swedish'`)
    - Male (`sex == 'male'`)
    - Alive (`death == 0`)
2. **Finding the Youngest**: The `max()` function is applied to the filtered generator using `attrgetter('birth')` to find the person with the most recent birth year.

## Output 📜

Example output:

```shell
Jon Bale
```

## Usage 📦

1. Save the function in a Python file, e.g., `youngest_swedish_male.py`.
2. Run the script in a terminal or within a Python environment:
    ```python
    from youngest_swedish_male import youngest_living_swedish_man, persons
    print(youngest_living_swedish_man(persons))
    ```
3. The output will be the full name of the youngest living Swedish male.

## Conclusion 🚀

This function demonstrates the power of generator pipelines in efficiently processing and filtering data, ensuring optimal performance with minimal memory overhead.
