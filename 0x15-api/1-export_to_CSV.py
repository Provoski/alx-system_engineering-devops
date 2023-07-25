#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import csv
import requests
import sys


def export_to_csv(userId):
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
    employee_username = employee_data.get("username")
    """opening the csv file to write to"""
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            """writing to csv file"""
            writer.writerow([
                                str(employee_id),
                                employee_username,
                                todo["completed"],
                                todo["title"]
                                ])


if __name__ == "__main__":
    """program entry point"""
    userid = int(sys.argv[1])
    export_to_csv(userid)
