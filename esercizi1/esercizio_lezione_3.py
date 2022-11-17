def sum_csv(file_name):
    somma = 0
    file_name = open(file_name, 'r')
    for line in file_name:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = float(elements[1])
            somma = somma + value
        return somma

