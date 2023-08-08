#!/usr/bin/python3
"""a function that queries the Reddit API and prints
the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints
the titles of the first 10 hot posts """
    user_agent = "MyRedditBot/1.0"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"][:10]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    elif response.status_code == 404:
        print("None")
    else:
        print(f"Error: {response.status_code}")
        print("None")
