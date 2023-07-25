#!/usr/bin/python3
""" Python to get data from an API and convert to Json"""
import json
import requests
import sys


def get_user_data(user_id):
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + str(user_id)
    res = requests.get(url_to_user)
    user_data = res.json()

    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    task_list = []
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        task_list.append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": user_data.get('username')
        })

    return task_list


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    dict_data = {USER_ID: get_user_data(USER_ID)}

    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data[USER_ID], f, indent=4)
