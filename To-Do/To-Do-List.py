import os

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


display_tasks(Tasks)

while True:
    with open("To-Do-List.txt", "w") as file:
        file.write("My To-Do List:\n")
        file.write("======================\n")
        
        for index, task in enumerate(Tasks, start=1):
            file.write(f"{index}. {task}\n")
      
