# Imports the variable username and json module
from user_authentication.login_function import username
import json

def categorize_tasks_by_user(): # RFunction that lets user categorize their tasks
    try:
        # Loads the tasks from username-tasks.json
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "r") as file:
            tasks = json.load(file)
        # If tasks exist in the json file
        if tasks:
            # Empty dictionary to store categorized tasks
            categorized_tasks = {}
            # For each task in the set of tasks
            for task in tasks:
                # Retrieves the title of the current task and assign it to the variable 'user'
                user = task["title"] 
                if user in categorized_tasks: 
                    # If the user already exists as a key in the categorized_tasks dictionary
                    categorized_tasks[user].append(task)
                else:
                    # If the user does not exist as a key in the categorized_tasks dictionary
                    categorized_tasks[user] = [task]
            while True:
                # Prompts the user to enter a category name
                category_name = input("\nEnter the category name (or type 'exit' to finish): ")
                if category_name == 'exit':
                    break

                # Prompts the user to choose the tasks to categorize
                print("\n------ LIST OF TASKS ------")
                for i, task in enumerate(tasks, 1):
                    print(f"TASK {i}: {task['title']}")
                chosen_tasks = input("\nEnter the task numbers to categorize (separated by commas): ").split(",")
                chosen_tasks = [int(task.strip()) for task in chosen_tasks]

                # Creates a new list to hold the categorized tasks
                selected_tasks = []

                # For each task number in the chosen_tasks list
                for task_number in chosen_tasks:
                    # Checks if the task number is within the valid range
                    if 1 <= task_number <= len(tasks):
                        # Appends the task with the corresponding task number to the selected_tasks list
                        selected_tasks.append(tasks[task_number - 1])

                # Loads existing categories from username-categories.json
                try:
                    # Attempts to open the categories file for the current user
                    with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_categories_folder/{username}-categories.json", "r") as categories_file:
                        # Loads the categories from the file and assign them to the 'categories' dictionary
                        categories = json.load(categories_file)
                except FileNotFoundError:
                    # If the categories file does not exist, create an empty 'categories' dictionary
                    categories = {}

                # Adds the category and its tasks to the dictionary
                categories[category_name] = selected_tasks 

                # Writes the updated categories dictionary to the categories file
                with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_categories_folder/{username}-categories.json", "w") as file:
                    json.dump(categories, file)

                # Prints a success message
                print(f"\nTasks categorized by user in '{username}-categories.json' successfully for category '{category_name}'.")
        else:
            # No tasks found
            print("\nNo tasks found.")
    except FileNotFoundError:
        # No tasks found
        print("\nNo tasks found.")
