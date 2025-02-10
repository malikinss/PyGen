'''
TODO:
    Implement the hide_card() function, which takes one argument:
        - card_number - is a string representing the correct bank card number
          of 16 digits, between which there may be space characters

    The function should replace the first 12 digits in the card_number string
    with the * character and return the result.

    If there were space characters between the digits in the number,
    they should be deleted.
'''


def hide_card(card_number: str) -> str:
    """
    Hides all but the last 4 digits of the card number by replacing the first
    12 digits with asterisks. Space characters between digits are removed.

    Args:
        card_number (str): A string representing the bank card number.

    Returns:
        str: The card number with the first 12 digits replaced by asterisks.
    """
    # Remove any spaces from the card number
    cleaned_card_number = ''.join(card_number.split())

    # Ensure the card number is 16 digits long
    if len(cleaned_card_number) != 16:
        raise ValueError("Card number must be exactly 16 digits.")

    # Replace the first 12 digits with '*' and keep the last 4 digits
    return '*' * 12 + cleaned_card_number[-4:]
