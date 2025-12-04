import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "todo_tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x500")
        self.tasks = load_tasks()

        self.build_gui()
        self.display_tasks()

    def build_gui(self):
        # Entry box to add task
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Add Task button
        add_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_btn.pack()

        # Frame to list tasks
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Delete completed button
        clear_btn = tk.Button(self.root, text="Delete Completed", command=self.delete_completed)
        clear_btn.pack(pady=5)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            save_tasks(self.tasks)
            self.entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def toggle_done(self, index):
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        save_tasks(self.tasks)
        self.display_tasks()

    def delete_completed(self):
        self.tasks = [task for task in self.tasks if not task["done"]]
        save_tasks(self.tasks)
        self.display_tasks()

    def display_tasks(self):
        # Clear old task widgets
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Display all tasks
        for idx, task in enumerate(self.tasks):
            task_text = task["task"]
            done = task["done"]

            cb = tk.Checkbutton(
                self.task_frame,
                text=task_text,
                font=("Arial", 12),
                variable=tk.BooleanVar(value=done),
                onvalue=True,
                offvalue=False,
                anchor="w",
                command=lambda i=idx: self.toggle_done(i),
            )
            cb.pack(fill="x", pady=2)
            if done:
                cb.select()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
