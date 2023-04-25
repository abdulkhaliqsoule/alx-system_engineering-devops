#!/usr/bin/python3
""" Python script that, using a
REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    """Get employee name"""
    user_url = f"{url}users/{sys.argv[1]}"
    employee = requests.get(user_url).json()
    print(f"Employee {employee.get('name')} is done with tasks", end="")

    """Get employee to do list"""
    todo_url = f"{url}todos?userId={sys.argv[1]}"
    tasks = requests.get(todo_url).json()
    completed_tasks = []
    for task in tasks:
        if task.get('completed') is True:
            completed_tasks.append(task)

    print(f" ({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
