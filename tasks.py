import json
import uuid
from storage import load_user_data, save_user_data

# Load the tasks for a specific user
def load_tasks(username):
    user_data = load_user_data()
    return user_data[username].get("tasks", [])

# Save the tasks for a specific user
def save_tasks(username, tasks):
    user_data = load_user_data()
    if username in user_data:
        user_data[username]["tasks"] = tasks
        save_user_data(user_data)

# Create a new task with a simplified sequential ID and status set to "Pending"
def create_task(username):
    task_description = input("Enter the task description: ")
    tasks = load_tasks(username)
    
    # Generate a simple task ID based on the number of existing tasks
    task_id = f"{len(tasks) + 1:03}"  # Task ID as '001', '002', etc.
    task_status = "Pending"  # Set the task status to "Pending"
    
    tasks.append({
        "id": task_id,
        "description": task_description,
        "status": task_status
    })
    
    save_tasks(username, tasks)
    print(f"Task '{task_description}' added successfully with ID: {task_id} and status: {task_status}.")


# View all tasks with task ID, description, and status
def view_tasks(username):
    tasks = load_tasks(username)
    if not tasks:
        print("No tasks found.")
        return
    print(f"\nTasks for {username}:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")

# Mark a task as completed by its ID
def mark_task_completed(username):
    tasks = load_tasks(username)
    view_tasks(username)  # Show all tasks with their IDs
    task_id = input("Enter the task ID to mark as completed: ")

    # Find the task by its ID
    task = next((task for task in tasks if task["id"] == task_id), None)
    
    if task:
        task["status"] = "Completed"  # Change the status to "Completed"
        save_tasks(username, tasks)
        print(f"Task '{task['description']}' with ID {task_id} marked as completed.")
    else:
        print(f"Task with ID {task_id} not found.")


# Delete a task by its ID
def delete_task(username):
    tasks = load_tasks(username)
    view_tasks(username)  # Show all tasks with their IDs
    task_id = input("Enter the task ID to delete: ")

    # Find the task by its ID
    task_index = next((index for index, task in enumerate(tasks) if task["id"] == task_id), None)
    
    if task_index is not None:
        task = tasks.pop(task_index)
        save_tasks(username, tasks)
        print(f"Task '{task['description']}' with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")
