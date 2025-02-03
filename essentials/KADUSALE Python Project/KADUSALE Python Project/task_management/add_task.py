# Imports necessary module and variable from other script
from user_authentication.login_function import username
import json

def addtask_function(todo_list):
    try:
        # Opens the tasks file and loads existing tasks from JSON file
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        # If the tasks file is not found, assign an empty list to tasks
        tasks = []

    while True:
        # Checks if the maximum number of tasks is reached
        if len(tasks) == 10:
            # Program reminds the user to only crfeate a maximum of 10 tasks
            print("\nYou cannot add more tasks. Maximum number of tasks reached.")
            break
        # Users input information for their task
        title = input("\nEnter task title or 'exit' to exit: ") # Title of the task
        if title.lower() == 'exit': # If the user chooses to ext
            from todo_list_system.todo_menu import todo_mainmenu
            todo_mainmenu() # The user will be redirected back to the to-do main menu

        # Description of the task
        description = input("Enter task description: ")

        # Date and time inputs automatically generates for the users
        from datetime import datetime

        current_date = datetime.now().date() # Date will be added to the task information
        formatted_date = current_date.strftime("%Y-%m-%d") # Formatted date
                
        current_time = datetime.now().time() # Time will be added to the task information
        formatted_time = current_time.strftime("%H:%M:%S %p") # Formatted time

        # Imports modules for unique ID generator function
        import random
        import string

        def generate_random_id(length): # Generates random ID function using length as paremeter
            # Defines the characters to choose from
            characters = string.ascii_letters + string.digits

            # Generates a random ID by randomly selecting characters from the defined set
            random_id = ''.join(random.choice(characters) for _ in range(length))
            return random_id

        # Generates a random ID with a length of 6
        random_id = generate_random_id(6) 

        # Task status 
        while True:
            # Asks the user the status of the task (done or not done)
            status = input("Enter task status ('done' or 'not done'): ")
            # If the input is either done or not done, program will proceed to the creation of task dictionary
            if status.lower() == 'done' or status.lower() == 'not done':
                break 
            else:
                # Else, the input is invalid and the program prints the message below
                print("\nInvalid status. Please choose either 'done' or 'not done'.")

        # Creates a new task dictionary with the following information contained in it
        task = {
            "title": title,
            "description": description,
            "date": formatted_date,
            "time": formatted_time,
            "id": random_id,
            "status": status.lower()
        }

        # Adds the task to the to-do list
        tasks.append(task)

        # Saves the updated to-do list to a json file
        save_todo_list(tasks)
        print("\nTask added successfully!")

        # Asks the user if they want to continue making a task
        choice = input("\nDo you want to continue adding tasks? (y/n): ")
        if choice.lower() != 'y':
            # If the user chooses not to, the program redirects him/her to to-do menu
            from todo_list_system.todo_menu import todo_mainmenu
            todo_mainmenu()

def save_todo_list(todo_list): # Function to save the to-do list
    # Save the to-do list to a JSON file
    with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder/{username}-tasks.json", "w") as file:
        json.dump(todo_list, file)


