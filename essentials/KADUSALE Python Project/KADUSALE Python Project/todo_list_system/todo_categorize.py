# Function that has access to the different options for task categorization

def todo_categorize():

    while True:
        # Options for the user 
        print("\n☆☆☆☆☆ ~'CATEGORIZE TASKS'~ ☆☆☆☆☆")
        print("\nPlease select one below:")
        print("[1] Categorize tasks")
        print("[2] Show categories with tasks")
        print("[3] Exit")
        
        # The user's choice will be collected in the user_choice variable
        choice_user = input("\nYour choice: ")

        if choice_user == "1": # Directs the user to categorize_tasks function
            from category_management.task_category import categorize_tasks_by_user
            categorize_tasks_by_user() # Lets the user categorize his/her tasks
        elif choice_user == "2": # Directs the user to show_categories function
            from category_management.show_categories import show_categories_and_tasks
            from user_authentication.login_function import username
            show_categories_and_tasks(username) # The function shows the categorized tasks the user created
        elif choice_user == "3": # Redirects back to to-do main menu
            from todo_list_system.todo_menu import todo_mainmenu
            todo_mainmenu()
        else: # Else, the program asks the user to enter appropriate input
            print("\nInvalid input! Please try again.")