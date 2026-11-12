## Code for task tracker

## Imports
import json


def safe_data_manager(task):
    with open('task_tracker.json', 'w') as file:
        json.dump(task, file)


def load_tasks():
    try:
        with open('task_tracker.json', 'r') as file:
            test = json.load(file)
            # print(test(type))
            return test
    except FileNotFoundError:
        return [] 

## function to list all the commands
def list_all_task(task):
    print("\n")
    print("*" * 70)
    for index, current_task in enumerate(task, start=1):
        print(f"{index}. {current_task['name']}, description: {current_task['description']}, Deadline:{current_task['deadline']} ")

## function to create tasks
def create_tasks(task):
    name = input("Enter task name: ")
    description = input("Describe exactly what you need to accomplish: ")
    status = input("Mention the time till this should get accomplished: ")
    task.append({"name": name, "description": description, "deadline": status})
    safe_data_manager(task)


## function to update tasks
def update_tasks(task):
    list_all_task(task)
    index = int(input("Enter the task to update: "))
    if 1 <= index <= len(task):
        name = input("Enter the new name: ")
        status = input("Enter status update: ")
        task[index-1] = {"name": name, "status": status} 
        safe_data_manager()
    else:
        print("INVALID SYNTEX!!") 

## function to delete tasks
def delete_tasks(task):
    list_all_task(task)
    index = int(input("Enter the task to delete: "))
    if 1 <= index <= len(task):
        del task[index-1]
        safe_data_manager()
    else:
        print("INVALID SYNTAX!!!")



## function to work as a guide and help the user to navigate
def help_tasks():
    print("\nWelcome to Task Tracker!!!\n")
    print("\nThis is a software you can use to track your progress, ideas, and tasks that you need to accomplish in the next deadline.\n")
    print("\nThis software has following features which can be used and activated using the numbers shown to activate them.\n")
    print("""\n
    1. List all the tasks mentioned
    Pressing 1 leads you to knowing all the list of tasks that you have allocated for yourself. 
    If you are a new user, this would be empty for you as of now. 

    2. Create tasks
    Pressing 2 leads you to create new tasks into this software. 
    Once the task is created, you can use the 1 command to read the those tasks later on. 
    You have a status section with every tasks, which you can come later to update it.

    3. Update tasks
    Pressing 3 leads you to update the status of the tasks you have created in this software.
    These status help the user (YOU) to keep track of your time and work.

    4. Delete tasks
    Pressing 4 leads you to delete the tasks you have created in this software. 
    You can do it at the end of everyday, to wake up with a clean place to start with. 

    5. Help
    Pressing 5 is the navigation help command. 
    It provide you with all the command you need to know to use this software end-to-end. 

    6. Quit
    This is the quit command. 
    This takes you out of the system. 
\n""")


## main function 
def main():
    task = load_tasks()

    print("""
    Welcome to Task Tracker.
    This is a place to write down your tasks, read then when you forget about them ,update them when they are done, and delete them at the end of your day.
        """)

    while True:
        print("\nTask Tracker\n")
        print("\n1. List all the tasks")
        print("\n2. Create a new task")
        print("\n3. Update the status of a task")
        print("\n4. Delete a task")
        print("\n5. New here???? Need Help")
        print("\n6. Quit")
        choice = input("What do you want to do today????")

        match choice:
            case "1":
                list_all_task(task)
            case "2":
                create_tasks(task)
            case "3":
                update_tasks(task)
            case "4":
                delete_tasks(task)
            case "5":
                help_tasks()
            case "6":
                break
            case "_" :
                print("Invaliad Choice!!!")

if __name__ == "__main__":
    main() 