#!/usr/bin/python3
""" We get the hotlist recursively """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """args subreddit -the subreddit
            hot_list - the list to be returned
            after pagnation used to got to the next page
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json()['data']
    after = data['after']
    if after:
        recurse(subreddit, hot_list, after)
    posts = data['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['after']
    return hot_list
