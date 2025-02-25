'''
TODO:
    You have access to a program that finds the sum of all values for the
    Likes key from all dictionaries in the blog_posts list.

    If the dictionary does not contain the Likes key, its value is considered
    to be minus one.

    Add a try-except statement to the code below so that it runs
    without errors.
'''


def calculate_total_likes(blog_posts: list) -> int:
    """
    Calculates the total sum of the 'Likes' values from all dictionaries in
    the given list.

    If the 'Likes' key is missing in any dictionary, its value is
    considered -1.

    Args:
        blog_posts (list): A list of dictionaries, each representing a
        blog post.

    Returns:
        int: The total sum of 'Likes' values, considering -1 for missing keys.
    """
    total_likes = 0

    for post in blog_posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            total_likes -= 1

    return total_likes


blog_posts = [
    {'Photos': 3, 'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Photos': 8, 'Comments': 1, 'Shares': 1},
    {'Photos': 3, 'Likes': 19, 'Comments': 3}
]

result = calculate_total_likes(blog_posts)
print(result)
