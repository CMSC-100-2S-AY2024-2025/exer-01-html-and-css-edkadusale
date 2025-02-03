# This function allows an existing user to log-in his/her username and password
# Imports json module
import json

def login(): # Log-in function

     # Imports the authentication function from authentication_main script
     from user_authentication.authentication_main import authentication

     # Imports the todo_mainmenu function from todo_menu script
     from todo_list_system.todo_menu import todo_mainmenu

     # Collects the user's username and password
     print("\nLOGIN") # Login title
     
     global username # Makes the username variable accessible on the outside
     username = input("Enter your username: ") # Asks the user his/her username
     password = input("Enter your password: ") # Asks the user his/her password

     # Loads the information from user.json file
     with open("C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/user.json", "r") as file:
        user_information = json.load(file)

     # Checks if the username and password are already registered and are in the json file
     # If the username and password can be found in the json file
     if username in user_information and user_information[username] == password:
          # Then the program allows access to the to-do list program
          print("\nLogin successful! You can now use the To-Do List Program!")
          todo_mainmenu() # Calls the to-do list main menu function
     else:
          # Otherwise, the program will redirect users to the user authentication section
          print("\nInvalid username or password. Please try again.")
          authentication() # Calls the authentication menu
     



               
