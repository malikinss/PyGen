'''
TODO:
    Write a program using a recursive function that prints an hourglass image
    made up of the digits 1, 2, 3, and 4:
        1111111111111111    # 16 times
         2222222222222      # 12 times
            33333333        # 8 times
              4444          # 4 times
            33333333        # 8 times
         2222222222222      # 12 times
        1111111111111111    # 16 times
'''


def display_layer(layer_str: str) -> None:
    """
    Displays a single layer of the hourglass.

    Args:
        layer_str (str): The string of digits to be displayed.
    """
    print(layer_str.center(16))


def draw_hourglass() -> None:
    """
    Draws an hourglass shape using digits 1 through 4, recursively.

    This function prints the top and bottom halves of the hourglass,
    with decreasing and then increasing numbers of repeated digits.

    The hourglass shape is formed by starting with '1' repeated 16 times
    and decreasing by 4 digits at each step until '4', then reversing
    the pattern.
    """

    def draw_layer(digit_value: int, repeat_count: int) -> None:
        """
        Recursively draws each layer of the hourglass.

        Args:
            digit_value (int): The digit to be repeated in the layer.
            repeat_count (int): The number of times the digit is repeated.
        """
        layer_str = str(digit_value) * repeat_count

        if repeat_count > 4:
            display_layer(layer_str)  # Display the current layer
            draw_layer(digit_value + 1, repeat_count - 4)

        display_layer(layer_str)  # Display the mirrored layer

    draw_layer(1, 16)


draw_hourglass()
