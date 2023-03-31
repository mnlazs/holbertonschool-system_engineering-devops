#!/usr/bin/python3
"""
place holder
"""

if __name__ == "__main__":
    import requests
    import csv
    from sys import argv

    if len(argv) < 2:
        exit()

    # Get the employee name
    user_id = argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users?id={}".format(user_id)).json()[0]["username"]
    
    # Get the list of todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)).json()
    
    # Create a list to store todo items
    todo_list = []

    # Append the todo item to the list
    for todo in todos:
        todo_list.append([user_id, name, todo["completed"], todo["title"]])

    # Write the list of todo items to a CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(todo_list)
