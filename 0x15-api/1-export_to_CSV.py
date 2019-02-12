#!/usr/bin/python3
"""
uses a REST API for a given employee Id, returns information
about his/her TODO list progress
"""
import sys
import requests
import csv


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    username = user.get('username')
    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([sys.argv[1], username, task.get('completed'),
                             task.get('title')])
