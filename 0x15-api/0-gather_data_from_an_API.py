#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import json
import request


def gather_data_from_api(userId):
    """declearing my tasks counter variables"""
    total_tasks = 0
    completed_tasks = 0
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
    """counting my total task and completed task"""
    for todo in todo_data:
        total_tasks = total_tasks + 1
        if todo["completed"]:
            completed_tasks = completed_tasks + 1
    print("Employee {} is done with tasks({}/{}):".format(
            employee_data["name"],
            completed_tasks,
            total_tasks
            ))
    for todo in todo_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))


if __name__ == "__main__":
    """program entry point"""
    import sys

    userid = sys.argv[1]
    gather_data_from_api(userid)
