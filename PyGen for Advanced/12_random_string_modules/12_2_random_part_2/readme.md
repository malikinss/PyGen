# Lesson 12.2: Random Module (Part 2) 📚

## Description 📝

This lesson focuses on advanced methods of working with sequences in Python's `random` module.
It covers the methods `shuffle()`, `choice()`, and `sample()`, as well as how to apply them to various real-world problems.
The lesson consists of 9 practical tasks that help solidify my understanding of randomness in different contexts, such as generating IP addresses, lottery tickets, and passwords.

## Purpose 🎯

The purpose of this lesson is to deepen your understanding of the `random` module, specifically in the context of sequence manipulation.
I will learn how to shuffle, sample, and make random selections from sequences, which are common tasks in simulations, games, and security applications.

## Tasks 📜

### 1. 12_2_1 Generate IP Address 🌐

This program generates a random valid IP address consisting of four numbers, each ranging from 0 to 255, separated by periods.
The purpose of this program is to simulate the generation of random, valid IP addresses that are used in various network-related applications.

### 2. 12_2_2 Generate Postal Code for Latveria 🇱🇻

This program generates a random valid postal code for Latveria. The postal code follows the format:

-   `LetterLetterNumber_NumberLetterLetter`

Where:

-   `Letter` is a capital letter from the English alphabet (A-Z).
-   `Number` is a number between 0 and 99 (inclusive).
-   An underscore (`_`) separates the number segments.
    The purpose of this program is to generate random postal codes for Latveria that conform to a specified format, which may be useful for simulations or testing.

### 3. 12_2_3 Shuffle Matrix 🔀

This program randomly shuffles the contents of a two-dimensional list (matrix).
The matrix is shuffled both row-wise (shuffling each row individually) and overall (shuffling the rows themselves).
The purpose of this program is to demonstrate how to randomly shuffle a matrix, which can be useful for simulations, randomization tasks, or game development.

### 4. 12_2_4 Generate Lottery Tickets 🎟️

This program generates 100 unique 7-digit lottery ticket numbers using the `random` module.
Each ticket number is randomly generated between 1,000,000 and 9,999,999 and ensures that no ticket number starts with zero.
The generated numbers are guaranteed to be unique.
The program's main purpose is to generate and output 100 unique lottery ticket numbers.
This can be useful in simulations, lotteries, or as a part of larger systems requiring random unique identifiers.

### 5. 12_2_5 Generate Anagram 🔠

This program takes a word as input and generates a random anagram of that word by rearranging its letters using the `random` module.
The program allows users to input a word and get a randomly shuffled version of it (an anagram).
This is useful for games, puzzles, or learning how to manipulate strings in Python.

### 6. 12_2_6 Generate Bingo Card 🎲

This program generates a random Bingo card for the "Super Bingo" lotto game.
The card consists of 25 cells with unique numbers between 1 and 75, and the center cell is marked as empty (0).
The program ensures that all numbers are unique and formats the card for display.
The program simulates a Bingo card for use in online Bingo games or for fun, educational activities.
It ensures the correct number of cells, uniqueness of numbers, and proper formatting.

### 7. 12_2_7 Print Student Secret Friends 🤫

This program randomly assigns each student a secret friend who will work with them on programming problems.
The program ensures that no one is assigned to themselves and that each student only has one secret friend.
The main purpose of this program is to facilitate a "secret friend" assignment for students, where each student is paired with another randomly.
It ensures fairness by making sure no one is paired with themselves.

### 8. 12_2_8 Generate Passwords 🔑

This program generates a specified number of random passwords of a given length.
The passwords consist of lowercase and uppercase English letters, as well as digits, but exclude certain characters that are easily confused with others, such as "l", "I", "1", "o", "O", and "0".
The main purpose of this program is to generate strong passwords that avoid easily confused characters, making them more secure and user-friendly.

### 9. 12_2_9 Generate Passwords with Constraints 🔐

This program generates a specified number of random passwords of a given length.
The passwords consist of lowercase and uppercase English letters, as well as digits, but exclude certain characters that are easily confused with others, such as "l", "I", "1", "o", "O", and "0".
Additionally, each password must contain at least one number, one lowercase letter, and one uppercase letter.
The program's purpose is to generate secure passwords that meet specific requirements, avoiding confusing characters and ensuring diversity in the password structure (with at least one digit, one lowercase, and one uppercase letter).

## Conclusion 🚀

By completing this lesson, I will gain practical experience using advanced methods in the `random` module to manipulate sequences.
These tasks are widely applicable in scenarios such as games, simulations, and security applications.
Mastering these techniques will enhance my ability to handle randomness effectively in Python.
