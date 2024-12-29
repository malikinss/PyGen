'''
TODO:
    Timur and Ruslan are trying to share the front of work on
    the "Python for Professionals" course.

    To do this, they decided to play rock, paper and scissors.

    Help the kids cast fair lots and determine who will do the next module
    of the new course.

    The program receives two lines of text containing the words "rock",
    "scissors" or "paper" as input.

    The first line records Timur's choice, the second line records
    Ruslan's choice.
'''


def determine_winner(timur_move: str, ruslan_move: str) -> str:
    """
    Determines the winner of a rock-paper-scissors game between Timur
    and Ruslan.

    Parameters:
    - timur_move (str): The move of Timur, which can be "rock", "scissors",
                        or "paper".
    - ruslan_move (str): The move of Ruslan, which can be "rock", "scissors",
                         or "paper".

    Returns:
    - str: "Timur" if Timur wins, "Ruslan" if Ruslan wins, or "draw" if
           it's a tie.
    """
    options = ["rock", "scissors", "paper"]
    results = ["draw", "Ruslan", "Timur"]

    case = options.index(timur_move) - options.index(ruslan_move)
    return results[case]


def main() -> None:
    """
    Main function to read the input from the user and determine the winner.
    """
    timur_move = input("Enter Timur's choice (rock, scissors, paper): ")
    ruslan_move = input("Enter Ruslan's choice (rock, scissors, paper): ")

    result = determine_winner(timur_move, ruslan_move)
    print(result)


if __name__ == "__main__":
    main()
