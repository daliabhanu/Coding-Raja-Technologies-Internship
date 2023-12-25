import os
import json
from datetime import datetime, timedelta

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']}")

def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (High/Medium/Low): ").capitalize()
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {"title": title, "priority": priority, "due_date": due_date.strftime("%Y-%m-%d")}
    tasks.append(task)
    print("Task added successfully!")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Task data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()