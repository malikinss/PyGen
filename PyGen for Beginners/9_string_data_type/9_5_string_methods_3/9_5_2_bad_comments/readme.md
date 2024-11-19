# Stepik Comment Validator 📝

## Description 📝

This program helps moderators on the Stepik platform by checking if users' comments are appropriate. It removes comments that are either empty or consist only of spaces.

## Purpose 🎯

To assist moderators in cleaning up unnecessary or inappropriate comments and keep the course content relevant.

## How It Works 🔍

1. The program receives an integer `n` which represents the number of comments.
2. For each comment:
    - If the comment is empty or contains only spaces, it is marked as "COMMENT SHOULD BE DELETED".
    - Otherwise, the program prints the comment's index followed by its content.
3. The result is printed for each comment with either the original text or the deletion notice.

## Output 📜

-   Each comment is printed with its number followed by its content, or "COMMENT SHOULD BE DELETED" if it doesn't meet the standards.

## Usage 📦

1. Input the number of comments `n`.
2. Input `n` lines representing the comments.
3. The program will check each comment and display either its content or a deletion message.

### Example 1:

**Input:**  
`3`  
`Hello, nice course!`  
`     `  
`Great explanation!`

**Output:**  
`1: Hello, nice course!`  
`2: COMMENT SHOULD BE DELETED`  
`3: Great explanation!`

### Example 2:

**Input:**  
`2`  
` `  
`Valid comment here!`

**Output:**  
`1: COMMENT SHOULD BE DELETED`  
`2: Valid comment here!`

## Conclusion 🚀

This program provides an easy way to ensure comments on Stepik remain meaningful and relevant by detecting and removing inappropriate comments.
