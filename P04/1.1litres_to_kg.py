litres = float(input('How many litres?'))
density = float(input('Density?'))

def calc_weight(litres, density):
    weight = litres*density
    return(weight)

print('Weight = ' + str(calc_weight(litres, density)) + 'kg')