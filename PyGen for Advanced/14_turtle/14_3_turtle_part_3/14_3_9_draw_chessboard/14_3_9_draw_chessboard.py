'''
TODO:
    Write a program that draws an image of a chessboard using a sample.
'''
import turtle


def setup_turtle(square_size: int) -> None:
    """
    Sets up the turtle properties for drawing the chessboard.

    Args:
        square_size (int): The size of one square on the chessboard.

    Returns:
        None: The function configures the turtle but does not return any value.
    """
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.shape('square')

    # Adjust the shape size to fit the square_size
    turtle.shapesize(square_size / 20)


def calculate_position(
    row: int, col: int, step: int, board_size: int
) -> tuple[int, int]:
    """
    Calculates the position of a square on the chessboard.

    Args:
        row (int): The row number of the square.
        col (int): The column number of the square.
        step (int): The size of each square.
        board_size (int): The size of the chessboard (number of squares along
                          one side).

    Returns:
        tuple[int, int]: The (x, y) coordinates of the square's center.
    """
    x = col * step - (board_size * step) / 2
    y = row * step - (board_size * step) / 2

    res: tuple = x, y
    return res


def get_square_color(row: int, col: int) -> str:
    """
    Determines the color of a square based on its row and column.

    Args:
        row (int): The row number of the square.
        col (int): The column number of the square.

    Returns:
        str: 'white' if the square is white, 'black' if the square is black.
    """
    return 'white' if (row + col) % 2 == 0 else 'black'


def draw_square(row: int, col: int, step: int, board_size: int) -> None:
    """
    Draws a single square on the chessboard.

    Args:
        row (int): The row number of the square.
        col (int): The column number of the square.
        step (int): The size of each square.
        board_size (int): The size of the chessboard (number of squares along
                          one side).

    Returns:
        None: The function draws one square and does not return any value.
    """
    turtle.fillcolor(get_square_color(row, col))
    x, y = calculate_position(row, col, step, board_size)
    turtle.setpos(x, y)
    turtle.stamp()


def draw_chessboard(board_size: int, square_size: int) -> None:
    """
    Draws a chessboard using turtle graphics.

    Args:
        board_size (int): The size of the chessboard (number of squares along
                          one side).
        square_size (int): The size of one square on the chessboard.

    Returns:
        None: The function draws the chessboard but does not return any value.
    """
    setup_turtle(square_size)

    # Set step as the size of each square
    step = square_size

    for row in range(board_size):
        for col in range(board_size):
            draw_square(row, col, step, board_size)

    turtle.done()


# Main code to draw the chessboard
board_size = 8  # Size of the chessboard (8x8)
square_size = 40  # Size of each square

draw_chessboard(board_size, square_size)
