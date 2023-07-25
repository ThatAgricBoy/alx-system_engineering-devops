#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(API)).json()
    todos_res = requests.get('{}/todos'.format(API)).json()

    users_data = {
        str(user['id']): [
            {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            for todo in todos_res if todo['userId'] == user['id']
        ]
        for user in users_res
    }

    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
