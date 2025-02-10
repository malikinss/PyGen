# Similar Words Finder

## Description 📝

This program finds all words that are similar to a given word based on the arrangement of vowels and consonants.
Words are considered similar if they have the same number and arrangement of vowel letters, though the actual vowels may differ.
The program supports the Russian language, where vowels are: а, у, о, ы, и, э, я, ю, ё, е, and consonants are the other letters in the Russian alphabet.

## Purpose 🎯

The goal of this program is to identify words that share a similar vowel-consonant pattern with a given word, without considering the specific vowels used, but rather their arrangement.

## How It Works 🔍

1. The program first accepts the word to compare and analyzes its vowel-consonant pattern.
2. It then asks for the number of words to compare against the initial word.
3. For each word in the list, the program checks if its vowel-consonant pattern matches that of the given word.
4. It outputs all the words that share the same pattern in the same order as they were entered.
5. If no similar words are found, it prints a message indicating that no similar words exist.

## Output 📜

Example usage and expected outputs:

```python
Input:
пирог
5
письмо
город
поезд
покер
пиво

Output:
письмо
поезд
покер
```

If no similar words are found:

```python
Input:
пирог
3
работа
молоко
компот

Output:
No similar words found.
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Run the program in your script or interactive Python shell.

Example:

```python
from similar_words_finder import find_similar_words_by_vowels

RU_VOWELS = set(['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'])
RU_CONSONANTS = set(['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш'])

word_to_compare = "пирог"
result = find_similar_words_by_vowels(word_to_compare, RU_VOWELS, RU_CONSONANTS)
print(result)
```

## Conclusion 🚀

This program provides a helpful tool for identifying words with similar vowel patterns, which can be useful in word games or language learning scenarios where the structure of words is more important than the specific vowels used.
