# Imports the username variable from login function and json module
from user_authentication.login_function import username
import json

def viewtasks_function(): # Function that shows the tasks of the user
    try:
        # Attempts to open and load tasks from the user-specific tasks file
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "r") as file:
            task = json.load(file)
            if task: # If the json file is not empty, then the program shows the tasks
                print("\n------LIST OF TASKS------")
                # Iterates over each task and display its details/information
                for i, task in enumerate(task, 1):
                    print(f"\nTASK {i} ---------------")
                    print(f"Title: {task['title']}")
                    print(f"Description: {task['description']}")
                    print(f"Date: {task['date']}")
                    print(f"Time: {task['time']}")
                    print(f"ID: {task['id']}")
                    print(f"Status: {task['status']}")
                    print("**********************")
            else:
                # Otherwise, if the file is empty, no task is found
                print("\nNo tasks found.")
    except FileNotFoundError:
        # Message below occurs if the file contains no task
        print("No tasks found.")
