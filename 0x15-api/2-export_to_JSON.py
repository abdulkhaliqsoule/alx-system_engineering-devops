#!/usr/bin/python3
"""Export to JSON"""
import json
from requests import get
from sys import argv


def json_write(user):
    """writes to csv"""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    ordered = []
    for record in data:
        ordered.append({"task": record.get('title'), "completed":
                        record.get('completed'), "username": name})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: ordered}, f)


if __name__ == "__main__":
    json_write(int(argv[1]))
