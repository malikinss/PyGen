# Card and Deck Class Implementation

## Description 📝

The provided code implements the `Card` and `Deck` classes to represent a playing card and a standard deck of 52 playing cards, respectively.
The `Card` class stores a suit and rank, with a string representation of `<suit><rank>`.
The `Deck` class initializes a full deck ordered by suit and rank, supports shuffling (only when full) and dealing the last card, and provides a string representation of the remaining card count.

## Purpose 🎯

Intended for card game simulations, such as poker or blackjack, or educational examples of object-oriented programming, list manipulation, and exception handling in Python.

## How It Works 🔍

-   **Card Class**:
    -   **Initialization (`__init__`)**:
        -   Takes `suit` (one of ♣, ♢, ♡, ♠) and `rank` (one of 2, 3, ..., 10, J, Q, K, A).
        -   Stores them as `self.suit` and `self.rank`.
    -   **String Representation (`__str__`)**:
        -   Returns a string in the format `<suit><rank>`, e.g., `♠A`.
-   **Deck Class**:
    -   **Class Attributes**:
        -   `_SUITS = "♣♢♡♠"`: Defines suits in ascending order.
        -   `_RANKS = (*map(str, range(2, 11)), "J", "Q", "K", "A")`: Defines ranks in ascending order.
    -   **Initialization (`__init__`)**:
        -   Takes no arguments.
        -   Creates `self._deck` as a list of 52 `Card` instances, ordered by suit (♣, ♢, ♡, ♠) then rank (2 to A).
    -   **Methods**:
        -   `shuffle()`:
            -   Checks if `self._deck` has 52 cards.
            -   Raises `ValueError` with "You can only shuffle a full deck" if not full.
            -   Shuffles `self._deck` using `random.shuffle`.
        -   `deal()`:
            -   Checks if `self._deck` is non-empty.
            -   Raises `ValueError` with "All cards have been played" if empty.
            -   Removes and returns the last card using `pop`.
    -   **String Representation (`__str__`)**:
        -   Returns a string in the format `Cards in the deck: <number>`, e.g., `Cards in the deck: 52`.
-   **Behavior**:
    -   `Card` represents a single card with suit and rank.
    -   `Deck` manages a list of cards, enforcing full-deck shuffling and dealing from the end.
    -   No validation is performed, as inputs are guaranteed valid.

## Verification ✅

Implementation satisfies requirements:

-   **Card Initialization**:
    -   `Card("♠", "A")` creates a card with `suit="♠"`, `rank="A"`.
    -   `Card("♣", "2")` creates a card with `suit="♣"`, `rank="2"`.
-   **Card String Representation**:
    -   `str(Card("♠", "A"))` → `♠A`.
    -   `str(Card("♣", "10"))` → `♣10`.
-   **Deck Initialization**:
    -   `Deck()` creates a deck with 52 cards, ordered as:
        -   ♣2, ♣3, ..., ♣A, ♢2, ..., ♢A, ♡2, ..., ♡A, ♠2, ..., ♠A.
-   **Deck Methods**:
    -   `deck = Deck(); deck.deal()` → Returns `♠A` (last card), deck has 51 cards.
    -   `deck.shuffle()` shuffles 52 cards randomly.
    -   After dealing all 52 cards, `deck.deal()` raises `ValueError: All cards have been played`.
    -   After dealing one card, `deck.shuffle()` raises `ValueError: You can only shuffle a full deck`.
-   **Deck String Representation**:
    -   `str(Deck())` → `Cards in the deck: 52`.
    -   After one deal: `Cards in the deck: 51`.
    -   After all deals: `Cards in the deck: 0`.
-   **Order**:
    -   Suits: ♣ < ♢ < ♡ < ♠.
    -   Ranks: 2 < 3 < ... < 10 < J < Q < K < A.
    -   Initial deck follows this order.
-   **Correctness**:
    -   `Card` formats correctly.
    -   `Deck` initializes, shuffles, and deals as specified.
    -   Exceptions raised correctly for invalid operations.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `Card` stores and formats suit and rank as specified.
    -   `Deck` initializes cards in correct suit-then-rank order.
    -   `shuffle` and `deal` enforce constraints with appropriate exceptions.
    -   String representations match requirements exactly.
-   **Performance**:
    -   **Card**:
        -   Initialization: O(1).
        -   `__str__`: O(1).
    -   **Deck**:
        -   Initialization: O(1) for creating 52 cards.
        -   `shuffle`: O(n) for `random.shuffle` (n=52).
        -   `deal`: O(1) for `pop`.
        -   `__str__`: O(1).
    -   Efficient for all operations.
-   **Design**:
    -   Simple and focused implementation with minimal attributes.
    -   List storage for `Deck` is efficient for shuffling and dealing.
    -   Class-level `_SUITS` and `_RANKS` ensure consistent order.
    -   Type hints (`str`, `Card`) clarify inputs and outputs.
    -   No inheritance needed, as `Card` and `Deck` are distinct.
-   **Alternatives**:
    -   Storing cards as tuples in `Deck` would duplicate `Card`’s logic.
    -   Custom shuffle implementation is unnecessary given `random.shuffle`.
-   **Extensibility**:
    -   Easily extended with methods (e.g., deal multiple cards, check card presence).
    -   Could add validation or card comparison if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create a deck
deck = Deck()
print(deck)  # Cards in the deck: 52

# Deal a card
card = deck.deal()
print(card)  # ♠A
print(deck)  # Cards in the deck: 51

# Shuffle full deck
deck = Deck()
deck.shuffle()
print(deck)  # Cards in the deck: 52

# Deal all cards
for _ in range(52):
    deck.deal()
print(deck)  # Cards in the deck: 0

# Test exceptions
try:
    deck.deal()
except ValueError as e:
    print(e)  # All cards have been played

deck = Deck()
deck.deal()
try:
    deck.shuffle()
except ValueError as e:
    print(e)  # You can only shuffle a full deck
```

## Conclusion 🚀

The `Card` and `Deck` implementation is precise, providing correct representations and functionality for playing cards and a 52-card deck.
The design is simple, efficient, and extensible, with proper ordering and exception handling.
It’s ideal for card game simulations or teaching object-oriented concepts, fully compliant with the task’s requirements.
