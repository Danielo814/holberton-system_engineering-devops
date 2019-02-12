#!/usr/bin/python3
"""
uses a REST API for a given employee Id, returns information
about his/her TODO list progress
"""
import sys
import requests

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    employee = user.get('name')
    completed = 0
    lst_completed = []
    for task in tasks:
        if task.get('completed'):
            completed += 1
            lst_completed.append("\t {}".format(task.get('title')))
    print("Employee {} is done with tasks({}/{})"
          .format(employee, completed, len(tasks)))
    for i in lst_completed:
        print("{}".format(i))
