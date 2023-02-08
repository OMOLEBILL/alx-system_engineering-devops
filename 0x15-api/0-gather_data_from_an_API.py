#!/usr/bin/python3
"""this module fetche info"""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    url_todo = url + "users/{}/todos".format(sys.argv[1])
    dic = requests.get(url_todo)

    url_users = url + "users/{}".format(sys.argv[1])
    dic1 = requests.get(url_users)
    todo = dic.json()
    username = dic1.json().get("name")
    lens = len(todo)

    tasks = [user.get("title")
             for user in todo if user.get("completed")]
    print(f"Employee {username} is done with tasks({len(tasks)}/{lens}):")
    for i in tasks:
        print('\t {}'.format(i))
