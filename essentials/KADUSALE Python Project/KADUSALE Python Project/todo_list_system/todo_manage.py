# A function for all the options for managing the user's tasks

def todo_manage(): # To-do manage function

    while True:
        # Users can select an option below 
        print("\n☆☆☆☆☆ ~'MANAGE TASKS'~ ☆☆☆☆☆")
        print("\nPlease select one below:")
        print("[1] View all tasks")
        print("[2] Add tasks")
        print("[3] Delete tasks")
        print("[4] Update task status")
        print("[5] Exit")

        # The user's choice will be collected in the choice_user variable
        choice_user = input("\nYour choice: ")

        if choice_user == "1": # Directs the user to viewtasks_function
            from task_management.view_all_tasks import viewtasks_function
            viewtasks_function() # Allows the user to see all the tasks he/she created
        elif choice_user == "2": # Directs the user to addtask_function
            from task_management.add_task import addtask_function
            from user_authentication.login_function import username
            filename = f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/{username}"
            addtask_function(todo_list=filename) # Allows the user to create task(s)
        elif choice_user == "3": # Directs the user to deletetask_function
            from task_management.delete_task import deletetask_function
            deletetask_function() # Allows the user to delete task(s)
        elif choice_user == "4": # Directs the user to updatestatus_task function
            from task_management.update_status import updatestatus_task
            updatestatus_task() # The user can update his/her task (done or not done)
        elif choice_user == "5": # Redirects back to to-do menu
            from todo_list_system.todo_menu import todo_mainmenu
            todo_mainmenu()
        else: # Else, the program asks the user to enter appropriate input
            print("\nInvalid input! Please try again.")