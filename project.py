import json


def main():
    ...




if __name__ == "__main__":
    main()

def week_planner():
    while True:
        print("add task = 1")
        print("remove task = 2")
        print("finnish task = 3")
        print("veiw tasks = 4")
        print("add routine = 5")
        print("save/exit = ")

        action = int(input(": "))
        if action == 1:
            add_task()
        if action == 2:
            remove_task()

def add_task():
    print("-----------------------")
    print("add task, specify name and description")
    name = input("name: ")
    description = input("description: ")
    print("what type of task is it rigid/flowing")
    task_type = input("rigid = 1, flowing = 2")
    if task_type == 1:
        print("declare day and time")
    with open("calander.json", 'w') as add:
        ...

def remove_task():
    ...

def finnish_task():
    ...

def sort_tasks():
    ...

def view_tasks():
    ...

def planner_paramiter():
    ...





