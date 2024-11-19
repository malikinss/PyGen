'''
TODO:
    Timur pays moderator Sam for each character of his comments
    in 🐝 (bee-coins) at the following rate:
        <symbol code in the Unicode table>x3🐝

    And the cost of the entire message is the sum of the costs
    of all the characters.

    Sam wanted to calculate how many 🐝 he earns for his comments and
    asks you to help him.

    The program receives a text string as input.

    You need to write a program that finds the cost of Sam's message in 🐝
    and outputs the text in the following format:
        Message text: '<Sam's message text>'
        Message cost: <Sam's message cost>🐝

NOTE:
    🐝 (bee-coin) is the virtual currency of the BEEGEEK team, which Timur uses
    to pay his employees.
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
        total += (ord(symbol) * 3)
    return total


# Input: The comment string
comment = input("Enter the comment: ")

# Calculate the cost
comment_cost = get_comment_cost(comment)

# Output the results
print(f"Message text: '{comment}'")
print(f"Message cost: {comment_cost}🐝")
