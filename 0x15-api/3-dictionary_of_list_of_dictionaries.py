#!/usr/bin/python3
'''JSON format'''
import json
import requests


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


def get_todos():
    '''Get the data from the API'''
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching todos data from API")
        exit(1)


def write_to_json(todos):
    '''Write todos data to a JSON file'''
    file_name = "todo_all_employees.json"
    my_dict = {}
    user_id = 0
    for todo in todos:
        todo_dict = {}
        todo_list = []
        user_id = todo.get("userId")
        for key, value in todo.items():
            if key == 'title':
                todo_dict['task'] = value
            elif key == 'completed':
                todo_dict['completed'] = value
        todo_dict['username'] = get_user_name(user_id)
        todo_list.append(todo_dict)
        my_dict[user_id] = todo_list
    with open(file_name, "w") as jsonfile:
        json.dump(my_dict, jsonfile, indent=4)


if __name__ == "__main__":
    todos = get_todos()
    write_to_json(todos)
