import json
import texttable
import re

def main():
    #print(switch_minutes("6:00"))
    sort_days()
    #sort_tasks()
    #view_tasks()
    #print(reg_estimate(input(":")))
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
    
    loaded = load_data()
    with open("calander.json", 'w') as add:
        loaded.append(data)
        json.dump(loaded, add)

def remove_task():
    ...

def finnish_task():
    ...
def switch_minutes(time):
    minutes = time.split(":")
    minutes = int(minutes[0])*60 + int(minutes[1])
    print("switch")
    return minutes

def switch_hour(min):
    hours = min // 60
    minutes = min % 60
    return "{:02d}:{:02d}".format(hours, minutes)

def conflict_check(week, start, end):
    print(f"week {week}")
    if not week:
        return False
    for task in week:
        placed_start = switch_minutes(task["start"])
        placed_end = switch_minutes(task["end"])
        if (start < placed_end and placed_start < end):
            print("conflict")
            return True
    print("not a conflict")
    return False

def compare_time(data):
    print("so we begin")
    print(data)
    week = []

    #sort important day
    print("import")
    for k in data:
        stop = False
        print(F"current is {k}")
        if len(k["day"]) < 2:
            print(f"this is suposed to be only monday {k}")
            start_min = switch_minutes(k["time"][0])
            end_min = switch_minutes(k["time"][1])
            duration = int(float(k["estimate"])*60)
            print(k["name"])
            print(start_min)
            print(end_min)
            print(duration)
            print(f"comine {start_min + duration}")
            while (start_min + duration <= end_min) and stop == False:
                if not conflict_check(week, start_min, start_min + duration):
                    week.append({
                        "name": k["name"],
                        "description": k["description"],
                        "start": switch_hour(start_min),
                        "end": switch_hour(start_min + duration)
                    })
                    stop = True
                start_min += 1

    #same but for rest of day
    print("rest")
    for i in data:
        print(F"current is {i}")
        stop = False
        start_min = switch_minutes(i["time"][0])
        end_min = switch_minutes(i["time"][1])
        duration = int(float(i["estimate"])*60)
        while (start_min + duration < end_min) and stop == False:
            if not conflict_check(week, start_min, start_min + duration):
                week.append({
                    "name": i["name"],
                    "description": i["description"],
                    "start": switch_hour(start_min),
                    "end": switch_hour(start_min + duration)
                })
                stop = True
            start_min += 1
    return week


#go throug day by day, compare time slots
def sort_days():
    x = True
    data = load_data()
    table = texttable.Texttable()
    week = {"mon":[], "tue":[], "wed":[], "thu":[], "fri":[], "sat":[], "sun":[]}
    for temp in range(7):
        day = 0
        current_day = []
        for i in data:
            if day in i["day"]:
                current_day.append(i)
                print(i)
        day += 1
        print(f"this is day {day} : {compare_time(current_day)}")
        #check if already placed on another day
        #save global
        #switch to sql maybe
        






#add tasks to table
#prolly decrepid
def sort_tasks():
    hour = 0
    data = load_data()
    table = texttable.Texttable()
    table.header(["time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    while hour < 25:
        planner_time = f"{hour}:00"
        current_hour = [planner_time, "", "", "", "", "", "", ""]
        for i in data:
            time_check = i["time"][0].split(":")
            time_check = int(time_check[0])
            if time_check == hour:
                day_index = i["day"][0]
                current_hour[day_index + 1] += i["name"]
            #print(f"hour: {current_hour} task: {i["name"]} time: {i["time"]} estimate: {i["estimate"]}")
        print(current_hour)
        table.add_row(current_hour)
        hour += 1



    print(table.draw())


def view_tasks():
    table = texttable.Texttable()
    table.header(["time","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    table.add_row(["6:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["7:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["8:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["9:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["10:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["11:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["12:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["13:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["14:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["15:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["16:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["18:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["19:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["20:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["21:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["22:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["23:00","task", "task", "task", "task", "task", "task", "task"])
    table.add_row(["24:00","task", "task", "task", "task", "task", "task", "task"])
    print(table.draw())

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
    ps = re.match(r"^([0-9]{1,2}(\.[0-9]{0,2})?)\s*(hours?|hrs?|HR|Hr|HRS|Hours)?$", data, re.IGNORECASE)
    if ps:
        hours_str = ps.group(1).strip()
        hours = float(hours_str)
        return float("{:.2f}".format(hours))
    else:
        return "Wrong"

#return day in form of [1,2,3]
def reg_day(data):
    solved =[]
    week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day_format = re.split(r"[- ]+",data)
    for i in day_format:
        print(i[:3])
        if i[:3].lower() in week:
            solved.append(week.index(i[:3]))
            print(f"found {solved}")
    print(day_format)
    return solved

#return time in form [00:00, 00:00]
def reg_time(data):
    #00:00 - 00:00
    pattern = re.match(r"^([01]?[0-9]|2[0-3])(:[0-5][0-9])?\s*(-?\s*([01]?[0-9]|2[0-3])(:[0-5][0-9])?)?$", data)
    #0:00 am - 00:00 pm
    patternx = re.match(r"^([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM)\s*(-?\s*([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM))?$", data)
    
    if patternx:
        print("patternx")
        return switch_to_24hr(patternx.groups())
    elif pattern:
        print("pattern")
        return clean_24_hr(pattern.group())
    else:
        return "Wrong"


def switch_to_24hr(data):
    data = tuple(item for item in data if item != None)
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
                    fin =f"{int(data[i - 2]) + 12}{time}"
                else:
                    fin = f"{int(time) + 12}:00"
                    solved.append(fin)
                print(f"add the pm{solved}")
            else:
                time = data[i - 1]
                if ":" in time:
                    fin =f"{int(data[i-2])}{time}"
                else:
                    fin = f"{int(time)}:00"
                if fin == "12:00":
                    solved.append("00:00")
                else:
                    solved.append(fin)
                print(f"add the am{solved}")
    print(solved)
    return solved

def clean_24_hr(data):
    print(data)
    solved = []
    i = 0
    while i < len(data) and len(solved) < 2:
        temp = ""
        if is_int(data[i]):
            for k in range(len(data[i:])):
                if data[k + i] not in [" ", "-"]:
                    temp += data[k + i]
                    print(temp)
                else:
                    print("break found")
                    i = k + i
                    print(f"I is {i}")
                    solved.append(temp)
                    break
            else:
                solved.append(temp)
        i += 1
    return solved

def is_int(x):
    try:
        int(x)
        print(f"{x} is def a number")
        return True
    except ValueError:
        print(f"{x} is def NOT a number")
        return False
    

if __name__ == "__main__":
    main()