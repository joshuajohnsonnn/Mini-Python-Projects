import os
from time import sleep
print("Your To-Do List")

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            
Tasks = []
input_task = input("Enter a task (or type 'done' to finish): ")
while input_task.lower() != 'done':
    Tasks.append(input_task)
    input_task = input("Enter a task (or type 'done' to finish): ")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        new_task = input("Enter a new task: ")
        Tasks.append(new_task)
        print(f"Task '{new_task}' added.")
    elif choice == '2':
        display_tasks(Tasks)
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(Tasks):
            removed_task = Tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    elif choice == '3':
        display_tasks(Tasks)
        sleep(5)  # Pause for 5 seconds to allow the user to read the tasks
    elif choice == '4':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid option. Please choose again.")