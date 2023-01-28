def write_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5])))
        return columns, data

def write_to_file(filename, data, columns):
    with open(filename, 'w') as file:
        file.write(','.join(columns)+'\n')
        for line in data:
            line=[str(1) for i in line]
            file.write(','.join(line)+'\n')
            