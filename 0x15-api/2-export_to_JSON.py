#!/usr/bin/python3
""" Python to get data from an API and convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """Documentation"""
    USER_DATA = res.json()
    USERNAME = USER_DATA.get('username')
    """Documentation"""
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
            "username": USERNAME
        })

    dict_data = {USER_ID: task_list}

    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f, indent=4)
