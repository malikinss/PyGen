'''
TODO:
    At the end of the school year, Ruslan received a reading list for
    the summer.

    Now he needs to figure out which books from this list he has.

    Ruslan has all the books from his home library written down in a text file
    on his computer in random order.

    Write a program that determines for each book from the reading list
    whether Ruslan has it or not.
'''


def check_books_in_library(library_books: set, task_books: list) -> None:
    """
    Checks for each book in the summer reading list whether Ruslan has it in
    his library.

    Args:
        library_books (set): A set of books Ruslan has in his library.
        task_books (list): A list of books from the summer reading list
                           to check.

    Returns:
        None: Prints "YES" if the book is in the library, "NO" otherwise.
    """
    for book in task_books:
        if book in library_books:
            print("YES")
        else:
            print("NO")


def main() -> None:
    """
    Main function to read input and call the check_books_in_library function.
    """
    ruslan_lib_books_number = int(input())
    summer_task_books_number = int(input())

    ruslan_lib_books_set = {input() for _ in range(ruslan_lib_books_number)}
    summer_task_books_list = [input() for _ in range(summer_task_books_number)]

    check_books_in_library(ruslan_lib_books_set, summer_task_books_list)


if __name__ == "__main__":
    main()
