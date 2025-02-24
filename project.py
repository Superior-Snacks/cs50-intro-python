import json
import texttable
import re

def main():

    print(reg_time(input(":")))
    #week_planner()

    #view_single()


def week_planner():
    while True:
        print("soon: add routine, move task, save and exit")
        print("add[1] remove[2] complete[3]")

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
        "estimate": reg_estimate(estimate),
        "day": reg_day(day),
        "time": reg_time(time)
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
    if data["estimate"] == "Wrong":
        print("give a propper estmate")
        x = False
    if data["day"] == "Wrong":
        print("pleas give a valid date")
        x = False
    if data["time"] == "Wrong":
        print("format time propperly")
        x = False
    
    return x

#retrun hours in form of 0.00
def reg_estimate(data):
    if re.match(r"^[0-9]{1,2}(\.[0-9]{0,2})?\s*(hours?|hrs?|HR|Hr|HRS|Hours)?$", data):
        get = re.match(r"^[0-9]{1,2}(\.[0-9]{0,2})?\s", data)
        hours = float(get.group(0))
        return "{:.2f}".format(hours) 
    else:
        return "Wrong"

#return day in form of [1,2,3]
def reg_day(data):
    week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day_format = data
    return day_format

#return time in form [00:00, 00:00]
def reg_time(data):
    #00:00 - 00:00
    #pattern = re.match(r"^([01]?[0-9]|2[0-3])(:[0-5][0-9])?\s*(-?\s*([01]?[0-9]|2[0-3])(:[0-5][0-9])?)?$", data)
    #0:00 am - 00:00 pm
    patternx = re.match(r"^([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM)\s*(-?\s*([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM))?$", data)
    print(patternx.groups(all))
    
    
    if patternx:
        switch_to_24hr(patternx.groups(all))
        return patternx
    elif pattern:
        return pattern
    else:
        return "Wrong"


def switch_to_24hr(data):
    solved = []
    print("start")
    for i in range(len(data)):
        ob = data[i]
        print("for strt")
        print(ob)
        if ob in ["am","AM","PM","pm"]:
            print(f"i is {ob}")
            if ob in ["pm", "PM"]:
                time = data[i - 1]
                if ":" in time:
                    time.split(":")
                    fin =time[0] + 5
                    fin ="{fin}" +":" + time[-1]
                    solved.append(fin)
                    print(f"add the sloved{solved}")
                    print("sillty")
    return solved

    

if __name__ == "__main__":
    main()