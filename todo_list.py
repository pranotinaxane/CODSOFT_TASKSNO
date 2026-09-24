tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")

            tasks[number - 1] = new_task
            print("Task updated successfully!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to delete: "))

            deleted_task = tasks.pop(number - 1)
            print(f"'{deleted_task}' deleted successfully!")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")