# This function registers a new user in the program before they can proceed to the login section
# Imports re and json modules
import re
import json

def register(): # Registration function
    # Registration title
    print("\nREGISTRATION")

    # Username input
    username = input("Input username: ")

    # Check if the username is at least 6 characters long
    if len(username) < 6:
        # A message will print out if the character length condition is not satisfied
        print("\nUsername should be at least 6 characters long!")
        return

    # Loads the existing user information from user.json
    with open("C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/user.json", "r") as file:
        user_information = json.load(file)

    # Checks if the username already exists
    if username in user_information:
        # If not, users are required to create a new one
        print("\nUsername already exists. Please input a new one.")
    else:
        # If yes, users can input their password
        password = input("Input password: ")

        # Password being created should have at least a lowercase and uppercase letter and a number
        # If the inputted password does not follow the password format, the message below appears
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            print("\nPassword should be at least 8 characters containing a combination of uppercase and lowercase letters, and numbers.")
            return
        
        # If all conditions (username and password) are satisfied then
        # The new username and password will be added to the user.json file
        user_information[username] = password

        # Save the updated user information to user.json
        with open("C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/user.json", "w") as file:
            json.dump(user_information, file)
        
        # A new {username}-tasks.json file will be created that collects the tasks
        from user_authentication.jsonfile_fortasks import createjson_usertask
        createjson_usertask(username)

        print("\nRegistration successful! Please log in.")
