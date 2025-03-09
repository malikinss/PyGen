# `card_deck` Generator

## Description 📝

The `card_deck` function is a generator that yields playing cards excluding the specified suit.
Each card is represented as a string in the format `<rank> <suit>`.
The order of the cards respects the predefined suit and rank hierarchies.

## Purpose 🎯

This generator is designed to simulate a deck of cards without one of the four suits, generating cards in the correct order by suit and rank.
It is useful for creating custom card games or card-related simulations.

## How It Works 🔍

-   The function takes a suit to exclude (either `spades`, `clubs`, `diamonds`, or `hearts`).
-   The function then loops through the suits and ranks of playing cards.
-   It yields the card in the format `<rank> <suit>`, excluding the specified suit.
-   The seniority of the suits and ranks is followed in ascending order.

## Output 📜

Example usage:

```python
gen = card_deck('spades')

# Print cards excluding spades
for card in gen:
    print(card)
    if card == "ace hearts":  # Example to stop after hearts suit
        break
```

**Output:**

```
2 clubs
3 clubs
4 clubs
5 clubs
6 clubs
7 clubs
8 clubs
9 clubs
10 clubs
jack clubs
queen clubs
king clubs
ace clubs
2 diamonds
3 diamonds
4 diamonds
5 diamonds
6 diamonds
7 diamonds
8 diamonds
9 diamonds
10 diamonds
jack diamonds
queen diamonds
king diamonds
ace diamonds
2 hearts
3 hearts
4 hearts
5 hearts
6 hearts
7 hearts
8 hearts
9 hearts
10 hearts
jack hearts
queen hearts
king hearts
ace hearts
```

## Usage 📦

1. **Create a deck excluding a suit**:

    ```python
    gen = card_deck('hearts')
    for card in gen:
        print(card)
        if card == "ace diamonds":  # Stop after diamonds suit
            break
    ```

2. **List all cards excluding clubs**:
    ```python
    gen = card_deck('clubs')
    for card in gen:
        print(card)
    ```

## Conclusion 🚀

The `card_deck` generator efficiently produces a deck of cards while excluding the specified suit.
It respects the predefined suit and rank order, making it suitable for card games or simulations requiring custom decks.
