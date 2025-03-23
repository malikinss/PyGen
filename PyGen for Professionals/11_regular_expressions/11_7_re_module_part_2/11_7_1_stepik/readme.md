# Stepik Text Analyzer

## Description 📝

This program analyzes a multi-line text and determines:

-   The number of lines that begin with the word **Stepik** (case-insensitive).
-   The number of lines that end with **three dots (...)** or an **exclamation mark (!)**.

The program then outputs these two numbers, each on a separate line.

## Purpose 🎯

This script is useful for analyzing structured text data where certain lines may indicate important information based on their starting or ending words. It can help detect significant sections in an educational article or similar formatted content.

## How It Works 🔍

1. **Reads the multi-line text** stored in the `article` variable.
2. **Uses regular expressions** to:
    - Count the lines starting with `Stepik` (case-insensitive).
    - Count the lines ending with either `...` or `!`.
3. **Prints the two counts**, one per line.

## Output 📜

### Example Input (stored in `article`):

```text
Stepik (до августа 2016 года Stepic) — это образовательная
платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android.
В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном
режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать
интерактивные обучающие уроки и онлайн-курсы...
```

### Example Output:

```text
4
3
```

## Usage 📦

1. Save the script as `stepik_text_analyzer.py`.
2. Run the script.
3. The output will display two numbers:
    - **First number**: Count of lines starting with "Stepik".
    - **Second number**: Count of lines ending with `...` or `!`.

## Conclusion 🚀

This program efficiently extracts structured insights from a text, making it useful for analyzing formatted educational content, news articles, or structured reports.
