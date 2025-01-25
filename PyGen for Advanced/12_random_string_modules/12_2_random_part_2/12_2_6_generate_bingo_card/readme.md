# Bingo Card Generator 🎲

## Description 📝

This program generates a random Bingo card for the "Super Bingo" lotto game.
The card consists of 25 cells with unique numbers between 1 and 75, and the center cell is marked as empty (0).
The program ensures that all numbers are unique and formats the card for display.

## Purpose 🎯

The program simulates a Bingo card for use in online Bingo games or for fun, educational activities.
It ensures the correct number of cells, uniqueness of numbers, and proper formatting.

## How It Works 🔍

1. **Card Generation**:
    - The program generates 24 unique random numbers between 1 and 75.
    - The center cell of the card is automatically set to 0.
2. **Card Display**:

    - The numbers are displayed in a 5x5 grid format.
    - Each number is printed with a width of 3 characters for clarity.

3. **Output**:
    - The Bingo card is printed in a human-readable format, with each row of 5 numbers separated by spaces.

## Output 📜

The output will be a 5x5 Bingo card where each number is separated by a space, and the center cell is empty.

### Example Output:

```
  1  16  31  46  61
 10  30  42  47  68
  3  18   0  48  63
  9  19  34  49  70
  5  20  35  50  65
```

## Usage 📦

1. Copy the code into a Python file (e.g., `bingo_card_generator.py`).
2. Run the script.
3. The program will output a randomly generated Bingo card.

### Example Run:

```python
card = generate_bingo_card()
print_bingo_card(card)
```

## Conclusion 🚀

This program provides a simple way to generate and display a Bingo card for games, lotto activities, or educational purposes.
The center cell is automatically empty, and all other cells contain unique random numbers.
