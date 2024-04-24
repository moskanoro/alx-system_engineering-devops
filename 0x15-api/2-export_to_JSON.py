#!/usr/bin/python3
'''JSON format'''
import json
import requests
from sys import argv


def validate_input(args):
    '''Validate the input'''
    if len(args) < 2:
        print("Usage: python3 fabfile.py <user_id>")
        exit(1)
    try:
        user_id = int(args[1])
        return user_id
    except ValueError:
        print(f"{args[1]} must be an integer")
        exit(1)


def get_user_name(user_id):
    '''Retrieve user name from API'''
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        user = response.json()
        return user.get("name")
    else:
        print("Error fetching user data from API")
        exit(1)


def get_todos(user_id):
    '''Get the data from the API'''
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching todos data from API")
        exit(1)


def write_to_json(todos, user_id, user_name):
    '''Write todos data to a JSON file'''
    file_name = f"{user_id}.json"
    my_dict = {}
    todo_list = []
    for todo in todos:
        todo_dict = {}
        for key, value in todo.items():
            if key == 'title':
                todo_dict['task'] = value
            elif key == 'completed':
                todo_dict['completed'] = value
        todo_dict['username'] = user_name
        todo_list.append(todo_dict)
    my_dict[user_id] = todo_list
    print(my_dict)
    with open(file_name, "w") as jsonfile:
        json.dump(my_dict, jsonfile, indent=4)


if __name__ == "__main__":
    user_id = validate_input(argv)
    user_name = get_user_name(user_id)
    todos = get_todos(user_id)
    write_to_json(todos, user_id, user_name))
