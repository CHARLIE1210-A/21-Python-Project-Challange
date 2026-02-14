import os

# ================= CONFIGURATION =================
DATA_FILE = "storage.txt"

# ================= DATA HANDLING =================
def load_tasks():
    tasks=[]
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                title, status = line.strip().split("|")
                tasks.append({"title": title, "completed": status == "1"})
                
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        for task in tasks:
            status = "1" if task["completed"] else "0"
            file.write(f"{task['title']}|{status}\n")
        
# ================= TASK OPERATIONS =================
def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False


# ================= DISPLAY =================
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\nYour Tasks: ")
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i+1}. {status} {task['title']}")
        
# ================= MENU =================
def show_menu():
    print("""
          ================ TO-DO LIST MENU =================
            1. Add Tasks
            2. View Tasks
            3. Mark task Completed
            4. Delete Task
            5. Exit
          ===================================================
          """)

# ================= MAIN APP =================
def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            title = input("Enter task title: ")
            add_task(tasks, title)
            save_tasks(tasks)
            print("Task added successfully.")
            
        elif choice == "2":
            show_tasks(tasks)
        
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to mark as completed: "))
            if complete_task(tasks, index - 1):
                save_tasks(tasks)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
                
        elif choice == "4":
            show_tasks(tasks)
            index = int(input("Enter task number to delete: "))
            if delete_task(tasks, index - 1):
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        
        elif choice == "5":
            print("Existing the application. Goodbye! ")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()