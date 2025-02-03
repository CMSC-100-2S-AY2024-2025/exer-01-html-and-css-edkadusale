# PYTHON PROJECT in CMSC 12 
# made by JAN EDRIAN KADUSALE of C1L

# PROJECT DESCRIPTION: The goal of this project is to develop a Command Line Interface (CLI) 
# tool that enables users to manage a to-do list by adding, deleting, updating, and categorizing 
# tasks. The tool should integrate a user authentication system, allowing users to access their 
# tasks securely. The program should be able to parse dates and timestamps and display the 
# progress of tasks.

# Introduction (project title and owner)
print("\n--------TO-DO LIST PROGRAM--------")
print("      by JAN EDRIAN KADUSALE")

# Imports the authentication function from user_authentication folder and runs it
from user_authentication.authentication_main import authentication
authentication()

# Imports sys module and login function
import sys
from user_authentication.login_function import login
username = login()

# Takes the logged-in username to be printed out in the statement below
# This will be printed out if the user exits the program
def exit():
    print(f"\nThank you for using the program {username}. Goodbye!")
    sys.exit()




