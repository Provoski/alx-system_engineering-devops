#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import json
import requests
import sys


def export_to_json(userId):
    """declearing my tasks counter variables"""
    new_json_dict = {}
    json_file = "{}.json".format(userId)
    """api url"""
    api_link = "https://jsonplaceholder.typicode.com/"
    """todo url"""
    todo_url = "{}todos/".format(api_link)
    """employee url"""
    employee_url = "{}users/{}".format(api_link, userId)
    """employeeid parameter to be past to get request"""
    employeeId = {"userId": userId}
    """todo request"""
    todo_response = requests.get(todo_url, params=employeeId)
    """converting todo_respose to json format"""
    todo_data = todo_response.json()
    """employee request"""
    employee_response = requests.get(employee_url)
    """converting employee_response to json format"""
    employee_data = employee_response.json()
    employee_id = employee_data.get("id")
    employee_username = employee_data.get("username")

    new_json_dict[str(employee_id)] = []
    for todo in todo_data:
        task_info = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_username
            }
        new_json_dict[str(employee_id)].append(task_info)
    with open(json_file, 'w') as f:
        json.dump(new_json_dict, f)


if __name__ == "__main__":
    """program entry point"""
    userid = sys.argv[1]
    export_to_json(userid)
