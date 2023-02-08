#!/usr/bin/python3
"""this module fetches info from the given url"""
import requests
import sys

if __name__ == "__main__":
    dic = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".
                       format(sys.argv[1]))
    dic1 = requests.get("https://jsonplaceholder.typicode.com/users")
    todo = dic.json()
    users = dic1.json()
    lens = len(todo)
    user = todo[0].get("userId")

    tasks = [todo[i].get("completed") for i in range(lens) if
             todo[i].get("completed") is True]
    username = ""
    for i in range(len(users)):
        if users[i].get("id") == user:
            username = users[i].get("name")
            break
    print(f"Employee {username} is done with tasks({len(tasks)}/{lens}):")
    for i in range(lens):
        print('\t', ' ', todo[i].get("title"))
