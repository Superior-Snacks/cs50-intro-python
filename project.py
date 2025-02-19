import json
import texttable


def main():

    week_planner()

    view_single()


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
        if action == 3:
            break

def add_task():
    print("-----------------------")
    print("add task, specify name and description")
    name = input("name: ")
    description = input("description: ")
    estimate = input("estimated length 0.0hr:")
    print("give range or spesific time and day")
    day = input("day mon - tue or any: ")
    time = input("write time in 00:00 format or give a range 00:00 - 00:00")

    data = {
        "name": name,
        "description": description,
        "estimate": estimate,
        "day": day,
        "time": time
    }


    #if check_data(data) == False:
    #    return 1
    


    loaded = load_data()
    with open("calander.json", 'w') as add:
        loaded.append(data)
        json.dump(loaded, add)

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

def view_single():
    with open("calander.json", 'r') as see:
        loaded_data = json.load(see)
        print(loaded_data)

def load_data():
    whole_plan = []
    try:
        with open("calander.json", 'r') as load:
            whole_plan = json.load(load)
            return whole_plan
    except:
        return whole_plan


def check_data(data):
    x = True
    if len(data["name"]) > 20:
        print("name too long")
        x = False
    if len(data["description"]) > 200:
        print("descriptin too long, it is not that deep bro")
        x = False
    estimate = reg_estimate(data["estimate"])
    if estimate == "Wrong":
        print("give a propper estmate")
    else:
        data["estimate"] = estimate
    
    day = reg_day(data["day"])
    if day == "Wrong":
        print("pleas give a valid date")


def reg_estimate(data):
    estimate_format = ""
    return estimate_format

def reg_day(data):
    day_format = ""
    return day_format

def reg_time(data):
    time_format = ""
    return time_format
    

if __name__ == "__main__":
    main()