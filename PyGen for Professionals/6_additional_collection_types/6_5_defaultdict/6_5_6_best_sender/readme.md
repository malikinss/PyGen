# Best Sender in Messages 📧

## Description 📝

The program calculates the sender with the most words in their messages.
If there are multiple senders with the same number of words, the one with the lexicographically greater name is returned.

## Purpose 🎯

✔ Identify the sender who has sent the most words in total.  
✔ In case of a tie, return the sender with the lexicographically larger name.

## Example Input

```python
messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
```

## Example Output 📜

```python
Sam Fisher
```

## Output Format

-   The output is the name of the sender who has sent the most words across all their messages.
-   If multiple senders have the same word count, the sender with the lexicographically greater name is chosen.

## Usage 📦

To use the program:  
1️⃣ Pass two lists: one containing messages and the other containing sender names.  
2️⃣ Call the `best_sender()` function to calculate and return the sender's name with the most words.  
3️⃣ The function will output the name of the sender with the largest number of words or the one with the lexicographically greater name in case of a tie.

### Run the script:

```bash
$ python best_sender.py
```

## Conclusion 🚀

This program efficiently determines the sender with the most words, handling ties by returning the lexicographically greater name.
