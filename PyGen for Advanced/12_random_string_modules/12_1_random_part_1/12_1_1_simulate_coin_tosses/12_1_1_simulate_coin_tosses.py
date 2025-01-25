'''
TODO:
    Write a program that uses the random module to simulate coin tosses.

    The program takes the number of attempts as input and outputs the results
    of the tosses:
        Heads or Tails (each on a separate line).
'''
import random
from typing import List


def simulate_coin_tosses(attempts: int) -> List[str]:
    """
    Simulates a given number of coin tosses and returns the results.

    Args:
        attempts (int): The number of coin tosses to simulate.

    Returns:
        List[str]: A list of results, where each element is either "Heads"\
                   or "Tails".
    """
    results = []
    for _ in range(attempts):
        if random.randint(1, 2) == 1:
            results.append("Heads")
        else:
            results.append("Tails")
    return results


def print_toss_results(results: List[str]) -> None:
    """
    Prints the results of coin tosses, each on a separate line.

    Args:
        results (List[str]): A list of coin toss results.

    Returns:
        None
    """
    for result in results:
        print(result)


def run_simulation() -> None:
    """
    Runs the coin toss simulation by taking input for the number of attempts
    and outputting the results of the tosses.

    Returns:
        None
    """
    attempts = int(input("Enter the number of coin toss attempts: "))
    toss_results = simulate_coin_tosses(attempts)
    print_toss_results(toss_results)


# Start the simulation
run_simulation()
