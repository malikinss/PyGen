# Chinese Zodiac Program 🐉

## Description 📝

This program reads a given year and determines the associated animal from the Chinese zodiac.
The Chinese zodiac follows a 12-year cycle, with each year represented by a different animal.

## Purpose 🎯

The program helps users identify the animal of the Chinese zodiac corresponding to a given year.
This is useful for those interested in astrology or simply curious about their zodiac animal.

## How It Works 🔍

1. **Input Format**:
    - The user is prompted to input a year (integer).
2. **Logic**:

    - The Chinese zodiac follows a 12-year cycle starting from the year 1900, which was the year of the Rat.
    - The program uses the formula `(year - 1900) % 12` to find the position of the year in the zodiac cycle.
    - The program then returns the animal associated with that cycle position.

3. **Example**:

    ```
    Enter the year: 2012
    Output: Dragon
    ```

    The program correctly associates the year 2012 with the Dragon in the Chinese zodiac.

4. **Edge Cases**:
    - The program works for any valid year, including historical years before or after 1900.

## Usage 📦

1. Copy the code into a Python file, e.g., `chinese_zodiac.py`.
2. Run the script in the terminal:
    ```bash
    python chinese_zodiac.py
    ```
3. Enter the year when prompted.
4. The program will output the animal associated with that year.

## Conclusion 🚀

This simple program is an easy way to find the Chinese zodiac animal for any given year, making it a fun tool for those interested in astrology.
