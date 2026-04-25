tasks = []
print("Welcome to To Do List!")
choice = input("\n1.Add Task \n2. Show Tasks\n3. Delte Task\nEnter choice: ")
if choice == "1":
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task added: {task}")
    
elif choice == "2":
    if len(tasks) == 0:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

elif choice == "3":
    task = input("Enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Deleted: {task}")
    else:
        print("Task not found!")

else:
    print("Invalid choice!")