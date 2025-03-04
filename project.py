import json
import texttable
import re


def main():
    """start function"""
    week_planner()


def week_planner():
    """main function"""
    while True:
        sort_days() #display
        print("add[1] finnish[2] reset_week[3] exit[4]")

        action = int(input(": "))
        if action == 1:
            add_task()
        if action == 2:
            remove_task()
        if action == 3:
            new_week()
        if action == 4:
            break


def add_task():
    """add task"""
    print("-----------------------")
    name = input("name: ")
    description = input("description: ")
    estimate = input("estimated length 0.0hr: ")
    day = input("days: ")
    time = input("time range: ")

    data = {
        "name": name,
        "description": description,
        "estimate": reg_estimate(estimate),
        "day": reg_day(day),
        "time": reg_time(time)
    }

    if not check_data(data): #check if data correct
        return print("error")
    
    loaded = load_data()
    with open("calander.json", 'w') as add:
        loaded.append(data)
        json.dump(loaded, add)


def remove_task():
    data = load_data()
    name = input("name: ")
    day = reg_day(input("day: "))
    print(day)
    time = reg_time(input("time: "))
    print(time)
    for i in data:
        if (day[0] in i["day"]) and (i["name"] == name) and within_time(time, i):
            data.remove(i)
            with open("calander.json", 'w') as add:
                json.dump(data, add)
            return print("task removed")
    return print("error task not found")


def new_week():
    data = []
    with open("calander.json", 'w') as add:
        json.dump(data, add)


def within_time(time, check):
    inp = switch_minutes(time[0])
    if len(check["time"]) == 2:
        start = switch_minutes(check["time"][0])
        finnish = switch_minutes(check["time"][1])
    else:
        start = switch_minutes(check["time"][0])
        finnish = float(check["estimate"]) * 60

    if start <= inp <= finnish:
        return True
    return False
    

def switch_minutes(time):
    minutes = time.split(":")
    minutes = int(minutes[0])*60 + int(minutes[1])
    return minutes


def switch_hour(min):
    hours = min // 60
    minutes = min % 60
    return "{:02d}:{:02d}".format(hours, minutes)


def conflict_check(week, start, end):
    if not week:
        return False
    for task in week:
        placed_start = switch_minutes(task["start"])
        placed_end = switch_minutes(task["end"])
        if (start < placed_end and placed_start < end):
            return True
    return False


def compare_time(data):
    week = []
    done = []
    #sort important day
    sorted_data = sorted(data, key=lambda t: len(t["day"]))

    #same but for rest of day
    for task in sorted_data:
        
        start_min = switch_minutes(task["time"][0])
        end_min = switch_minutes(task["time"][1])
        duration = int(float(task["estimate"])*60)
        while (start_min + duration <= end_min):
            if not conflict_check(week, start_min, start_min + duration):
                week.append({
                    "name": task["name"],
                    "description": task["description"],
                    "start": switch_hour(start_min),
                    "end": switch_hour(start_min + duration)
                })
                done.append(task)
                break
            start_min += 15
    return [week, done]


def sort_days():
    done = []
    data = load_data()
    week = []
    day = 0
    for temp in range(7):
        current_day = []
        for i in data:
            if (day in i["day"]) and (i not in done):
                current_day.append(i)
        sorted = compare_time(current_day)
        week.append(sorted[0])
        done.extend(sorted[1])
        day += 1
    view_tasks(place_tasks(week))


def place_tasks(week):
    formed_time = []

    for day in week:
        formed_day =[]
        sorted_schedule = sorted(day, key=lambda x: x['start']) #where have you been all my life
        placement = [["",""] for x in range(24 * 4)] #premade
        #first round!
        if not day:
            for hour in range(24):
                for minutes in range(4):
                    minutes = minutes * 15
                    formed_day.append([f"{hour:02d}:{minutes:02d}", ""])
            formed_time.append(formed_day)
            continue #not it

        for task in sorted_schedule:
            task_start = min_15_format(task["start"])
            task_end = min_15_format(task["end"])
            for i in range(task_start, task_end):
                placement[i][1] = task["name"]

        for hour in range(24):
            for minute_interval in range(4):
                minutes = minute_interval * 15
                index = (hour * 4) + minute_interval
                formed_day.append([f"{hour:02d}:{minutes:02d}", placement[index][1]])
        
        formed_time.append(formed_day)
    return formed_time


def min_15_format(data):
    hr, min = data.split(":")
    return (int(hr) * 4) + (int(min) // 15)


def view_tasks(week):
    table = texttable.Texttable()
    table.header(["time","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    
    transposed_week = list(zip(*week))

    for time_slot in transposed_week:
        row = [time_slot[0][0]]
        for day_data in time_slot:
            row.append(day_data[1])
        table.add_row(row)

    print(table.draw())


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
        if i[:3].lower() in week:
            solved.append(week.index(i[:3]))
    return solved


#return time in form [00:00, 00:00]
def reg_time(data):
    #00:00 - 00:00
    pattern = re.match(r"^([01]?[0-9]|2[0-3])(:[0-5][0-9])?\s*(-?\s*([01]?[0-9]|2[0-3])(:[0-5][0-9])?)?$", data)
    #0:00 am - 00:00 pm
    patternx = re.match(r"^([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM)\s*(-?\s*([0]?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|AM|pm|PM))?$", data)
    
    if patternx:
        return switch_to_24hr(patternx.groups())
    elif pattern:
        return clean_24_hr(pattern.group())
    else:
        return "Wrong"


def switch_to_24hr(data):
    data = tuple(item for item in data if item != None)
    solved = []
    for i in range(len(data)):
        ob = data[i]
        if ob in ["am","AM","PM","pm"]:
            if ob in ["pm", "PM"]:
                time = data[i - 1]
                if ":" in time:
                    fin =f"{int(data[i - 2]) + 12}{time}"
                else:
                    fin = f"{int(time) + 12}:00"
                    solved.append(fin)
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
    return solved


def clean_24_hr(data):
    solved = []
    i = 0
    while i < len(data) and len(solved) < 2:
        temp = ""
        if is_int(data[i]):
            for k in range(len(data[i:])):
                if data[k + i] not in [" ", "-"]:
                    temp += data[k + i]
                else:
                    i = k + i
                    solved.append(temp)
                    break
            else:
                solved.append(temp)
        i += 1
    return solved


def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    

if __name__ == "__main__":
    main()