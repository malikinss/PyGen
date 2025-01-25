# Random Password Generator with Constraints

## Description 📝

This program generates a specified number of random passwords of a given length.
The passwords consist of lowercase and uppercase English letters, as well as digits, but exclude certain characters that are easily confused with others, such as "l", "I", "1", "o", "O", and "0".
Additionally, each password must contain at least one number, one lowercase letter, and one uppercase letter.

## Purpose 🎯

The program's purpose is to generate secure passwords that meet specific requirements, avoiding confusing characters and ensuring diversity in the password structure (with at least one digit, one lowercase, and one uppercase letter).

## How It Works 🔍

1. The program first excludes characters that are easily confused (e.g., "l", "I", "1", "o", "O", "0").
2. It then generates passwords of the specified length, ensuring each password contains at least one lowercase letter, one uppercase letter, and one digit.
3. The program shuffles the password characters to randomize the order.
4. It generates the requested number of passwords and prints each one on a new line.

## Output 📜

The program will output `n` passwords, each consisting of `m` characters. The characters are drawn from a set of lowercase and uppercase English letters and digits, excluding confusing characters.

Example output:

```
f2Mw6Bq9
zQ5j3Rs8
B7vT5uAx
...

```

## Usage 📦

1. Run the program.
2. Enter the number of passwords (`n`) to generate.
3. Enter the length (`m`) of each password.
4. The program will print the generated passwords.

Example usage:

```bash
Enter number of passwords: 5
Enter length of passwords: 8
f2Mw6Bq9
zQ5j3Rs8
B7vT5uAx
...
```

## Conclusion 🚀

This password generator ensures that the passwords are secure and easy to read by excluding commonly confused characters and meeting the requirements of having at least one digit, one uppercase letter, and one lowercase letter.
It's perfect for generating strong passwords for various use cases.
