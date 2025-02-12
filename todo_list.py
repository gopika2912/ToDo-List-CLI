tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def view_tasks():
    print("Tasks:", tasks)

if __name__ == "__main__":
    add_task("Complete project")
    add_task("Buy groceries")
    view_tasks()
    remove_task("Buy groceries")
    view_tasks()
