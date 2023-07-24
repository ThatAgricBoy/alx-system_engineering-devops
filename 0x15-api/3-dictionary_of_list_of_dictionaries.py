#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import json
from requests import get
from sys import argv


def jsonWrite():
    data = get('https://jsonplaceholder.typicode.com/users').json()
    ids = [(dic.get('id'), dic.get('username')) for dic in data]
    dumped = {}
    for person in ids:
        data = get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                person[0])).json()
        ordered = [{"task": line.get('title'), "completed":
                    line.get('completed'), "username":
                    person[1]} for line in data]
        dumped[person[0]] = ordered
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dumped, f)


if __name__ == "__main__":
    jsonWrite()
