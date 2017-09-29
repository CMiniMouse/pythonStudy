#coding=utf-8

import pickle

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
        return (AthleteList(temp.pop(0), temp.pop(0), temp))
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
    def __init__(self, a_name = None, a_dob = None, a_times = []):
        list.__init__([])
        self.name   = a_name
        self.dob    = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle", "wb") as athf:
            pickle.dump(all_athletes,athf)
    except IOError as err:
        print("File Error:" + str(err))

    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print("File Error:" + str(err))

    return (all_athletes)
