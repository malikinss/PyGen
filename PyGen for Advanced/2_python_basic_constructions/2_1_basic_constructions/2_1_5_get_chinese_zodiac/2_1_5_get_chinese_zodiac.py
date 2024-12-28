'''
TODO:
    The Chinese horoscope assigns years to animals in a 12-year cycle.

    Thus, 2012 will be another year of the dragon.

    Write a program that reads the year and displays the name
    of the animal associated with it.
'''


def get_chinese_zodiac(year: int) -> str:
    """
    Given a year, returns the animal associated with it according
    to the Chinese zodiac.

    The Chinese zodiac follows a 12-year cycle:
        Rat, Ox, Tiger, Rabbit, Dragon, Snake,
        Horse, Sheep, Monkey, Rooster, Dog, Pig

    Args:
        year (int): The year to find the associated animal for.

    Returns:
        str: The name of the animal for the given year.
    """
    animals = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig'
    ]

    # The cycle starts in 1900, which was the year of the Rat
    return animals[(year - 1900) % 12]


def main() -> None:
    """
    Main function to take year input, determine the Chinese zodiac animal,
    and print the result.
    """
    year = int(input("Enter the year: "))
    print(get_chinese_zodiac(year))


if __name__ == "__main__":
    main()
