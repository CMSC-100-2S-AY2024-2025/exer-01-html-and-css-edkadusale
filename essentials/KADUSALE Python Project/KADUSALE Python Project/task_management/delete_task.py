# Imports the username variable from login_function module and the json module
from user_authentication.login_function import username
import json

# Function that allows the user to delete task(s) of his/her choice
def deletetask_function():
    try:
        # Tries to open and load the information inside the json file
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "r") as file:
            tasks = json.load(file)
            if tasks:
                # If tasks are present in the file, the program will ask the user which task to delete
                print("\n-----TASKS TO DELETE-----")
                print("\nSelect the task that you want to delete")
                # Loop that will show the available tasks inside the file
                for i, task in enumerate(tasks, 1):
                    print(f"TASK [{i}]: {task['title']}") # Shows the task number and its title
                
                # An option which deletes the entire content (all tasks) of the file 
                print("Enter 'all' to delete all tasks.")

                # User's choice
                task_choice = input("\nEnter the task number to delete or 'exit' to exit: ")
                
                # If the user chooses to exit, he/she will be redirected to the to-do main menu
                if task_choice.lower() == 'exit':
                    from todo_list_system.todo_menu import todo_mainmenu # Imports the to-do menu function
                    todo_mainmenu()  # Calls the to-do menu function
                # If the user chooses 'all', all tasks will be deleted
                elif task_choice.lower() == 'all':
                    deleted_tasks = tasks
                    tasks = [] # The contents will be replaced by an empty list 
                    with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "w") as file:
                        json.dump(tasks, file) # Saves the updated tasks data to the json file
                    print("\nAll tasks deleted successfully.") 
                else:
                    # A task will be deleted based on the user's inputted number 
                    task_index = int(task_choice) - 1
                    if task_index >= 0 and task_index < len(tasks):
                        # Checks if the task index is within the valid range
                        deleted_task = tasks.pop(task_index) # Removes the task at the specified index and retrieve its details
                        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "w") as file:
                            json.dump(tasks, file) # Saves the updated tasks data to the json file
                        print(f"\nTask '{deleted_task['title']}' deleted successfully.")
                    else:
                        # If the task index is out of range, i.e., an invalid task number is provided
                        print("\nInvalid task number.")
            else:
                # If the json file is empty, the message below occurs
                print("\nNo tasks found.")
    except FileNotFoundError:
        # If the json file is empty, the message below occurs
        print("\nNo tasks found.")
