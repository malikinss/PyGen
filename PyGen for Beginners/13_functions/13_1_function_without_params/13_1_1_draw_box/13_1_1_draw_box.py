'''
TODO:
    Write a draw_box() function that draws a 14x10 star box, as shown:
        **********
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        *        *
        **********
'''


def draw_box() -> None:
    """
    Draws a 14x10 star box. The box has 14 rows and 10 columns:

    - The first and last rows are filled with stars (**********).
    - The middle rows have stars at the start and end, with 8 spaces
      in between.

    This function prints the box directly to the console.

    Example Output:
    **********
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    **********

    Returns:
    None
    """
    for i in range(14):
        if i == 0 or i == 13:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')


# Example usage
draw_box()
