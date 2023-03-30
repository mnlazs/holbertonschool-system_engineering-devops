#!/usr/bin/python3
"""return all the user description
"""
import sys
import requests

# Get employee ID from command-line argument
employee_id = int(sys.argv[1])

# Send GET request to API to get employee's todo list
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

# Raise an exception if API response is not successful
response.raise_for_status()

# Get todo list from API response
todos = response.json()

# Calculate number of completed tasks and total number of tasks
num_completed_tasks = sum(1 for todo in todos if todo['completed'])
total_tasks = len(todos)

# Get employee name from API response
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
response.raise_for_status()
employee_name = response.json()['name']

# Display progress information
print(f'Employee {employee_name} is done with {num_completed_tasks}/{total_tasks} tasks:')
for todo in todos:
    if todo['completed']:
        print(f'\t{todo["title"]}')
