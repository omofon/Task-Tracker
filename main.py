# CLI Todo App

import json, os, sys

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done - not done yet ⬇
# List all tasks that are not done
# List all tasks that are in progress

DATAFILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATAFILE):
        with open(DATAFILE, "r") as f:
            return json.load(f)
    return []
        
def save_tasks(tasks):
    with open(DATAFILE, "w") as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    new_id = get_next_id(tasks)
    task = {
        'id': new_id,
        'description': description,
        'status': 'todo'
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")
    
def delete_task(task_id):
    tasks = load_tasks()
    original_count = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) == original_count:
        print(f"Task {task_id} not found")
    
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")
    
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")
    
def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task['status'] == status_filter]
        
    if not tasks:
        print("No task found")
        return
    
    status_icons = {
        'todo': '⏸',
        'in-progress': '▶',
        'done': '✔'
    }
    
    for task in tasks:
        icon = status_icons.get(task['status'], '?')
        print(f"{task['id']}. {icon} {task['description']} [{task['status']}]")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [arguments]")
        return
    
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python main.py add '<description>'")
            return
        add_task(sys.argv[2])
        
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python main.py update <id> '<description>'")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
        
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-in-progress <id>")
            return
        mark_task(int(sys.argv[2]), "in-progress")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python main.py delete <id>")
            return
        delete_task(int(sys.argv[2]))
        
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-done <id>")
            return
        mark_task(int(sys.argv[2]), "done")
        
    elif command == "list":
        if len(sys.arv) == 2:
            list_tasks()
        else:
            status = sys.argv[2]
            list_tasks(status)
            
    else:
        print("Unknown command")
        
if __name__ == '__main__':
    main()
