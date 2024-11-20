'''
TODO:
    The program is fed a sequence of lines, each line on a separate line.

    The end of the sequence is the word "END" (without quotes).

    However, the word "END" itself is not part of the sequence, but only
    symbolizes its end.

    Write a program that finds the maximum and minimum lines in this sequence
    (in lexicographic order) and outputs them in the following format:
        Minimum line ⬇️: <minimum line>
        Maximum line ⬆️: <maximum line>

NOTE:
    We can find maximum and minimum not only in numbers. 🤪
'''


def find_min_max_lines() -> None:
    """
    Reads a sequence of lines from the input, and finds the lexicographically
    minimum and maximum lines from the sequence (excluding the "END" line).

    Outputs the minimum and maximum lines in lexicographic order.
    """
    # Initialize min_row and max_row as None to be set with the first line
    min_row = None
    max_row = None

    while True:
        # Read the next line of input
        row = input().strip()

        # End the loop if the word "END" is encountered
        if row == "END":
            break

        # If it's the first line, initialize min_row and max_row
        if min_row is None and max_row is None:
            min_row = row
            max_row = row
        else:
            # Update the minimum and maximum rows
            min_row = min(min_row, row)
            max_row = max(max_row, row)

    # Output the results
    print(f"Minimum line ⬇️: {min_row}")
    print(f"Maximum line ⬆️: {max_row}")


# Call the function to execute the logic
find_min_max_lines()
