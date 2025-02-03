# Imports the json module
import json

def show_categories_and_tasks(username): # Function that shows the categories along with its tasks
    try:
        # Attempts to open and load categories from the user-specific categories file
        with open(f"C:/Users/edria/OneDrive/Desktop/KADUSALE Python Project/KADUSALE Python Project/users_categories_folder/{username}-categories.json", "r") as file:
            categories = json.load(file)
            if categories: # If categories exist in the file, then show the categories and its tasks
                print("\n-'/LIST OF CATEGORIES/'-")
                # Iterates over each category and its associated tasks
                for category, tasks in categories.items():
                    print(f"\n***** CATEGORY: {category} *****")
                    print("`````````````````````````````")
                    # Iterates over each task within the category and display its information
                    for task in tasks:
                        # Details for each category
                        print(f"Title: {task['title']}")
                        print(f"Description: {task['description']}")
                        print(f"Date: {task['date']}")
                        print(f"Time: {task['time']}")
                        print(f"ID: {task['id']}")
                        print(f"Status: {task['status']}")
                        print("-------------------------")
            else:
                # If no categories can be found
                print("\nNo categories found.")
    except FileNotFoundError:
        # If the categories json file is empty
        print("\nNo categories found.")
