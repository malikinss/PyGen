# Random Password Generator

## Description 📝

This program generates a specified number of random passwords of a given length.
The passwords consist of lowercase and uppercase English letters, as well as digits, but exclude certain characters that are easily confused with others, such as "l", "I", "1", "o", "O", and "0".

## Purpose 🎯

The main purpose of this program is to generate strong passwords that avoid easily confused characters, making them more secure and user-friendly.

## How It Works 🔍

1. The program first excludes certain characters that are easily confused (e.g., "l", "I", "1", "o", "O", "0").
2. It then randomly generates the required number of passwords, each with the specified length, using the available characters.
3. Each password is printed on a new line.

## Output 📜

The program will output `n` passwords, each consisting of `m` characters. The characters are drawn from a set of lowercase and uppercase English letters and digits, excluding the characters that are easy to confuse.

Example output:

```
f9MnBk7z
V6HyqR5d
A2pV7jFq
...

```

## Usage 📦

1. Run the program.
2. Enter the number of passwords (`n`) to generate.
3. Enter the length (`m`) of each password.
4. The program will print the generated passwords.

Example usage:

```bash
Enter the number of passwords: 5
Enter the password length: 8
V6HyqR5d
A2pV7jFq
f9MnBk7z
...
```

## Conclusion 🚀

This password generator ensures that the passwords are secure and easy to read by excluding commonly confused characters.
It can be used to generate multiple random passwords for various use cases.
