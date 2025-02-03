# A function that creates json file for each user 

def createjson_usertask(username):
    # Imports json and os modules
    import json
    import os

    # To viewers of this code, kindly change the path if necessary
    folder = "C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_tasks_folder"
    filename = f"{username}-tasks.json" # json file name
    filepath = os.path.join(folder, filename)

    # Creates an empty list to be included in the json file 
    data = []

    # Adds the empty list to the file
    with open(filepath, "w") as file:
        json.dump(data, file)
