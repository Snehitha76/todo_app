import json

# Task Class
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['category'])
        task.completed = data['completed']
        return task

# File Handling
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Task Management Functions
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}. [{status}] {task.title} - {task.description} ({task.category})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        print(f"Task '{tasks[task_num].title}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks.pop(task_num)
        print(f"Task '{task.title}' deleted.")
    else:
        print("Invalid task number.")

# Main Application loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice, please select again.")
if __name__ == "__main__":
    main()
