# Mobile Keypad Keystrokes Encoder 📱

## Description 📝

This program simulates the process of typing a message on an old push-button mobile phone.
It converts each letter of the given message into the corresponding keystrokes on the mobile keypad.
Each key on the keypad has multiple letters associated with it, and the number of keystrokes varies depending on which character is being typed.

## Purpose 🎯

The purpose of this program is to display the sequence of keystrokes required to type a given message on a traditional mobile phone keypad.

## How It Works 🔍

1. **Input**:
    - The user enters a message, which can include letters, numbers, and punctuation.
2. **Processing**:
    - The program checks each character of the message and determines how many times each corresponding number on the keypad needs to be pressed.
    - Uppercase and lowercase letters are treated the same.
3. **Output**:
    - The program outputs a string of keystrokes corresponding to the entered message.

## Output 📜

The program outputs a sequence of digits, each digit repeated a certain number of times depending on the character typed.

### Example:

**Input**:

```
Enter your message: Hello World
```

**Output**:

```
443355555566611096667775553
```

### Explanation:

-   H -> `4` (2nd letter on key 4)
-   E -> `3` (1st letter on key 3)
-   L -> `5` (3rd letter on key 5)
-   L -> `5` (3rd letter on key 5)
-   O -> `6` (3rd letter on key 6)
-   W -> `9` (1st letter on key 9)
-   O -> `6` (3rd letter on key 6)
-   R -> `7` (3rd letter on key 7)
-   L -> `5` (3rd letter on key 5)
-   D -> `3` (1st letter on key 3)

## Usage 📦

1. Save the code in a Python file, e.g., `keypad_keystrokes.py`.
2. Run the script.
3. Input your desired message when prompted.
4. The program will output the corresponding keystrokes for the message.

### Example Run:

```plaintext
Enter your message: Hello World
Output: 443355555566611096667775553
```

## Conclusion 🚀

This program simulates the keypresses required to type a message on an old mobile keypad, supporting both uppercase and lowercase characters, and ignoring any invalid characters.
