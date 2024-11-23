'''
TODO:
    The input to the program is a text string containing integers.

    Write a program that draws a bar chart given numbers.
'''


def draw_bar_chart(numbers: str) -> None:
    """
    This function takes a string of space-separated integers and draws
    a bar chart where each integer is represented by a line of '+'
    characters corresponding to its value.

    Args:
        numbers (str): A string containing space-separated integers.

    Returns:
        None: The function prints a bar chart where each integer
        is represented by '+' characters.
    """
    # Split the input string by spaces and process each element
    for element in numbers.split():
        print("+" * int(element))


# Input string containing space-separated integers
numbers_input = input()

# Call the function to draw the bar chart
draw_bar_chart(numbers_input)
