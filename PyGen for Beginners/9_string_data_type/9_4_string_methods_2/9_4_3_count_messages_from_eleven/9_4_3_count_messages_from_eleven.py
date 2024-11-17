'''
TODO:
    Jim Hopper tries to get a message from Eleven using the radio.

    The receiver receives n different Morse code sequences.

    Having decoded them, he receives sequences of numbers and a lowercase
    Latin alphabet, while all of Eleven's messages contain the number 11,
    and at least 3 times.

    Help Jim determine the number of messages from Eleven.
'''


def count_messages_from_eleven(n: int, messages: list) -> int:
    """
    Counts how many messages contain the number "11" at least three times.

    Args:
        n (int): The number of Morse code sequences.
        messages (list): A list of Morse code sequences (strings).

    Returns:
        int: The number of messages that contain the number "11"
        at least three times.
    """
    msg_cnt = 0

    for message in messages:
        if message.count('11') >= 3:
            msg_cnt += 1

    return msg_cnt


# User input
n = int(input("Enter the number of messages: "))
messages = [input("Enter message: ") for _ in range(n)]

# Get the result and print
result = count_messages_from_eleven(n, messages)
print(result)
