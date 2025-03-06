# CardDeck Class

## Description 📝

The `CardDeck` class is an iterator that generates a sequence of 52 playing cards.

Each card is represented as a string in the format `<value> <suit>`. The iteration follows the ranking and suit order:

-   **Suits**: spades, clubs, diamonds, hearts.
-   **Ranks**: two, three, ..., king, ace.

The cards are generated in order first by rank (two to ace), and then by suit (spades to hearts).

## Purpose 🎯

This iterator allows you to traverse through a standard deck of 52 playing cards in a well-defined order based on suit and rank.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Defines the suits (`spades`, `clubs`, `diamonds`, `hearts`) and ranks (2 to ace) for the deck.
    - Initializes the indexes (`suit_index` and `rank_index`) to control the iteration through the deck.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the iterator instance (`self`).
    - `__next__()`:
        - Returns the next card in the deck in the format `<rank> of <suit>`.
        - After all cards in a suit are exhausted, moves to the next suit.
        - If all cards have been generated, raises a `StopIteration` exception.

## Output 📜

Example usage:

```python
deck = CardDeck()
for card in deck:
    print(card)
```

**Expected Output** (Partial):

```
2 of spades
3 of spades
4 of spades
...
king of diamonds
ace of diamonds
2 of hearts
...
ace of hearts
```

## Usage 📦

1. Save the class in a file, e.g., `card_deck.py`.
2. Use the following code to iterate over the deck:
    ```python
    deck = CardDeck()
    for card in deck:
        print(card)
    ```
    **Expected Output:**
    ```
    2 of spades
    3 of spades
    ...
    ace of hearts
    ```

## Conclusion 🚀

The `CardDeck` iterator provides a way to generate a full deck of 52 cards in a specific order, adhering to the traditional ranking and suit order.

It is useful for card games and simulations that require generating a standard deck of cards in a consistent manner.
