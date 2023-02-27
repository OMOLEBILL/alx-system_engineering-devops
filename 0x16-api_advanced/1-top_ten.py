#!/usr/bin/python3
"""We get the top 10 titles of post from a subreddit"""
import requests


def top_ten(subreddit):
    """ args: names of the subredit
        prints the 1st 10 tittles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=header)
    if response.status_code == 404:
        print("None")
        return
    data = response.json()
    for i in range(10):
        title = data['data']['children'][i]['data']['title']
        print(title)
