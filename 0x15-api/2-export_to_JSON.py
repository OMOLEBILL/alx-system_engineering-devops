#!/usr/bin/python3
"""Gets employee details"""

import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # get user's todos
    todos_url = url + "/user/{}/todos".format(argv[1])
    user_todo = get(todos_url).json()
    # get user's name
    user_url = url + "/users/{}".format(argv[1])
    username = get(user_url).json().get("username")

    alllist = [{
               "tasks": user.get("title"),
               "completed": user.get("completed"),
               "username": username} for user in user_todo]
    diction = {}
    diction[1] = alllist
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(diction, f)
