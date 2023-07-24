#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import csv
import requests
import sys


def gather_data_from_api(userId):
    """declearing my tasks counter variables"""
    csv_file = "{}.csv".format(userid)
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
    """storing employee neeeded data"""
    employee_id = employee_data.get("id")
    employee_name = employee_data.get("name")
    """opening the csv file to write to"""
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            if todo["completed"]:
                completed = "True"
            else:
                completed = "False"
            """writing to csv file"""
            writer.writerow([
                                employee_id,
                                employee_name,
                                completed,
                                todo["title"]
                                ])


if __name__ == "__main__":
    """program entry point"""
    userid = sys.argv[1]
    gather_data_from_api(userid)
