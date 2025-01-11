# Homework Completion Calculator 📝

## Description 📝

This program helps a teacher determine how many students in a class have completed their homework, considering various reasons for not submitting it. Students may have missed homework due to:

-   Their homework being eaten by a dog.
-   A power outage at their home.
-   Both of the above misfortunes.

The program calculates the number of students who successfully submitted their homework based on the provided inputs.

## Purpose 🎯

To efficiently calculate the number of students who completed their homework by accounting for overlapping reasons that caused homework submission issues.

## How It Works 🔍

1. **Inputs**:
    - `n`: Total number of students in the class.
    - `m`: Number of students whose homework was eaten by a dog.
    - `k`: Number of students who had their power cut off.
    - `p`: Number of students who suffered from both misfortunes.
2. **Logic**:
    - The total number of students who couldn't complete their homework is calculated as:
      \[
      \text{Total missed} = (m - p) + k
      \]
    - Subtracting the total missed from `n` gives the number of students who completed their homework:
      \[
      \text{Completed} = n - ((m - p) + k)
      \]
3. **Output**: Prints the number of students who completed their homework.

## Output 📜

The program will output the number of students who successfully completed their homework.

### Example:

**Inputs**:

```
n = 30
m = 5
k = 4
p = 2
```

**Output**:

```
23
```

## Usage 📦

1. Copy the code into a Python file, e.g., `homework_completion.py`.
2. Run the script and provide the following inputs when prompted:
    - Total number of students (`n`).
    - Students affected by dog-eaten homework (`m`).
    - Students affected by power cuts (`k`).
    - Students affected by both misfortunes (`p`).
3. The program will print the number of students who completed their homework.

## Conclusion 🚀

This program provides a quick and accurate way to calculate the number of students who have completed their homework, taking into account overlapping reasons for missing it. It's a useful tool for teachers handling large classes and complex scenarios.
