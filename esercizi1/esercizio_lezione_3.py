def sum_csv(argomento1):
    somma = 0
    
    for item in argomento1:
        somma = somma + item
    return somma

vendite = []
my_file = open('shampoo_sales.csv', 'r')

for line in my_file:
    elements = line.split(',')
    if elements[0] != 'Date':
        date = elements[0]
        value = float(elements[1])
        vendite.append(value)

valori_vendite = sum_csv(vendite)
print('La somma delle vendite è: {}'.format(valori_vendite))