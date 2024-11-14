# Count Fives in a Sequence of Grades

## Description 📝

This program reads a sequence of student grades (integers from 1 to 5) entered by the user and counts how many times the grade 5 appears.
The sequence ends when a negative number or a number greater than 5 is entered, signaling termination without being counted.

## Purpose 🎯

The program demonstrates sequence processing and counting based on specific conditions.
It is useful for determining the frequency of a particular grade within a controlled range of inputs.

## How It Works 🔍

1. The program initializes a counter, `count_of_fives`, to zero.
2. It prompts the user to enter grades, one at a time.
3. For each grade:
    - If the grade is 5, it increments the counter.
    - If the grade is outside the range of 1 to 5 (inclusive), the program stops accepting input.
4. Finally, it prints the count of the number of fives.

## Output 📜

The output is the total count of the grade 5 within the entered sequence.

### Example

```bash
Input: 4 5 3 5 2 6
Output: Number of fives: 2

```

## Usage 📦

1. Run the script in a Python environment.
2. Enter grades from 1 to 5, one per line.
3. Enter a negative number or a number greater than 5 to end the sequence and see the count of fives.

## Conclusion 🚀

This program effectively counts occurrences of a specific grade with a controlled sequence termination, illustrating basic input handling and counting techniques.
