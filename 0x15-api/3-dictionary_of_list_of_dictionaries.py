#!/usr/bin/python3
"""Gets employee details"""

import json
from requests import get


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # get user's todos
    todos_url = url + "/todos"
    user_todo = get(todos_url).json()
    user_url = url + "/users"
    username = get(user_url).json()
    namedic = {user.get("id"): user.get("username") for user in username}
    def lookup(x): return namedic[x] if x in namedic.keys() else None
    alllist = [{
        "tasks": user.get("title"),
        "completed": user.get("completed"),
        "username": lookup(user.get("userId"))} for user in user_todo]
    diction = {}
    diction[1] = alllist

    with open("todo_all_employees.json", "w") as f:
        json.dump(diction, f)
