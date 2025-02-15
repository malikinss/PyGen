'''
TODO:
    News of dubious content began to appear in the chats of one well-known
    messenger.

    It turned out that a certain youth club decided to play a joke, spreading
    all sorts of nonsense.

    However, such hooliganism bothers gullible people, especially those of
    retirement age, so a group of independent programmers decided to develop
    a bot that could assess the degree of reliability of the news, as well as
    classify it into any category.

    Write a program that displays all news in a given category, ranking them
    in ascending order of credibility.
'''
import sys
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class NewsRecord:
    title: str
    category: str
    credibility: float


def read_input() -> List[str]:
    """
    Reads input from stdin and returns a list of stripped lines.

    Returns:
        List[str]: A list of lines from input.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def filter_news_by_category(
    news: List[NewsRecord], category: str
) -> List[NewsRecord]:
    """
    Filters the news records by the specified category.

    Args:
        news (List[NewsRecord]): List of news records.
        category (str): The category to filter news by.

    Returns:
        List[NewsRecord]: A list of filtered news records.
    """
    return [record for record in news if record.category == category]


def print_sorted_news(news: List[NewsRecord]) -> None:
    """
    Prints the news sorted by credibility in ascending order and by title
    lexicographically within the same credibility.

    Args:
        news (List[NewsRecord]): List of sorted news records.
    """
    for record in news:
        print(record.title)


def extract_news_and_category() -> Tuple[List[str], str]:
    """
    Extracts the list of news and the chosen category from the input.

    Returns:
        Tuple[List[str], str]: A tuple containing the list of news and the
                               selected category.
    """
    news = read_input()
    category = news[-1]
    news.pop()
    return news, category


def parse_news_record(record: str) -> NewsRecord:
    """
    Parses a single news record string into a NewsRecord dataclass.

    Args:
        record (str): A single line of news in the format
                      'title/category/credibility'.

    Returns:
        NewsRecord: A NewsRecord object with title, category, and credibility.
    """
    title, category, credibility = record.split('/')
    return NewsRecord(
        title.strip(), category.strip(), float(credibility.strip())
    )


def sort_news_by_credibility(news: List[NewsRecord]) -> List[NewsRecord]:
    """
    Sorts news records by credibility in ascending order and by title
    lexicographically within the same credibility.

    Args:
        news (List[NewsRecord]): List of news records.

    Returns:
        List[NewsRecord]: The sorted list of news records.
    """
    return sorted(news, key=lambda x: (x.credibility, x.title))


# Main execution
news_str, category = extract_news_and_category()
news_records = [parse_news_record(record) for record in news_str]
filtered_news = filter_news_by_category(news_records, category)
sorted_news = sort_news_by_credibility(filtered_news)
print_sorted_news(sorted_news)
