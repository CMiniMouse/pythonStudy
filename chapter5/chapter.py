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


james = []
julie = []
mikey = []
sarah = []
with open("james.txt", "r") as jaf:
    data = jaf.readline() 
james = data.strip().split(",")
with open("julie.txt", "r") as juf:
    data = juf.readline()
julie = data.strip().split(",")
with open("mikey.txt", "r") as mif:
    data = mif.readline()
mikey = data.strip().split(",")
with open("sarah.txt", "r") as saf:
    data = saf.readline()
sarah = data.strip().split(",")

std_james = []
std_julie = []
std_mikey = []
std_sarah = []

for each_item in james:
    std_james.append(sanitize(each_item))
for each_item in julie:
    std_julie.append(sanitize(each_item))
for each_item in mikey:
    std_mikey.append(sanitize(each_item))
for each_item in sarah:
    std_sarah.append(sanitize(each_item))

print("old data:")
print(james)
print(julie)
print(mikey)
print(sarah)
print("standard data:")
print(std_james)
print(std_julie)
print(std_mikey)
print(std_sarah)
print("sorted data:")
print(sorted(std_james))
print(sorted(std_julie))
print(sorted(std_mikey))
print(sorted(std_sarah))

#用列表推导优化代码
print("After optimize code:")
print(sorted([sanitize(each_item) for each_item in james])[0:3])
print(sorted([sanitize(each_item) for each_item in julie])[0:3])
print(sorted([sanitize(each_item) for each_item in mikey])[0:3])
print(sorted([sanitize(each_item) for each_item in sarah])[0:3])

#在排序基础上去重输出前三记录
unique_james = []
for each_one in sorted(std_james):
    if each_one not in unique_james:
        unique_james.append(each_one)
print(unique_james[0:3])
