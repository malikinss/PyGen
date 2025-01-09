# Same Digits Checker Program 📝

## Description 📝

This program checks if two given numbers contain exactly the same digits, regardless of their order or frequency.

## Purpose 🎯

To determine whether the digits used in two numbers are identical.
This functionality can be useful in situations where you need to compare numerical compositions, such as in number theory or data validation tasks.

## How It Works 🔍

1. **Input**:
    - The program accepts two numbers as input in string format.
2. **Logic**:
    - Each number is converted into a set of its digits.
    - The program checks if the two sets are equal:
        - If the sets are identical, it means both numbers contain the same digits.
3. **Output**:
    - The program outputs "YES" if the numbers contain the same digits, and "NO" otherwise.

### Example:

**Input**:

```
12345
54321
```

**Output**:

```
YES
```

-   Both numbers contain the same digits `{1, 2, 3, 4, 5}`.

**Input**:

```
12345
12346
```

**Output**:

```
NO
```

-   The numbers have different sets of digits (`5` is missing in the second number, `6` is missing in the first).

## Output 📜

-   "YES" if the two numbers contain the same digits.
-   "NO" if the digits differ.

## Usage 📦

1. Run the program.
2. Input the first number.
3. Input the second number.
4. The program will output whether the two numbers contain the same digits.

## Conclusion 🚀

This program provides a simple and efficient way to check if two numbers are composed of the same digits, helping in scenarios where numerical structure comparison is needed.
