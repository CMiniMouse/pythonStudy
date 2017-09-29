filename = 'sketch.txt'
man = []
other = []
try:
    data = open(filename)

    for each_line in data:
        try:
            (role, spoken) = each_line.split(':', 1)
            spoken = spoken.strip();
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print("The data file <" + filename + "> does not exists!")

try:
    with open("man.txt", "w") as man_file:
        man_file.writelines(man)
    with open("other.txt", "w") as other_file:
        other_file.writelines(other)
except IOError as err:
    print("File Error" + str(err))
