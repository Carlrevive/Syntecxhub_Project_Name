import json
import os
from datetime import datetime


FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from a JSON file. If file doesn't exist, return an empty list."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error reading task file. Starting fresh.")
        return []


def save_tasks(tasks):
    """Save the list of tasks to a JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error: Could not save tasks.")



def add_task(tasks):
    """Add a new task with optional tag and due date."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tag = input("Enter tag (optional): ").strip()
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task will have no due date.")
            due_date = ""

    task = {
        "title": title,
        "done": False,
        "tag": tag if tag else None,
        "due_date": due_date if due_date else None
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else " Not Done"
        tag = f"[Tag: {task['tag']}]" if task["tag"] else ""
        due = f"(Due: {task['due_date']})" if task["due_date"] else ""
        print(f"{idx}. {task['title']} {status} {tag} {due}")
    print()


def delete_task(tasks):
    """Delete a task by number."""
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_task_done(tasks):
    """Mark a specific task as done."""
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num - 1]['title']}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
