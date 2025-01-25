# Dice Throw Simulation Program 🎲

## Description 📝

This program simulates rolling a 6-sided dice multiple times using Python's `random` module.
Each result represents the number displayed on the top face of the dice.

## Purpose 🎯

The program is designed to demonstrate randomness in dice rolls, which can be useful for games, probability studies, or testing random number generators.

## How It Works 🔍

1. **Input**:

    - The program asks the user to input the number of dice rolls (attempts).

2. **Processing**:

    - For each roll:
        - A random number between `1` and `6` is generated using `random.randint(1, 6)`.
        - The result is stored in a list.
    - The program simulates the number of dice throws specified by the user.

3. **Output**:
    - The results of all dice rolls are displayed, one result per line.

## Output 📜

The output consists of the results of the dice rolls, displayed in order.

### Example Input/Output:

**Input**:

```
Enter the number of dice throw attempts: 5
```

**Output**:

```
4
2
6
1
3
```

### Explanation:

-   The user requested 5 dice rolls.
-   The program randomly generated the outcomes of the rolls.
-   Each roll result is displayed on a new line.

## Usage 📦

1. Copy the code into a Python file (e.g., `dice_simulation.py`).
2. Run the script and provide the number of dice roll attempts when prompted.
3. View the results of the rolls printed one by one.

### Example Run:

```python
# Input:
Enter the number of dice throw attempts: 3

# Output:
2
5
4
```

## Conclusion 🚀

This program showcases a simple simulation of rolling a dice using Python. It’s a fun and practical way to understand random number generation and can serve as a foundation for more advanced dice-based applications or games.
