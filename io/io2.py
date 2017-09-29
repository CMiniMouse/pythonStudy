import nester

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
    man_file = open("man.txt", 'w')
    other_file = open("other.txt", 'w')

    nester.print_lol(man, fh = man_file)
    nester.print_lol(other, fh = other_file)
except IOError:
    print("File Error")

finally:
    man_file.close()
    other_file.close()
