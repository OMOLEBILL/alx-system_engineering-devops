#!/usr/bin/python3
"""Gets employee details"""

from requests import get
from sys import argv


if __name__ == "__main__":
    site_url = "https://jsonplaceholder.typicode.com"
    # get user's todos
    todos_url = site_url + "/user/{}/todos".format(argv[1])
    user_todo = get(todos_url).json()
    # get user's info such as name
    user_url = site_url + "/users/{}".format(argv[1])
    user_dits = get(user_url).json()

    username = user_dits.get("name")
    total_tasks = len(user_todo)
    completed_task_titles = [user.get("title")
                             for user in user_todo if user.get("completed")]
    completed_tasks = len(completed_task_titles)
    message = "Employee {} is done with tasks({}/{}):".format(
        username, completed_tasks, total_tasks)
    print("{}".format(message))
    for todo in completed_task_titles:
        print("\t {}".format(todo))
