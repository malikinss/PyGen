# Random Password Generator 🔐

## Description 📝

This program generates a random password of a specified length using only English alphabet characters.
The password can contain both uppercase (`A..Z`) and lowercase (`a..z`) letters.

## Purpose 🎯

The program demonstrates the generation of random passwords, which can be useful for creating secure credentials or testing password generation logic.

## How It Works 🔍

1. **Input**:

    - The user specifies the desired length of the password.

2. **Processing**:

    - For each character in the password:
        - A random decision determines whether it will be an uppercase or lowercase letter.
        - A random ASCII value is generated:
            - `A..Z` (65–90 in ASCII).
            - `a..z` (97–122 in ASCII).
        - The `chr()` function converts the ASCII value to a character.
    - The characters are combined into a single password string.

3. **Output**:
    - The generated password is displayed.

## Output 📜

The program outputs a randomly generated password containing a mix of uppercase and lowercase letters.

### Example Input/Output:

**Input**:

```
Enter the desired password length: 10
```

**Output**:

```
aDfGjLpQrX
```

### Explanation:

-   The user requested a password of 10 characters.
-   The program generated a password with a mix of randomly chosen uppercase and lowercase letters.

## Usage 📦

1. Copy the code into a Python file (e.g., `password_generator.py`).
2. Run the script and input the desired password length when prompted.
3. View the generated random password.

### Example Run:

```python
# Input:
Enter the desired password length: 12

# Output:
pQaZrLmTyWuX
```

## Conclusion 🚀

This program is a simple and effective way to generate random passwords consisting only of alphabetic characters.
It can be further extended to include numbers, special characters, or other requirements for a more robust password.
