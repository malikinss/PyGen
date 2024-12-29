'''
TODO:
    Having lost to Timur 10 times, Ruslan realized that things couldn't go
    on like this and decided to complicate the game.

    Now Timur and Ruslan are playing the game Rock, Paper, Scissors, Lizard,
    Spock.

    Help the kids cast fair lots again and determine who will do the next
    module in the new course.

NOTE:
    The rules of the game are standard:
        - The scissors cut paper.
        - The paper wraps the stone.
        - The rock crushes the lizard.
        - The lizard poisons Spock
        - Spock breaks the scissors
        - The scissors cut off the head of the lizard
        - The lizard eats the paper
        - The paper contains evidence against Spock.
        - Spock vaporizes the stone
        - The stone, of course, dulls the scissors.
'''


def determine_winner(timur_move: str, ruslan_move: str) -> str:
    """
    Determines the winner of a game of Rock, Paper, Scissors, Lizard, Spock.

    Parameters:
    - timur_move (str): The move of Timur, one of "Stone", "Lizard", "Spock",
                        "Scissors", "Paper".
    - ruslan_move (str): The move of Ruslan, one of "Stone", "Lizard",
                         "Spock", "Scissors", "Paper".

    Returns:
    - str: "Timur" if Timur wins, "Ruslan" if Ruslan wins, or "Draw" if
            it's a tie.
    """
    # Rules of the game in terms of what each element defeats
    defeats = {
        "Stone": ["Scissors", "Lizard"],
        "Scissors": ["Paper", "Lizard"],
        "Paper": ["Stone", "Spock"],
        "Lizard": ["Spock", "Paper"],
        "Spock": ["Scissors", "Stone"]
    }

    if timur_move == ruslan_move:
        return "Draw"
    elif ruslan_move in defeats[timur_move]:
        return "Timur"
    else:
        return "Ruslan"


def main() -> None:
    """
    Main function to read the input from the user and determine the winner.
    """
    timur_move = input("Enter Timur's choice: ")
    ruslan_move = input("Enter Ruslan's choice: ")

    result = determine_winner(timur_move, ruslan_move)
    print(result)


if __name__ == "__main__":
    main()
