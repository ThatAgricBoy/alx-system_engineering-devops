#!/usr/bin/python3
"""Python Script to export data in CSV format"""
import csv
from requests import get
from sys import argv


def exportCsv(user):
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    employee_data = open('{}.csv'.format(user), 'w')
    cwrite = csv.writer(employee_data, quoting=csv.QUOTE_ALL)
    for line in data:
        lined = [line.get('userId'), name,
                 line.get('completed'), line.get('title')]
        cwrite.writerow(lined)
    employee_data.close()


if __name__ == "__main__":
    exportCsv(argv[1])
