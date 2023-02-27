#!/usr/bin/python3
"""This modules gets the number of subscribers of a
given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """args a subrediit name
    return the no of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                       (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        number = data.get("data").get("subscribers")
        return number
    return 0
