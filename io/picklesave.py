import pickle;

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
    with open("mandata.txt", "wb") as man_file:
        pickle.dump(man, man_file)
    with open("otherdata.txt", "wb") as other_file:
        pickle.dump(other, other_file)
except IOError as err:
    print("File Error" + str(err))
except pickle.PickleError as perr:
    print("Pickle Error" + str(perr))


#get data
with open("mandata.txt", "rb") as man_read:
    read_man = pickle.load(man_read)
    print(read_man)
