#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 Gather data from an API
"""
from requests import get
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = argv[1]
    try:
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        response = get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        name = response.json().get('name')

        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
        response = get(url)
        response.raise_for_status()
        tasks = response.json()
        done_tasks = [task for task in tasks if task.get('completed')]
        done = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):"
              .format(name, done, len(tasks)))
        for task in done_tasks:
            print("\t{}".format(task.get('title')))
    except Exception as e:
        print("An error occurred:", e)
