class TodoList:
    def __init__(self, filename='15_Daily_Questions\\project_txt_file\\tasks.txt'):
        self.filename = filename

    def add_task(self, task):
        with open(self.filename, 'a') as file:
            file.write(task + '\n')

    def show_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = file.readlines()
                if not tasks:
                    print("No tasks found!")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
        except FileNotFoundError:
            print("No task file found!")

todo = TodoList()

while True:
    print("\n1. Add Task  2. View Tasks  3. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        todo.add_task(input("Enter task: "))
    elif ch == '2':
        todo.show_tasks()
    elif ch == '3':
        break
    else:
        print("Invalid choice!")
