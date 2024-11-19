'''
TODO:
    Due to a cyberattack on the bank "Razbogatem Vmeste" the algorithm that
    displays exchange rates for a certain date in the mobile
    application has broken.

    The bank's technical department asks you to fix the situation
    and establish the output.

    The program receives the following values as input:
        - date (in the format DD-MM-YYYY)
        - dollar exchange rate (how many Russian rubles are worth 1 dollar)
        - yuan exchange rate (how many Russian rubles are worth 1 yuan)

    Write a program that outputs a line showing how many Russian rubles
    are worth 1 dollar and 1 yuan on the specified date in the format:
        On <date>: 1$ = <dollar exchange rate>₽, 1¥ = <yuan exchange rate>₽
'''


def display_exchange_rate(date: str,
                          rub_per_usd: float,
                          rub_per_cny: float) -> str:
    """
    This function returns a formatted string displaying the exchange rates
    for USD and CNY to Russian rubles on a specific date.

    Parameters:
    - date (str): The date in the format DD-MM-YYYY.
    - rub_per_usd (float): The exchange rate for 1 USD in Russian rubles.
    - rub_per_cny (float): The exchange rate for 1 CNY in Russian rubles.

    Returns:
    - str: A formatted string showing the exchange rates for 1 USD and 1 CNY
    in Russian rubles.

    Example:
    >>> display_exchange_rate("20-11-2024", 74.5, 10.5)
    "On 20-11-2024: 1$ = 74.5₽, 1¥ = 10.5₽"
    """
    return f"On {date}: 1$ = {rub_per_usd}₽, 1¥ = {rub_per_cny}₽"


# Input values
date: str = input()
rub_per_usd: float = float(input())  # Dollar exchange rate in rubles
rub_per_cny: float = float(input())  # Yuan exchange rate in rubles

# Call the function and print the result
print(display_exchange_rate(date, rub_per_usd, rub_per_cny))
