aircraft = 900
mass_max = 1280

pilot = int(input('Weight of the PILOT?'))
passenger = int(input('Weight of the PASSENGER?'))
baggage = int(input('Weight of the BAGGAGE?'))
fuel = int(input('Weight of the FUEL?'))

mass_total = aircraft + pilot + passenger + baggage + fuel

capacity = mass_max - mass_total


if capacity >= 0:
    print('You are ready for lift off. \nYour weight is ' + str(capacity) + 'kg under maximal capacity. \nEnjoy your flight!')


elif capacity < 0:
    print('Starting could be dangerous! \nYou total weight is ' + str(-capacity) + 'kg over the recommended threshold.')

else:
    print("The Weight could not be calculated. \nSorry I'm not sure if lift off is save.")