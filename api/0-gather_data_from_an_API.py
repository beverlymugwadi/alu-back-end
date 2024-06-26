#!/usr/bin/python3
import requests
import sys

def get_employee_todo_list(employee_id):
    """
    Retrieves and displays an employee's TODO list progress.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name", "Unknown Employee")
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task.get("completed"))

        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in todos_data:
            if task.get("completed"):
                print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
