# BEEGEEK Popularity Score Counter

## Description 📝

This program evaluates the popularity of the **BEEGEEK** online school by analyzing social media posts.
Each post is assigned a score based on occurrences of the word `"beegeek"` in lowercase.

## Purpose 🎯

The goal of this program is to assess the influence of **BEEGEEK** in social media posts by summing up the points given based on predefined scoring criteria.

## How It Works 🔍

1. **Input**:

    - The program takes multiple lines as input, each representing a post.

2. **Scoring Rules**:

    - **3 points** if the post **begins and ends** with `"beegeek"`.
    - **2 points** if the post **starts or ends** with `"beegeek"`.
    - **1 point** if `"beegeek"` appears **inside** the text.
    - **0 points** if `"beegeek"` is **absent**.

3. **Regular Expressions**:

    - `r'^beegeek$|^beegeek.*beegeek$'` → **3 points** (both start and end with `"beegeek"`)
    - `r'^beegeek.*$|^.*beegeek$'` → **2 points** (either starts or ends with `"beegeek"`)
    - `r'beegeek'` → **1 point** (occurs somewhere in the text)

4. **Output**:
    - The total score of all posts is printed.

## Output 📜

### Example Input:

```text
beegeek is amazing!
beegeek is the best beegeek
I love beegeek
beegeek
the word beegeek is here
```

### Example Output:

```text
10
```

## Usage 📦

1. Save the script in a file, e.g., `beegeek_popularity.py`.
2. Run the script in the terminal.
3. Enter multiple lines of input.
4. The program will calculate the total popularity score and output the result.

## Conclusion 🚀

This program efficiently calculates the **BEEGEEK** popularity score using **regular expressions**.
It can be useful for tracking trends, analyzing brand mentions, or measuring engagement levels across various platforms.
