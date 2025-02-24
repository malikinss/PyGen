'''
TODO:
    You have access to a program that finds the sum of all values for the
    Likes key from all dictionaries in the blog_posts list.

    If the dictionary does not contain the Likes key, its value is considered
    to be minus one.

    Add a try-except statement to the code below so that it runs
    without errors.
'''
blog_posts = [
    {'Photos': 3, 'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Photos': 8, 'Comments': 1, 'Shares': 1},
    {'Photos': 3, 'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

print(total_likes)
