# Importing modules/libraries for this basic todo list application.
import sys
from questionary import prompt, select
from termcolor import colored

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(colored(f"Task '{task}' added!", 'green'))

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {colored(task, 'yellow')}")

def mark_task_complete(tasks, index):
    if 0 <= int(index) < len(tasks):  # Convert index to integer
        tasks[int(index)] += " (Completed)"
        print(colored(f"Task '{tasks[int(index)]}' marked as complete!", 'green'))
    else:
        print(colored("Invalid task number.", 'red'))

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks[index]   # store first
        del tasks[index]              # then delete
        print(colored(f"Task '{removed_task}' removed!", 'green'))
    else:
        print(colored("Invalid task number.", 'red'))

# Define Main Dashboard function for the todo list application.
def main():
    tasks = []

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = int(input("[1-5]: "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            index = input("Enter the task number to mark as complete: ")
            mark_task_complete(tasks, int(index) - 1) # Convert index back to integer
        elif choice == 4:
            index = input("Enter the task number to remove: ")
            remove_task(tasks, int(index) - 1)  # Convert index back to integer
        elif choice == 5:
            print(colored("Exiting Todo List. Goodbye!", 'blue'))
            sys.exit(0)
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

if __name__ == "__main__":
    main()