'''
TODO:
    The input to the program is three natural numbers m, p, n:
        m: starting number of organisms;
        p: average daily increase in %;
        n: number of days to breed.

    Write a program that predicts the size of a population of organisms.
    The program should output the population size on each day, starting
    on day 1 and ending on the nth day.
'''


def predict_population_growth(initial_population: int,
                              daily_increase_percent: float,
                              days: int) -> None:
    """
    Predicts and prints the population size of organisms over a given
    number of days.

    Args:
        initial_population (int): The starting number of organisms.
        daily_increase_percent (float): The average daily increase
        as a percentage.
        days (int): The number of days to breed.

    Returns:
        None

    The function prints the population size on each day, starting from
    day 1 up to the specified number of days.
    """
    # Convert daily increase percentage to multiplier for population growth
    daily_increase_multiplier = 1 + daily_increase_percent / 100

    population = initial_population
    for day in range(1, days + 1):
        print(f"Day {day}: {population:.2f}")
        population *= daily_increase_multiplier


# Input data
initial_population = int(input("Enter the starting number of organisms: "))
daily_increase_percent = float(input("Enter the average daily increase (%): "))
days = int(input("Enter the number of days to breed: "))

# Run the population growth prediction
predict_population_growth(initial_population, daily_increase_percent, days)
