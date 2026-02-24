# storage.py
import json
import os

FILE_NAME = "data.json"

def load_data():
    """
    Loads expenses from the JSON file.
    Returns a list of expenses.
    """
    if not os.path.exists(FILE_NAME):
        return []  # file doesn't exist yet

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []

def save_data(expenses):
    """
    Saves the list of expenses to the JSON file.
    """
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except IOError:
        print("❌ Error: Could not save data.")