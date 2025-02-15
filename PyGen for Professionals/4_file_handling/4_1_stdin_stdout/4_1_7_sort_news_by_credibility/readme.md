# News Credibility and Categorization Bot

## Description 📝

This Python program reads news records, filters them by a specific category, and sorts them by credibility in ascending order.
If there are multiple news records with the same credibility, the news will be sorted lexicographically by title.
The program helps users view the most reliable news within a certain category.

## Purpose 🎯

The purpose of this program is to display all news articles belonging to a specific category, ranked by their credibility, allowing users to easily identify the most trustworthy sources within that category.

## How It Works 🔍

1. **Function `read_input()`**:

    - Reads input data from the standard input and returns a list of stripped lines.

2. **Function `filter_news_by_category(news, category)`**:

    - Filters the list of news records based on the provided category.

3. **Function `print_sorted_news(news)`**:

    - Prints the sorted news records, first by credibility in ascending order, and by title within the same credibility.

4. **Function `extract_news_and_category()`**:

    - Extracts news records and the desired category from the input.

5. **Function `parse_news_record(record)`**:

    - Converts a news record in the format `title/category/credibility` into a `NewsRecord` dataclass.

6. **Function `sort_news_by_credibility(news)`**:
    - Sorts the news records first by credibility in ascending order and second by title lexicographically if the credibility is the same.

### Example:

For input:

```
Breaking news on the elections/Politics/8.5
Economic growth rises/Economy/7.3
Weather report/Weather/5.5
Politics debate/Politics/9.1
```

If the user selects the "Politics" category, the program will output:

```
Breaking news on the elections
Politics debate
```

## Output 📜

The program outputs the titles of news articles in the specified category, sorted by credibility (ascending), and by title within the same credibility.

Example output:

```
Breaking news on the elections
Politics debate
```

## Usage 📦

1. Save the code in a file named `news_bot.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script and provide input via standard input.

### Example usage:

```bash
$ python news_bot.py
Breaking news on the elections/Politics/8.5
Economic growth rises/Economy/7.3
Weather report/Weather/5.5
Politics debate/Politics/9.1
Politics
```

The output will be:

```
Breaking news on the elections
Politics debate
```

## Conclusion 🚀

This program effectively sorts and filters news by category and credibility, providing users with a simple way to view reliable news in a specific category.
It ensures that the most trustworthy news sources are presented first.
