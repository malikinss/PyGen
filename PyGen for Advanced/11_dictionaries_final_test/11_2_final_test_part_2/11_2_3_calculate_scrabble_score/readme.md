# Scrabble Score Calculator 📝

## Description 📝

This program calculates the total Scrabble score for a given word.
Each letter in the word has a specific point value, and the total score is the sum of the points of each letter.

## Purpose 🎯

The purpose of this program is to calculate the total value of a word in Scrabble based on the individual point values assigned to each letter.

## How It Works 🔍

1. **Input**:
    - The program accepts a single word as input.
2. **Processing**:
    - The program uses predefined letter-to-score mappings to calculate the total score of the word.
3. **Output**:
    - The program returns the total score, which is the sum of the points for each letter in the word.

## Output 📜

The output is a single integer representing the total score of the word in Scrabble.

### Example Input/Output:

**Input**:

```
Enter a word: Scrabble
```

**Output**:

```
14
```

### Explanation:

-   S = 1, C = 3, R = 1, A = 1, B = 3, B = 3, L = 1, E = 1
-   Total: 1 + 3 + 1 + 1 + 3 + 3 + 1 + 1 = 14

## Usage 📦

1. Copy the code into a Python file (e.g., `scrabble_score_calculator.py`).
2. Run the program and input a word when prompted.
3. The program will return the total Scrabble score for that word.

### Example Run:

```python
# Sample run
given_word = "Scrabble"
word_score = calculate_scrabble_score(given_word)
print(word_score)
```

**Output**:

```python
14
```

## Conclusion 🚀

This program provides a quick way to calculate the Scrabble score of any word based on the official letter values.
It's a fun tool to use in games or when studying letter values for Scrabble strategy.
