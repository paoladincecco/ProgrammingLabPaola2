#scrivere una funzione sum_list che sommi tutti gli elementi di una lista

def sum_list(argomento_1):
    somma = 0
    if not argomento_1:
        return None 
    else:
        for item in argomento_1:
            somma = somma + item
    return somma

number_list = [1, 5, 7, 12, 14, 9]
somma = sum_list(number_list)
print(somma)

