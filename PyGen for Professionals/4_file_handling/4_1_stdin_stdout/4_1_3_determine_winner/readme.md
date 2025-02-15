# Sock Game - Determine Winner

## Description 📝

This Python program simulates a game between two players, Anri and Dima, who take turns drawing an arbitrary number of socks from a box.
The game ends after a series of moves.
The player who made the last move wins if they drew an even number of socks, while the other player loses.
Anri always makes the first move.

## Purpose 🎯

The program determines the winner of the game by evaluating the number of socks drawn in the final move.
It helps in determining whether the final move is a winning or losing move for the player who made it.

## How It Works 🔍

1. **Function `get_next_player(moves)`**:
    - Determines which player will make the next move based on the list of previous moves.
2. **Function `get_last_player(moves)`**:

    - Determines which player made the last move based on the list of previous moves. Anri makes the first move, and players alternate turns.

3. **Function `is_win(move)`**:

    - Checks if the last move is a winning move (even number of socks). If the move is even, the player wins; otherwise, they lose.

4. **Function `get_moves_values()`**:

    - Reads the moves made during the game and returns them as a list of integers (the number of socks drawn in each move).

5. **Function `determine_winner()`**:
    - Determines and prints the winner based on the last move. If the last move is even, the player who made it wins. If the last move is odd, the opponent wins.

### Example:

For input:

```
3
2
1
```

The program will output:

```
DIMA
```

In this case, Anri drew 3 socks (odd, so they lost), and Dima drew 2 socks (even, so they win).

## Output 📜

The program outputs the name of the winner based on the rules of the game.

Example output:

```
DIMA
```

## Usage 📦

1. Save the code in a file named `sock_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script.

### Example usage:

```bash
$ python sock_game.py
3
2
1
```

The output will be:

```
DIMA
```

## Conclusion 🚀

This program helps to simulate a game where two players take turns drawing socks from a box, and the winner is determined based on the number of socks drawn in the final move. It provides an easy and efficient way to determine the game's outcome.
