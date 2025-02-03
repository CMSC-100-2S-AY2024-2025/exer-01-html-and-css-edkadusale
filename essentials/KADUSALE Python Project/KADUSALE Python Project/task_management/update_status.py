# Imports the username variable from login function and json module
from user_authentication.login_function import username
import json

def load_tasks(): # Function for loading the tasks
    try:
        # Attempts to open and load tasks from the user-specific tasks json file
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        # If the file is not found, initialize an empty list for tasks
        tasks = []
    return tasks

def save_tasks(tasks): # Function for saving tasks
    # Saves the tasks list to the user-specific tasks file
    with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "w") as file:
        json.dump(tasks, file)

def updatestatus_task(): # Function for updating the status of a task
    # Loads tasks from the file
    tasks = load_tasks()

    # Checks if there are any tasks
    if not tasks: # If not, then message below appears
        print("\nNo tasks found.")
        return

    print("\nCHOOSE TITLE BELOW") # If there are tasks then
    # Program displays the titles and statuses of the tasks
    for i, task in enumerate(tasks, 1):
        print(f"TASK {i}: {task['title']} ({task['status']})")

    # Prompts the user to enter the title of the task to update
    task_title = input("\n[A] Enter the title of the task you want to update the status for: ")

    while True:
        # Prompts the user to enter the new status
        new_status = input("[B] Enter the new status ('done' or 'not done'): ")
        if new_status.lower() == 'done' or new_status.lower() == 'not done': # Checks if the user entered the right input
            break
        else:
            # Else, the user entered an invalid input
            print("\nInvalid input. Please enter either 'done' or 'not done'.")

    # Found_task with initial value of false
    found_task = False

    # Finds the task with the matching title and updates its status
    for task in tasks:
        if task["title"] == task_title:
            task["status"] = new_status
            found_task = True
            break

    if found_task:
        # Saves the updated tasks to the file
        save_tasks(tasks)
        print("\nTask status updated successfully.")
    else:
        # If the task is not present in the file
        print("\nTask not found.")
