from auth import login_user, register_user
from tasks import create_task, view_tasks, mark_task_completed, delete_task

def task_menu(username):
    while True:
        print("\n1. Add a Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete a Task\n5. Log Out")
        choice = input("Choose an option by entering the option number: ")

        if choice == '1':
            create_task(username)
        elif choice == '2':
            view_tasks(username)
        elif choice == '3':
            mark_task_completed(username)
        elif choice == '4':
            delete_task(username)
        elif choice == '5':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again. New users please register")

def task_manager():
    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Choose an option by entering the option number: ")

        if choice == '1':
            if login_user():
                username = input("Enter your username again to continue: ")
                task_menu(username)  # Proceed to task manager
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    task_manager()