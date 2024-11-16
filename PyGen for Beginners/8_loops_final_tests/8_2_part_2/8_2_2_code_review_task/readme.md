# Code review task 3 🪲

## Description 📝

This program processes a sequence of 8 integers and calculates:

1. The number of integers divisible by 4 in the sequence.
2. The maximum integer divisible by 4.

If no number is divisible by 4, the program outputs `"NO"`.

## Purpose 🎯

The purpose of this program is to:

1. Count how many numbers in the sequence are divisible by 4.
2. Find the maximum number divisible by 4.
3. Handle the case when no number is divisible by 4 by printing `"NO"`.

## How It Works 🔍

-   The program loops through a sequence of 8 integers.
-   It checks each integer to see if it is divisible by 4.
-   If a number is divisible by 4, the program increments the count and updates the maximum number if the current number is larger than the previous maximum.
-   After processing all numbers, it prints the count and the maximum number if there are any numbers divisible by 4; otherwise, it prints `"NO"`.

## Output 📜

-   If numbers divisible by 4 are found, the program prints:
    1. The count of numbers divisible by 4.
    2. The maximum number divisible by 4.
-   If no numbers are divisible by 4, it prints `"NO"`.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect number of iterations:

-   **Original**: `n = 7`
-   The program is supposed to process 8 integers, not 7.
-   **Fix**: Set `n = 8` to iterate 8 times.

### 2. Incorrect condition for checking divisibility by 4:

-   **Original**: `if x // 4 == 0`
-   This condition checks whether the result of integer division by 4 equals 0. It doesn't properly check if `x` is divisible by 4.
-   **Fix**: Use the modulus operator (`x % 4 == 0`) to check if `x` is divisible by 4.

### 3. Incorrect initial value for `maximum`:

-   **Original**: `maximum = 1000`
-   The initial value of `maximum` is too small to ensure that any valid number divisible by 4 can replace it. The absolute values of the numbers can be as large as `10^12`, so this initial value is inadequate.
-   **Fix**: Set `maximum = (-10 ** 6) - 1` to handle all possible inputs, as this value is lower than any valid number that could appear in the input.

### 4. Incorrect comparison to update `maximum`:

-   **Original**: `if x < maximum`
-   The program should update the maximum value when `x` is greater than the current maximum, not when `x` is smaller.
-   **Fix**: Change the comparison to `if x > maximum`.

## Fixed Code 🛠:

```python
n = 8  # Process 8 integers
count = 0
maximum = (-10 ** 6) - 1  # Initialize maximum to a very low value

for i in range(1, n + 1):
    x = int(input())

    if x % 4 == 0:  # Check if the number is divisible by 4
        count += 1

        if x > maximum:  # Update maximum if the current number is greater
            maximum = x

if count > 0:
    print(count)  # Print the count of numbers divisible by 4
    print(maximum)  # Print the maximum number divisible by 4
else:
    print('NO')  # Print "NO" if no numbers are divisible by 4
```

## Explanation of Changes 🧾:

1. **Number of iterations**: Changed the value of `n` to 8 to process 8 integers.
2. **Divisibility check**: Fixed the condition to check divisibility by 4 using the modulus operator (`x % 4 == 0`).
3. **Initial value of `maximum`**: Set a lower initial value for `maximum` that can handle any possible input.
4. **Update of `maximum`**: Fixed the comparison logic to update the maximum value when a larger number divisible by 4 is encountered.

## Conclusion 🚀

This program correctly counts and finds the maximum of numbers divisible by 4 in a sequence of 8 integers.
After fixing the identified issues, it now behaves as expected and handles all edge cases correctly.
