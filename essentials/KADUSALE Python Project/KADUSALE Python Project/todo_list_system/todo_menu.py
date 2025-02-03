# To-do list main menu of the program
# Imports the json and sys modules
import sys

def todo_mainmenu(): # Main menu of the to-do list program

    while True:
        # Prints the options that can be selected by the user
        print("\n☆☆☆☆☆☆☆☆ TO-DO LIST PROGRAM ☆☆☆☆☆☆☆☆")
        print("\nPlease select an option below:")
        print("[1] Manage Tasks")
        print("[2] Categorize Tasks")
        print("[3] Exit")

        # The user's choice will be collected in the user_choice variable
        user_choice = input("\nYour choice: ")

        if user_choice == "1": # Directs the user to the task management section
            from todo_list_system.todo_manage import todo_manage
            todo_manage() # Allows the user to manage his/her task
        elif user_choice == "2": # Directs the user to the task categorization section
            from todo_list_system.todo_categorize import todo_categorize
            todo_categorize() # Lets the user categorize his/her selected tasks
        elif user_choice == "3": # Exits the program
            from user_authentication.login_function import username
            print(f"\nThank you for using the program, {username}. Goodbye!")
            sys.exit() # Program ends. User automatically logs out
        else: # Else, the program asks the user to enter appropriate input
            print("\nInvalid input! Please try again.")
        