## Code for task tracker

## main function 
def main():

    print("""
    Welcome to Task Tracker.
    This is a place to write down your tasks, read then when you forget about them ,update them when they are done, and delete them at the end of your day.
        """)
    create_tasks()
    update_tasks()
    delete_tasks()


## function to create tasks
def create_tasks():
    task = input("What you want to accomplish today???\n")
    print(task)


## function to update tasks
def update_tasks():
    print("This is the list of things you need to do today.")

## function to delete tasks
def delete_tasks():
    print(input("Do you need to delete the tasks???"))


if __name__ == "__main__":
    main() 