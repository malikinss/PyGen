'''
TODO:
    Write a function generate_letter() that will assemble an email according
    to the template:
        To: <mail>
        Hello, <name>!
        You have an exam scheduled for <date>, at <time>.
        At: <place>.

        The exam will be conducted by <teacher> in room <number>.
        Good luck on the exam!

    The function should receive five mandatory arguments mail, name, date,
    time, place and two optional arguments teacher, number and return the text
    of the finished letter.

    If the teacher argument is missing, the teacher will be Timur Guev, and if
    the number argument is missing, the room will be 17.
'''


def generate_letter(
    mail: str,
    name: str,
    date: str,
    time: str,
    place: str,
    teacher: str = 'Тимур Гуев',
    number: int = 17
) -> str:
    """
    Generates an email text with exam details based on the provided
    information.

    Args:
        mail (str): The recipient's email address.
        name (str): The recipient's name.
        date (str): The date of the exam.
        time (str): The time of the exam.
        place (str): The location of the exam.
        teacher (str, optional): The teacher conducting the exam.
                                 Defaults to 'Тимур Гуев'.
        number (int, optional): The room number where the exam will take place.
                                Defaults to 17.

    Returns:
        str: The formatted email text.
    """
    return '\n'.join([
        f"To: {mail}",
        f"Hello, {name}!",
        f"You have an exam scheduled for {date}, at {time}.",
        f"At: {place}.",
        f"The exam will be conducted by {teacher} in room {number}.",
        "Good luck on the exam!"
    ])
