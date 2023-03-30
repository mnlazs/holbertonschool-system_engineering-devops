#!/usr/bin/python3
"""return all the user description
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos = response.json()
    
    total_tasks = len(todos)
    done_tasks = sum(todo['completed'] for todo in todos)
    employee_name = todos[0]['userId']
    
    print(f"Employee {employee_name} is done with {done_tasks}/{total_tasks} tasks:")
    
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")
            
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
