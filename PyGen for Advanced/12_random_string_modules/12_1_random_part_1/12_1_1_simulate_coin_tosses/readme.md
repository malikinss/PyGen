# Coin Toss Simulation Program 🪙

## Description 📝

This program simulates tossing a coin a specified number of times using Python's `random` module. It outputs the result of each toss as either "Heads" or "Tails".

## Purpose 🎯

The purpose of this program is to demonstrate the use of randomness in simulating real-world events like coin tosses. It can also be a fun way to experiment with probability and randomness.

## How It Works 🔍

1. **Input**:
    - The program prompts the user to input the number of coin toss attempts.
2. **Processing**:

    - Each toss is simulated using the `random.randint()` function:
        - A random number (`1` or `2`) is generated.
        - If the number is `1`, the result is "Heads".
        - If the number is `2`, the result is "Tails".
    - The results of all tosses are stored in a list.

3. **Output**:
    - The program outputs the results of the coin tosses, with each result ("Heads" or "Tails") displayed on a separate line.

## Output 📜

The output consists of the results of each coin toss displayed in order, one per line.

### Example Input/Output:

**Input**:

```
Enter the number of coin toss attempts: 5
```

**Output**:

```
Heads
Tails
Heads
Heads
Tails
```

### Explanation:

-   For 5 attempts, the program randomly generates outcomes for each toss.
-   Each toss result ("Heads" or "Tails") is printed on a separate line.

## Usage 📦

1. Copy the code into a Python file (e.g., `coin_toss.py`).
2. Run the script and input the number of coin toss attempts when prompted.
3. Observe the results of the coin tosses printed line by line.

### Example Run:

```python
# Input:
Enter the number of coin toss attempts: 3

# Output:
Heads
Tails
Heads
```

## Conclusion 🚀

This simple yet engaging program illustrates randomness through coin toss simulations. It's an excellent example of using Python's `random` module and can be extended for more complex probability experiments.
