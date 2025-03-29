# Pokemon Card Duplicates Counter 🃏

## Description 📝

This program helps Arthur determine how many duplicate Pokemon cards he has in his collection.
By keeping only one card of each type, the program calculates how many additional cards are duplicates and can be sold.

## Purpose 🎯

The goal is to count the number of duplicate Pokemon cards in the collection.
Arthur can sell the duplicates while retaining one of each unique card type.

## How It Works 🔍

1. **Input**:
    - The program reads an arbitrary number of lines representing Pokemon card names.
2. **Processing**:
    - The program uses the `set()` data structure to identify unique cards in the collection.
    - It compares the total number of cards with the number of unique cards to calculate how many duplicates exist.
3. **Output**:
    - The program outputs a single number: the count of duplicate cards that can be sold.

## Output 📜

### Example Input:

```sh
Pikachu
Charmander
Pikachu
Bulbasaur
Charmander
```

### Example Output:

```sh
2
```

(Arthur can sell 2 duplicate cards: one `Pikachu` and one `Charmander`.)

## Usage 📦

1. Run the script:
    ```sh
    python pokemon_duplicates.py
    ```
2. Input Pokemon card names, one per line.
3. The program will output the number of duplicate cards.

## Complexity Analysis ⏳

-   **Time Complexity**: `O(n)` where `n` is the number of input lines. This is because converting the list to a set and comparing lengths both operate in linear time.
-   **Space Complexity**: `O(n)` for storing the list of card names and the set of unique cards.

## Conclusion 🚀

This program provides an efficient way to determine how many duplicate Pokemon cards Arthur can sell, helping him organize his collection while making some profit.
