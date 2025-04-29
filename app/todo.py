# app/todo.py
class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid index")
        self.tasks.pop(index)

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid index")
        self.tasks[index]["completed"] = True

    def list_tasks(self):
        return self.tasks

if __name__ == "__main__":
    app = TodoApp()
    app.add_task("Test task")
    print("Current tasks:", app.list_tasks())