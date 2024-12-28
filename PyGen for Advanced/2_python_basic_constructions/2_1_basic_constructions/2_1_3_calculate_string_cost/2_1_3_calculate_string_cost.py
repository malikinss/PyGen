'''
TODO:
    Given a line of text.

    Write a program to calculate the cost of a string, based on the fact
    that any one character (including a space) costs 50 cents.

    Give your answer in dollars and cents according to the examples.
'''


def calculate_string_cost(text: str) -> str:
    """
    Calculate the cost of a string based on the number of characters.
    Each character, including spaces, costs 50 cents.

    Args:
        text (str): The input string whose cost needs to be calculated.

    Returns:
        str: The cost of the string in dollars and cents.
    """
    each_char_price = 50
    length_of_string = len(text)

    string_total_price_in_cents = length_of_string * each_char_price

    dollars = string_total_price_in_cents // 100
    cents = string_total_price_in_cents % 100

    return f"{dollars} dollars {cents} cents"


def main() -> None:
    """
    Main function to take input, calculate the string cost,
    and print the result.
    """
    input_string = input("Enter the text: ")
    print(calculate_string_cost(input_string))


if __name__ == "__main__":
    main()
