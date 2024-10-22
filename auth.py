import hashlib
from storage import load_user_data, save_user_data

# Hash the password for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user (with hashed password)
def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    password_confirm = input("Confirm password: ")

    if password != password_confirm:
        print("Passwords do not match. Try again.")
        return

    user_data = load_user_data()

    if username in user_data:
        print("Username already taken. Try a different one.")
        return

    # Initialize the user with hashed password and an empty task list
    user_data[username] = {
        "password": hash_password(password),  # Hash the password before storing it
        "tasks": []  # Initialize tasks as an empty list
    }

    save_user_data(user_data)
    print(f"User '{username}' registered successfully.")

# Authenticate user during login (compare hashed password)
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_data = load_user_data()

    # Check if the user exists and the password matches
    if username in user_data:
        stored_password = user_data[username]['password']  # Get the stored hashed password
        if stored_password == hash_password(password):     # Compare the hashed version of the entered password
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False
    else:
        print("Invalid username or password. Please try again.")
        return False