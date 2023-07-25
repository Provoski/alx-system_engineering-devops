#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import json
import requests


def all_users():
    """declearing my tasks counter variables"""
    new_json_dict = {}
    json_file = "todo_all_employees.json"
    """api url"""
    api_link = "https://jsonplaceholder.typicode.com/"
    """todo url"""
    todo_url = "{}todos/".format(api_link)
    """employee url"""
    all_employee_url = "{}users/".format(api_link)
    """employee request"""
    all_employee_response = requests.get(all_employee_url)
    """converting employee_response to json format"""
    all_employee_data = all_employee_response.json()

    for employee in all_employee_data:
        new_json_dict[str(employee["id"])] = []
        employeeId = {"userId": employee["id"]}
        todo_response = requests.get(todo_url, params=employeeId)
        todo_data = todo_response.json()
        for todo in todo_data:
            task_info = {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": employee['username']
                }
            new_json_dict[str(employee["id"])].append(task_info)
    with open(json_file, 'w') as f:
        json.dump(new_json_dict, f)


if __name__ == "__main__":
    """program entry point"""
    all_users()
