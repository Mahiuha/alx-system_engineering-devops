#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    allUsers = 'https://jsonplaceholder.typicode.com/todos'
    user1 = 'https://jsonplaceholder.typicode.com/users'

    all_users = sessionReq.get(allUsers)
    user = sessionReq.get(user1)

    json_req = all_users.json()
    json_user = user.json()

    users = {}

    for one in json_user:
        taskList = []
        for task in json_req:
            taskDict = {"username": one.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            taskList.append(taskDict)
        users[one.get('id')] = taskList

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users, f)
