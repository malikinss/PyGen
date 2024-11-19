'''
TODO:
    The legion of Caesar, created in the 23rd century on the
    basis of the Roman Empire, does not change the ancient traditions
    and uses the Caesar cipher.

    This let them down, because this cipher is very simple.

    However, in the post-apocalypse, people do not know well all the
    intricacies of the pre-war world, so scientists from the NKR cannot
    figure out exactly how to decode these messages.

    Write a program to decode this cipher.
'''


def decode_caesar_cipher(shift: int, given_string: str) -> str:
    """
    This function decodes a Caesar ciphered string by shifting the letters
    back by the specified number.

    Parameters:
    - shift (int): The number of positions the alphabet was shifted
    in the cipher.
    - given_string (str): The string to decode.

    Returns:
    - str: The decoded string.
    """
    decoded_string = ""
    for element in given_string:
        cur_n = ord("a") + (ord(element) - ord("a") + 26 - shift) % 26
        decoded_string += chr(cur_n)

    return decoded_string


# Input values
shift = int(input())
given_string = input()

# Decode the string using the Caesar cipher
decoded_message = decode_caesar_cipher(shift, given_string)

# Output the decoded message
print(decoded_message)
