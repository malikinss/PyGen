# Rock, Paper, Scissors Game Program 🪶🪨📄

## Description 📝

This program is designed to simulate a game of rock, paper, scissors between two players, Timur and Ruslan.
The program will determine the winner based on their choices, with the options being "rock", "scissors", or "paper".
It outputs the result as either "Timur", "Ruslan", or "draw", depending on the game outcome.

## Purpose 🎯

The goal of this program is to help Timur and Ruslan fairly decide who will work on the next module of the "Python for Professionals" course.
By playing rock, paper, scissors, the program decides the winner between them based on their choices.

## How It Works 🔍

1. **Input Format**:

    - The first line contains Timur's choice, which can be one of the following: "rock", "scissors", or "paper".
    - The second line contains Ruslan's choice, which also can be one of the following: "rock", "scissors", or "paper".

2. **Logic**:
    - The program compares the two moves and decides the winner:
        - "rock" beats "scissors"
        - "scissors" beats "paper"
        - "paper" beats "rock"
    - If both players choose the same move, it results in a draw.
3. **Example**:

    - **Input**:
        ```
        rock
        scissors
        ```
    - **Output**:
        ```
        Timur
        ```
    - **Explanation**:
        - "rock" beats "scissors", so Timur wins.

4. **Edge Cases**:
    - The program handles all possible valid inputs: "rock", "scissors", or "paper".
    - It also works for tie cases, where both players choose the same move.

## Usage 📦

1. Copy the code into a Python file, e.g., `rock_paper_scissors.py`.
2. Run the script in the terminal:
    ```bash
    python rock_paper_scissors.py
    ```
3. Enter Timur's choice and Ruslan's choice when prompted.
4. The program will output either "Timur", "Ruslan", or "draw" based on the result of the game.

## Conclusion 🚀

This simple and fun game allows Timur and Ruslan to fairly decide who will do the next module of the course using the classic rock-paper-scissors game.
The program efficiently determines the winner and handles all possible outcomes, ensuring a fair decision every time.
