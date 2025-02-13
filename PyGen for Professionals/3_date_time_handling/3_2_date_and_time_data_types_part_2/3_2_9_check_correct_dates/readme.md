# Date Validity Checker Program

## Description 📝

This program checks the correctness of dates entered by the user. The input dates should be in the format `DD.MM.YYYY`.
The program will validate each date, indicating whether it is correct or incorrect, and at the end, it will display the total number of correct dates.

## Purpose 🎯

The program serves the purpose of validating a sequence of dates entered in a specific format.
It ensures the entered dates are correct by checking if they match the Gregorian calendar.
The program stops when the word "end" is entered.

## How It Works 🔍

1. The program prompts the user to enter dates in the format `DD.MM.YYYY`.
2. For each date:
    - It checks the validity using the `is_correct()` function.
    - It prints "Correct" if the date is valid and "Incorrect" if it is not.
3. The input ends when the user types "end".
4. The program counts the number of valid dates and displays the total count at the end.

## Output 📜

-   For each date:
    -   "Correct" if the date is valid.
    -   "Incorrect" if the date is invalid.
-   At the end, the program will output the number of valid dates.

### Example Usage:

```plaintext
Input:
01.01.2020
29.02.2021
31.04.2020
end

Output:
Correct
Incorrect
Incorrect
1
```

## Usage 📦

1. Enter dates in the format `DD.MM.YYYY`.
2. Type `end` to stop the program.
3. The program will display whether each date is "Correct" or "Incorrect".
4. It will also display the number of correct dates.

## Conclusion 🚀

This program is a simple yet effective tool for checking the validity of dates in a user-friendly format. It can be used for validation tasks in various applications where date correctness is important.
