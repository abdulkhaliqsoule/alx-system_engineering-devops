#!/usr/bin/python3
"""Export to CSV"""
import csv
from requests import get
from sys import argv


def csv_write(user):
    """writes to csv"""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    employ_data = open('{}.csv'.format(user), 'w')
    cwrite = csv.writer(employ_data, quoting=csv.QUOTE_ALL)
    for record in data:
        row = [record.get('userId'), name,
                 record.get('completed'), record.get('title')]
        cwrite.writerow(row)
    employ_data.close()


if __name__ == "__main__":
    csv_write(argv[1])
