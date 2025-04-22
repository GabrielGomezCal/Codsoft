import json
from datetime import datetime

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"[{status}] {task['id']}: {task['description']} (Created at: {task['created_at']})")
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"🎉 Task {task_id} completed.")
                return
        print(f"❌ Task {task_id} not found.")
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑️ Task {task_id} deleted.")
                return
        print(f"❌ Task {task_id} not found.")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Error loading tasks. File may be corrupted.")
            self.tasks = []


todo_list = ToDoList()

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        description = input("Enter task description: ")
        todo_list.add_task(description)
    elif choice == '2':
        todo_list.show_tasks()
    elif choice == '3':
        task_id = int(input("Enter task ID to complete: "))
        todo_list.complete_task(task_id)
    elif choice == '4':
        task_id = int(input("Enter task ID to delete: "))
        todo_list.delete_task(task_id)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")
