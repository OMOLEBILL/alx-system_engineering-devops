#!/usr/bin/python3
"""This modules gets the number of subscribers of a
given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """args a subrediit name
    return the no of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        number = data.get("data").get("subscribers")
        return number
    return 0
