'''
TODO:
    On push-button mobile phones, text messages can be sent using the numeric
    keypad.

    Since each key has multiple letters associated with it, most letters
    require multiple keystrokes.

    Pressing a number once generates the first character specified
    for that key.

    Pressing a number 2,3,4, or 5 times generates the second, third, fourth,
    or fifth character of the key.
        1 .,?!:
        2 ABC
        3 DEF
        4 GHI
        5 JKL
        6 MNO
        7 PQRS
        8 TUV
        9 WXYZ
        0 space

    Write a program that displays the keystrokes required for the message
    entered.

NOTE:
    Your program must handle both uppercase and lowercase letters.
    Your program must ignore any characters not listed in the table above.
'''

# Dictionary for mobile keypad layout
keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}


def get_keystrokes_for_message(message: str) -> str:
    """
    Converts a message into the sequence of keystrokes on a mobile keypad.

    Arguments:
    message: str -- the message to be converted to keystrokes

    Returns:
    str -- a string of keystrokes required to type the message
    """
    # Convert the message to uppercase
    message = message.upper()

    keystrokes = ''
    for symbol in message:
        for key, value in keyboard.items():
            if symbol in value:
                keystrokes += key * (value.index(symbol) + 1)
                break  # Move to the next symbol once a match is found

    return keystrokes


# Get user input
given_text = input("Enter your message: ")

# Get the keystrokes and print the result
keystrokes_result = get_keystrokes_for_message(given_text)
print(keystrokes_result)
