#!/usr/bin/python3
"""Gets employee details"""

import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # get user's todos
    todos_url = url + "/user/{}/todos".format(argv[1])
    user_todo = get(todos_url).json()
    # get user's name
    user_url = url + "/users/{}".format(argv[1])
    username = get(user_url).json().get("name")

    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for user in user_todo:
            writer.writerow([user.get("userId"), username,
                            user.get("completed"), user.get("title")])
