'''
TODO:
    Morse code uses dashes and dots to represent numbers and letters.

    Write a program to encode a text message using Morse code.
        ________________________________________________
        | A | .-   | J | .---  | S | ...   | 1 | .---- |
        | B | -... | K | -.-   | T | -     | 2 | ..--- |
        | C | -.-. | L | .-..  | U | ..-   | 3 | ...-- |
        | D | -..  | M | --    | V | ...-  | 4 | ....- |
        | E | .    | N | -.    | W | .--   | 5 | ..... |
        | F | ..-. | O | ---   | X | -..-  | 6 | -.... |
        | G | --.  | P | .--.  | Y | -.--  | 7 | --... |
        | H | .... | Q | --.-  | Z | --..  | 8 | ---.. |
        | I | ..   | R | .-.   | 0 | ----- | 9 | ----. |

NOTE:
    Your program must ignore the case of the characters in the original
    text message.

    Your program should ignore any characters not listed in the table.

    Morse code was developed in the 19th century and is still in use more
    than 160 years after its creation.
'''

# Dictionary for Morse code translation
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


def text_to_morse(message: str) -> str:
    """
    Converts a given text message into Morse code.

    Arguments:
    message: str -- the text message to be converted to Morse code

    Returns:
    str -- Morse code translation of the input message
    """
    # Convert the message to uppercase and process it
    message = message.upper()
    morse_message = []

    for char in message:
        # Only translate valid characters
        if char in morse_code:
            morse_message.append(morse_code[char])

    # Return the Morse code as a single string
    return ' '.join(morse_message)


# Get user input
given_text = input("Enter your message: ")

# Convert to Morse code and print the result
morse_code_result = text_to_morse(given_text)
print(morse_code_result)
