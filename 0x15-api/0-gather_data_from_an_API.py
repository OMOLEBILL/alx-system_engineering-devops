#!/usr/bin/python3
"""this module fetches info from the given url"""
from requests import get
from sys import argv

dic = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
dic1 = get("https://jsonplaceholder.typicode.com/users")
todo = dic.json()
users = dic1.json()
lens = len(todo)
user = todo[0].get("userId")

tasks = [todo[i]["completed"] for i in range(lens) if
         todo[i]["completed"] is True]
username = ""
for i in range(len(users)):
    if users[i].get("id") == user:
        username = users[i].get("name")
        break
print(f"Employee {username} is done with tasks({len(tasks)}/{lens}):")
for i in range(lens):
    print('\t', ' ', todo[i].get("title"))
