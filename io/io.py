filename = 'sketch.txt'
try:
    data = open(filename)

    for each_line in data:
        try:
            (role, spoken) = each_line.split(':', 1)
            print(role + " said :" + spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print("The data file <" + filename + "> does not exists!")
