# Memory Test Checker 🧠

## Description 📝

The BEEGEEK online school director assesses new candidates' memory skills alongside their professional qualities. Candidates are briefly shown a set of numbers and are later required to recall them without omitting or adding any numbers. The order does not matter, but the accuracy does. This program evaluates whether the candidate successfully passed the memory test by comparing the given numbers with the numbers recalled by the candidate.

## Purpose 🎯

To determine if a candidate has accurately recalled all the numbers shown during the memory test without any omissions or additions.

## How It Works 🔍

1. **Inputs**:
    - A set of numbers (`given_numbers`) shown to the candidate.
    - A set of numbers (`candidate_numbers`) recalled by the candidate.
2. **Logic**:
    - Compare the two sets for exact equality.
    - If they match, the candidate passes the test.
    - If there is any discrepancy, the candidate fails.
3. **Outputs**:
    - `"YES"` if the candidate passes the test.
    - `"NO"` if the candidate fails.

## Output 📜

The program outputs:

-   `"YES"` if the candidate recalls the exact set of numbers.
-   `"NO"` if the candidate's recalled numbers are incorrect.

### Example:

**Input**:

```
1 2 3 4 5
5 4 3 2 1
```

**Output**:

```
YES
```

### Explanation:

-   **Given numbers**: `{1, 2, 3, 4, 5}`
-   **Candidate's numbers**: `{1, 2, 3, 4, 5}`
-   Both sets match, so the candidate passes.

## Usage 📦

1. Save the code in a Python file, e.g., `memory_test_checker.py`.
2. Run the script.
3. Provide inputs:
    - A space-separated list of numbers shown to the candidate.
    - A space-separated list of numbers recalled by the candidate.
4. View the result:
    - `"YES"` if the candidate recalls correctly.
    - `"NO"` if the candidate fails.

### Example Run:

```plaintext
Input:
10 20 30
20 10 30

Output:
YES
```

```plaintext
Input:
1 2 3 4
1 2 3

Output:
NO
```

## Conclusion 🚀

This program is a quick and efficient way to evaluate memory retention skills, ensuring fair and accurate results during tests. It's ideal for educational institutions and scenarios where memory assessment is a priority.
