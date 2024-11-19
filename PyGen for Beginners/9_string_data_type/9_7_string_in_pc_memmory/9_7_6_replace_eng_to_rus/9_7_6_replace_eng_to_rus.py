'''
TODO:
    As you remember from the previous task, Timur pays moderator Sam for each
    character of his messages in the comments in 🐝 (bee-coins)
    at the following rate:
        <symbol code in the Unicode table>x3🐝

    And the cost of the entire message is made up of the sum of the costs
    of all the characters.

    This time, Sam wanted to cheat and try to increase the cost of his message
    by replacing some English letters in it with Russian ones.

    As you remember, Russian letters in the Unicode table are after
    English ones.

    Sam wants to replace the following English letters:
        eyopaxcETOPAHXCBM
    with the corresponding Russian letters:
        еуорахсЕТОранХСВМ

    Timur will not notice the difference visually, and Sam will be able
    to earn more bee-coins. 😊

    A string of text is fed to the program's input.

    You need to write a program that finds the cost of Sam's old and
    new messages in 🐝 and outputs the text in the following format:
        Old cost: <cost of old message>🐝
        New cost: <cost of new message>🐝

NOTE:
    Please note that if you cannot replace letters in the string, the cost
    of the message will not change. 😢
'''


def get_comment_cost(comment: str) -> int:
    """
    Calculates the cost of a comment in 🐝 (bee-coins) based on the Unicode
    value of each character.
    Each character's cost is calculated as:
        <Unicode value> * 3

    Parameters:
    - comment (str): The text of the comment.

    Returns:
    - int: The total cost of the comment in 🐝.
    """
    total = 0
    for symbol in comment:
        # Calculate the cost of each character and add it to the total
        total += (ord(symbol) * 3)
    return total


def replace_eng_to_rus(comment: str) -> str:
    """
    Replaces specific English letters in the text with their corresponding
    visually similar Russian letters to increase the cost of the message.

    English letters to be replaced:
        eyopaxcETOPAHXCBM
    Corresponding Russian letters:
        еуорахсЕТОРАНХСВМ

    Parameters:
    - comment (str): The original text of the comment.

    Returns:
    - str: The modified text with English letters replaced by Russian ones.
    """
    ENG_LETTERS = "eyopaxcETOPAHXCBM"
    RUS_LETTERS = "еуорахсЕТОРАНХСВМ"

    new_comment = ''

    for symbol in comment:
        # Check if the character is in the list of English letters
        if symbol in ENG_LETTERS:
            # Replace it with the corresponding Russian letter
            symbol = RUS_LETTERS[ENG_LETTERS.index(symbol)]
        new_comment += symbol

    return new_comment


# Input: original comment text
comment = input("Enter your comment: ")
# Calculate the cost of the original comment
old_cost = get_comment_cost(comment)

# Replace English letters with Russian equivalents
new_comment = replace_eng_to_rus(comment)
# Calculate the cost of the modified comment
new_cost = get_comment_cost(new_comment)

# Output the costs of the original and modified comments
print(f'Old cost: {old_cost}🐝')
print(f'New cost: {new_cost}🐝')
