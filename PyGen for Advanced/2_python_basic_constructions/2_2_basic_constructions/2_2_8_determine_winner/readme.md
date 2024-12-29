# Rock, Paper, Scissors, Lizard, Spock Game Program 🪨📄🦎✂️🚀

## Description 📝

This program simulates an extended version of the classic Rock, Paper, Scissors game, called Rock, Paper, Scissors, Lizard, Spock.
Timur and Ruslan use this game to decide who will work on the next module of their "Python for Professionals" course.
The program determines the winner based on their choices and applies the extended rules of the game, which include five different elements: Stone, Scissors, Paper, Lizard, and Spock.

## Purpose 🎯

The goal of this program is to help Timur and Ruslan determine who will be responsible for the next course module by playing Rock, Paper, Scissors, Lizard, Spock.
The extended rules of the game make the decision-making more complicated and fairer.

## How It Works 🔍

1. **Input Format**:

    - The first line contains Timur's choice, which can be one of the following: "Stone", "Lizard", "Spock", "Scissors", or "Paper".
    - The second line contains Ruslan's choice, which also can be one of the following: "Stone", "Lizard", "Spock", "Scissors", or "Paper".

2. **Rules**:

    - Scissors cut Paper
    - Paper wraps Rock
    - Rock crushes Lizard
    - Lizard poisons Spock
    - Spock breaks Scissors
    - Scissors decapitate Lizard
    - Lizard eats Paper
    - Paper disproves Spock
    - Spock vaporizes Rock
    - Rock dulls Scissors

3. **Example**:

    - **Input**:
        ```
        Stone
        Scissors
        ```
    - **Output**:
        ```
        Timur
        ```
    - **Explanation**:
        - "Stone" crushes "Scissors", so Timur wins.

4. **Edge Cases**:
    - The program handles all possible valid moves: "Stone", "Lizard", "Spock", "Scissors", and "Paper".
    - It works for tie cases, where both players choose the same move.

## Usage 📦

1. Copy the code into a Python file, e.g., `rock_paper_scissors_lizard_spock.py`.
2. Run the script in the terminal:
    ```bash
    python rock_paper_scissors_lizard_spock.py
    ```
3. Enter Timur's choice and Ruslan's choice when prompted.
4. The program will output either "Timur", "Ruslan", or "Draw" based on the result of the game.

## Conclusion 🚀

This extended version of Rock, Paper, Scissors adds more complexity and fairness to the game, allowing Timur and Ruslan to decide who will work on the next course module.
The program efficiently determines the winner based on the extended rules, ensuring a fun and fair game each time.
