# Count Terms Until Keywords

## Description 📝

This program reads a sequence of words from user input and counts the number of words entered until a specific keyword is encountered.
The program stops counting when one of the keywords `"stop"`, `"enough"`, or `"sufficiently"` is entered.
These keywords act as termination signals and are not included in the count.

## Purpose 🎯

The program demonstrates how to use a loop with multiple exit conditions to count entries up to specific keywords, which act as sequence terminators.

## How It Works 🔍

1. The program enters a loop to read words continuously from the user.
2. It increments a counter for each word entered.
3. When the user enters any of the keywords `"stop"`, `"enough"`, or `"sufficiently"`, the loop terminates.
4. The program then outputs the total count of words entered before any keyword.

## Output 📜

The output is a single integer representing the total number of words entered before encountering a keyword.

### Example 1

```bash
Input: apple banana orange stop
Output: 3

```

### Example 2

```bash
Input: one two three four enough
Output: 4

```

## Usage 📦

1. Run the script in a Python environment.
2. Enter words one by one.
3. To stop and view the count, enter `"stop"`, `"enough"`, or `"sufficiently"`.
4. The program will output the total number of words entered before any of these keywords.

## Conclusion 🚀

This program efficiently counts terms in a sequence until a keyword is encountered, demonstrating the use of condition-controlled loops with customizable termination keywords.
