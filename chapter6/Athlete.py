#coding=utf-8

def sanitize(time_string):
    if ":" in time_string:
        splitter = ':'
    elif "-" in time_string:
        splitter = '-'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename, "r") as dfile:
            data = dfile.readline()
        temp = data.strip().split(",")
        return (Athlete(temp.pop(0), temp.pop(0), temp))
    except IOError as err:
        print("File Error:" + str(err))
        return (None)

#从零定义一个新类
class Athlete:
    def __init__(self, a_name, a_dob = None, a_times = []):
        self.name   = a_name
        self.dob    = a_dob
        self.times  = a_times
     
    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self, a_time):
        self.times.append(a_time)

    def add_times(self, time_list):
        self.times.extend(time_list)

#继承一个内置类
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        self.name   = a_name
        self.dob    = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

    def get_coach_data(filename):
        try:
            with open(filename, "r") as f:
                data = f.readline()
            temp = data.strip().split(",")
            
            return (AthleteList(temp.pop(0), temp.pop(0), temp))
        except IOError as err:
            print("File Error:" + str(err))
            return None

sarah = get_coach_data("sarah2.txt")

print(sarah.name + "'s fastest times are:" + str(sarah.top3()))

sarah.add_time("4.33")
print(sarah.times)
sarah.add_times(["3.33", "5.55"])
print(sarah.times)

james = Athlete("james")
james.add_times(["1.11", "1.11", "2.22", "2.32", "3.22"])
james.add_time("2-23")
print(james.name)
print(james.times)
print(james.top3())

print("AthleteList")
julie = AthleteList("julie")
julie.append("2-21")
julie.extend(["2:20", "3.21", "2.32"])
print(julie)
print(julie.top3())
