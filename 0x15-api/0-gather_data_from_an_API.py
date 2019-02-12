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
    EMPLOYEE_NAME = user.get('name')
    NUMBER_OF_DONE_TASKS = 0
    lst_completed = []
    for task in tasks:
        if task.get('completed'):
            NUMBER_OF_DONE_TASKS += 1
            lst_completed.append("\t {}".format(task.get('title')))
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in lst_completed:
        print("{}".format(i))
