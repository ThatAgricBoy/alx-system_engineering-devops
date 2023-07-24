#!/usr/bin/env python3
"""Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""
import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todos_url = f'{base_url}todos?userId={employee_id}'

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch TODOs for the employee
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Count completed tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Print the progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid JSON data received.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
