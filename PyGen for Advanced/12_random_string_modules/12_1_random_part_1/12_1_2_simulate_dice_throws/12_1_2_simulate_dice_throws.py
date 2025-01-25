'''
TODO:
    Write a program that uses the random module to simulate throws of
    a 6-sided dice.

    The program takes the number of attempts as input and outputs the results
    of the throws — the number that came up, which is written on the face
    of the dice (each on a separate line).
'''
import random
from typing import List


def simulate_dice_throws(attempts: int) -> List[int]:
    """
    Simulates a given number of throws of a 6-sided dice and returns
    the results.

    Args:
        attempts (int): The number of dice throws to simulate.

    Returns:
        List[int]: A list of integers representing the results of the dice
                   throws.
    """
    return [random.randint(1, 6) for _ in range(attempts)]


def print_throw_results(results: List[int]) -> None:
    """
    Prints the results of dice throws, each on a separate line.

    Args:
        results (List[int]): A list of dice throw results.

    Returns:
        None
    """
    for result in results:
        print(result)


def run_dice_simulation() -> None:
    """
    Runs the dice throw simulation by taking input for the number of attempts
    and outputting the results of the throws.

    Returns:
        None
    """
    attempts = int(input("Enter the number of dice throw attempts: "))
    results = simulate_dice_throws(attempts)
    print_throw_results(results)


# Start the simulation
run_dice_simulation()
