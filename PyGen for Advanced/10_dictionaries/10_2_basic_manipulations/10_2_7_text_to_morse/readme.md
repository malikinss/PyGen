# Text to Morse Code Encoder 🔠➡️📡

## Description 📝

This program converts a given text message into Morse code.
It takes a message, processes it by translating each character into its Morse code equivalent, and outputs the encoded message.
The program ignores the case of the characters and any characters not listed in the Morse code table.

## Purpose 🎯

The purpose of this program is to allow users to input a text message and receive the corresponding Morse code translation.
This can be useful for learning or using Morse code for communication.

## How It Works 🔍

1. **Input**:
    - The user enters a text message.
2. **Processing**:
    - The message is converted to uppercase, and each character is translated into its corresponding Morse code.
    - Invalid characters (i.e., characters not listed in the Morse code table) are ignored.
3. **Output**:
    - The program outputs the translated Morse code as a string of dots and dashes, separated by spaces.

## Output 📜

The program outputs the Morse code translation of the input message, with each Morse code symbol separated by a space.

### Example:

**Input**:

```
Enter your message: Hello
```

**Output**:

```
.... . .-.. .-.. ---
```

### Explanation:

-   H -> `....`
-   E -> `.`
-   L -> `.-..`
-   L -> `.-..`
-   O -> `---`

Thus, the Morse code for "Hello" is `.... . .-.. .-.. ---`.

## Usage 📦

1. Save the code in a Python file, e.g., `text_to_morse.py`.
2. Run the script.
3. Input your desired message when prompted.
4. The program will output the corresponding Morse code.

### Example Run:

```plaintext
Enter your message: SOS
Output: ... --- ...
```

## Conclusion 🚀

This program offers an easy and simple way to convert text messages into Morse code, supporting letters, numbers, and ignoring invalid characters. It provides a fun way to explore this classic encoding system.
