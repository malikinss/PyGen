'''
TODO:
    All books in the home library of Dushnila, Sam's friend, must be sorted
    in ascending order:
        first by author's last name, and if the last names match,
        then by title.

    Write a program that checks whether the books are sorted correctly.

    Your program receives the number n as input, and then n lines, each line
    representing a book in the following format:
        <author's last name> <author's initials>, "<book title>"

    The program should output "YES" (without quotes) if the books are sorted
    according to Dushnila's wishes, or "NO" (without quotes) otherwise.

NOTE:
    Please note that Dushnila ignores the author's initials when sorting books.

    It is guaranteed that no books in a set are repeated.

    It is guaranteed that the author's last name consists of one word.
'''


def check_books_sorted(n: int) -> None:
    """
    Checks if the list of books is sorted by the author's last name and,
    if needed, by the book's title.

    Parameters:
    n (int): The number of books in the library.
    """
    books = []

    # Read the books' details
    for _ in range(n):
        book = input().strip()
        # Split the input to extract author's last name and title
        last_name, rest = book.split(' ', 1)
        # Extract title by removing surrounding quotes
        title = rest.split('",')[0][1:]
        books.append((last_name, title))

    # Check if the books are sorted according to the required criteria
    for i in range(1, len(books)):
        if books[i-1] > books[i]:
            print("NO")
            return

    print("YES")


# Read the number of books and check the sorting
n = int(input())  # Number of books
check_books_sorted(n)
