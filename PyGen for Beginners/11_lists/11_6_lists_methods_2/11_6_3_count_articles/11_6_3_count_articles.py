'''
TODO:
    The input to the program is a string containing English text.

    Write a program that counts the total number of articles: 'a', 'an', 'the'.
'''


def count_articles(text: str) -> int:
    """
    Counts the total number of articles ('a', 'an', 'the') in the given text.

    Args:
        text (str): The input text string.

    Returns:
        int: The total count of articles in the text.
    """
    articles = {'a', 'an', 'the'}  # Set for faster lookups
    words = text.lower().split()  # Convert to lowercase and split into words
    return sum(1 for word in words if word in articles)


# Input: Read a string containing English text
input_text = input("Enter English text: ")

# Count the articles
total_articles = count_articles(input_text)

# Print the total number of articles
print(f"Total number of articles: {total_articles}")
