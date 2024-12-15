def file_to_list(filename):
    f = open(filename)
    line = f.readline()
    header = line.split(',')
    data = []
    line = f.readline()
    while line:
        row = line.split(',')
        d = {}
        for i in range(len(header)):
            d[header[i]] = row[i]
        data.append(d)
        line = f.readline()
    f.close()
    return data