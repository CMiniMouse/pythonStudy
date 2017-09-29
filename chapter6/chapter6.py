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
        return (data.strip().split(","))
    except IOError as err:
        print("File Error:" + str(err))
        return (None)

james = []
julie = []
mikey = []
sarah = []

sarah = get_coach_data("sarah2.txt")
sarah_data = dict()
sarah_data["Name"] = sarah.pop(0)
sarah_data["Birth"] = sarah.pop(0)
sarah_data["Times"] = str(sorted(set([sanitize(t) for t in sarah]))[0:3])
print(sarah_data)
