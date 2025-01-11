# City Repetition Checker 🏙️

## Description 📝

Timur and Ruslan love playing a game of naming cities. However, by the end of the game, they sometimes forget which cities they've already mentioned. This program helps them keep track by checking if a new city has already been named, ensuring they don’t repeat themselves.

## Purpose 🎯

To assist Timur and Ruslan in identifying if a newly named city during their game has already been mentioned, ensuring the game runs smoothly and without confusion.

## How It Works 🔍

1. **Inputs**:
    - The number of cities previously named.
    - A list of city names that have already been mentioned.
    - The name of the new city to check.
2. **Logic**:
    - Check if the new city exists in the list of previously named cities.
    - If the city is already mentioned, return "REPEAT".
    - Otherwise, return "OK".
3. **Output**:
    - The program prints:
        - `"REPEAT"` if the city has already been named.
        - `"OK"` if the city is new.

## Output 📜

The program outputs a message indicating whether the newly named city has already been mentioned.

### Example:

**Input**:

```
4
Paris
Berlin
Moscow
Rome
Berlin
```

**Output**:

```
REPEAT
```

### Explanation:

-   The list of previously named cities is `["Paris", "Berlin", "Moscow", "Rome"]`.
-   The new city to check is `"Berlin"`.
-   Since `"Berlin"` is already in the list, the program outputs `"REPEAT"`.

## Usage 📦

1. Copy the code into a Python file, e.g., `city_checker.py`.
2. Run the script.
3. Provide the following inputs when prompted:
    - Number of previously named cities.
    - List of city names, one per line.
    - The new city to check.
4. The program will output whether the city has been repeated or not.

### Example Run:

```plaintext
Input:
3
London
New York
Tokyo
London

Output:
REPEAT
```

## Conclusion 🚀

This program ensures that Timur and Ruslan can enjoy their game without confusion, making it easier to track cities they’ve already named. Perfect for anyone who loves games that involve naming items while keeping track of repetitions!
