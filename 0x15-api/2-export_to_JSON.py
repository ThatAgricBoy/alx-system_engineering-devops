#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import json
from requests import get
from sys import argv


def jsonWrite(user):
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    ordered = []
    for line in data:
        ordered.append({"task": line.get('title'), "completed":
                        line.get('completed'), "username": name})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: ordered}, f)


if __name__ == "__main__":
    jsonWrite(int(argv[1]))