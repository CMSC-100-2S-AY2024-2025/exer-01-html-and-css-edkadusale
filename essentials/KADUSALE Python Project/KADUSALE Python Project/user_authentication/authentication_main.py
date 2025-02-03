# User authentication section of the program
# The main script that has access to registration and login processes

# Import the register and login function here in the authentication script
from user_authentication.register_function import register
from user_authentication.login_function import login

# Reminder for the users
print("\n**********************************")
print("\nTo access the To-Do List Program, new users are required to register before")
print("logging in. However, existing users can jump directly to the Log In section.")

# Main program for the authentication system
def authentication(): # Authentication function

    while True: 
        # User Authentication title and options
        print("\nUSER AUTHENTICATION")
        print("[1] Register\n[2] Login\n[3] Exit\n")

        # User's choice (variable to be processed)
        choice = input("Select an option: ")

        # Conditional statements given the authentication options
        if choice == "1": # Choice 1 for the user registration
            register() # Directs the user to the register function
        elif choice == "2": # Choice 2 for user login
            login() # Directs the user to the login function
            break
        elif choice == "3": # Choice 3 for program exit
            print(f"\nGoodbye!") # Ends the program
            import sys
            sys.exit()
        else:
            # If users input an invalid choice, the program will ask again
            print("\nInvalid choice. Please try again.") 

