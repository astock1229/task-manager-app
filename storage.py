import json
import os

DATA_FILE = 'users.json'

# Load the data from the JSON file or create a new file if it doesn't exist
def load_user_data():
    if not os.path.exists(DATA_FILE):  # If the file doesn't exist, return an empty dictionary
        return {}
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:  # Handle the case when the file is empty or invalid
            return {}

# Save user data back to the JSON file
def save_user_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)
