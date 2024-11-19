'''
TODO:
    The traffic police decided to optimize the process of creating license
    plates:
        instead of a person, they assigned the generation of license plates
        to a certain GPT (machine learning model).

    As we know, artificial intelligence is still raw and makes many mistakes,
    so its results should be carefully checked.

    Write a program that takes a string as input and checks whether
    this string is a valid license plate.

    The program should output "YES" (without quotes) if the artificial
    intelligence coped with its task, or "NO" (without quotes) otherwise.

    In our task, the following formats will be considered as correct license
    plates:
        <LETTER><DIGIT><DIGIT><LETTER><LETTER>_<DIGIT><DIGIT>
        <LETTER><DIGIT><DIGIT><LETTER><LETTER>_<DIGIT><DIGIT><DIGIT>
    where <DIGIT> is any digit, and <LETTER> is one of the Cyrillic
    letters АВЭКМНОРСТУХ.
'''


def is_correct_car_plate(car_plate: str):
    """
    Checks whether a given car plate is valid according to the
    specified format.

    Args:
        car_plate (str): The license plate to check.

    Returns:
        None: Prints "YES" if valid, otherwise "NO".
    """
    # Allowed Cyrillic letters for license plates
    possible_letters = "АВЭКМНОРСТУХ"
    valid_lengths = {9, 10}

    if len(car_plate) not in valid_lengths or car_plate[6] != "_":
        print("NO")
        return

    letters_in_plate = car_plate[0] + car_plate[4:6]
    for letter in letters_in_plate:
        if letter not in possible_letters:
            print("NO")
            return

    numbers_in_plate = car_plate[1:4] + car_plate[7:]
    if not numbers_in_plate.isdigit():
        print("NO")
        return

    # If all checks pass
    print("YES")


# Input and function call
given_car_number = input()
is_correct_car_plate(given_car_number)
