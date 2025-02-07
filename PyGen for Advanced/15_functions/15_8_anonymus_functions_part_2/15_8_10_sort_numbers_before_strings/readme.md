# Sorting Numbers Before Strings in a Mixed List

## Description

This program sorts a **mixed list of numbers and strings**, ensuring:

1. **Numbers appear first**.
2. **All elements are sorted in non-decreasing order**.

## Purpose

-   Demonstrates **sorting mixed data types**.
-   Uses the `sorted()` function with a **custom lambda function**.

## How It Works

1. **Sorting Logic**:

    - Uses `sorted()` with `key=lambda x: (isinstance(x, str), x)`.
    - **Numbers (`False`) are placed before strings (`True`)**.
    - Sorting is applied **naturally within each type**.

2. **Example Input**

    ```
    [ 'beside', 48, 'accelerate', 28, 'beware', 'absorb', 15, 65, 'abate', 76 ]
    ```

3. **Example Output**
    ```
    10 11 12 12 13 13 14 15 19 20 20 26 26 26 28 35 36 37 38 40 40 41 41 46 46 47 48 50 51 60 64 65 65 66 67 70 75 76 76 76 78 80 87 89 94 95 95 98 99 aboard about above abrupt absent absorb abundant abuse abyss abyss accelerate accident accept accessory access adapt abate aboard abolish abound abroad abrupt absent absolute absorb abundant abuse abundant abyss
    ```

## Usage

1. **Provide a list (`mixed_list`)** with numbers and strings.
2. **Call `sort_numbers_before_strings(mixed_list)`**.
3. **Print the sorted result** using `print(*result)`, ensuring space-separated output.

## Conclusion

This approach ensures **clean and structured sorting** for **heterogeneous lists**, making mixed data more manageable.
