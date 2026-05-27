# Importing modules/libraries for this basic todo list application.
import sys
import json
from questionary import prompt, select
from termcolor import colored

filename = "todo_list.json"

# Function to add tasks
def add_task(tasks):
    task = input("Enter a new task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task = {
        "task": task,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    save_tasks_to_file(filename, tasks)
    print(colored(f"Task added successfully!", 'green'))

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print(colored("No tasks available.", 'yellow'))
        return
    
    print("\nYour Tasks:\n")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(
            f"{i}. "
            f"{task['task']} | "
            f"Due: {task['due_date']} | "
            f"{status}"
            )

# Function to mark tasks as complete
def mark_task_complete(tasks, index):
    if 0 <= int(index) < len(tasks):  # Convert index to integer
        tasks[int(index)]["completed"] = True
        save_tasks_to_file(filename, tasks)
        print(colored(f"Task '{tasks[int(index)]}' marked as complete!", 'green'))
    else:
        print(colored("Invalid task number.", 'red'))

# Function to remove task from a list of tasks
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks[index]["task"]   # store first
        del tasks[index]              # then delete
        save_tasks_to_file(filename, tasks)
        print(colored(f"Task '{removed_task}' removed!", 'green'))
    else:
        print(colored("Invalid task number.", 'red'))

# Function to search tasks
def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()
    found = False
    print("\nSearch Results:\n")
    for i, task in enumerate(tasks, start=1):
        if keyword in task["task"].lower():
            status = "✅" if task["completed"] else "❌"
            print(
                f"{i}. "
                f"{task['task']} | "
                f"Due: {task['due_date']} | "
                f"{status}"
            )
            found = True
    if not found:
        print(colored("No matching tasks found.", 'red'))

# Function to edit existing tasks
def edit_task(tasks, index):
    if 0 <= index < len(tasks):
        print(f"\nCurrent Task: {tasks[index]['task']}")
        print(f"Current Due Date: {tasks[index]['due_date']}")
        new_task = input("Enter updated task: ")
        new_due_date = input("Enter updated due date (YYYY-MM-DD): ")
        tasks[index]["task"] = new_task
        tasks[index]["due_date"] = new_due_date
        save_tasks_to_file(filename, tasks)
        print(colored("Task updated successfully!", "green"))
    else:
        print(colored("Invalid task number.", "red"))

# Function to write/save tasks to JSON file
def save_tasks_to_file(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to read/load tasks from JSON file
def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(colored("File not found. Starting with an empty task list.", 'yellow'))
        return[]

# Define Main Dashboard function for the todo list application.
def main():
    tasks = load_tasks_from_file(filename)

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Complete")
        print("5. Remove Task")
        print("6. Search Tasks")
        print("7. Exit")

        choice = int(input("\nSelect an option [1-7]: "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            view_tasks(tasks)
            index = input("Enter the task number to edit: ")
            edit_task(tasks, int(index) - 1)
        elif choice == 4:
            view_tasks(tasks)
            index = input("Enter the task number to mark as complete: ")
            mark_task_complete(tasks, int(index) - 1) # Convert index back to integer
        elif choice == 5:
            view_tasks(tasks)
            index = input("Enter the task number to remove: ")
            remove_task(tasks, int(index) - 1)  # Convert index back to integer
        elif choice == 6:
            search_task(tasks)
        elif choice == 7:
            print(colored("Exiting Todo List. Goodbye!", 'blue'))
            sys.exit(0)
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

if __name__ == "__main__":
    main()