import json
# Importiere alle Daten aus dem separaten json-file
plane_data = open('P07/planeData.json')
plane_spec = json.load(plane_data)

aircraft = 900
mass_max = 1280

# Frage den user nach den Gewichten
pilot = int(input('Weight of the PILOT?'))
passenger = int(input('Weight of the PASSENGER?'))
baggage = int(input('Weight of the BAGGAGE?'))
fuel = int(input('Weight of the FUEL?'))

# berechne die Masse
mass_total = aircraft + pilot + passenger + baggage + fuel

# Vergleich masse mit der maximalen Masse
capacity = mass_max - mass_total

# Berechne das Momentum mit Hilfe der Angaben aus dem separaten json-file
total_moment = plane_spec["Empty_Moment"] + pilot * plane_spec["Front_seats"] + passenger * plane_spec["Rear_seats"] + baggage * plane_spec["Baggage_tube"] + fuel * plane_spec["Usable_fuel"]

# Berechne center of gravity
cg = total_moment / mass_total

# vergleiche cg mit dem zugelassenen Wert 2.4 - 2.53
if cg > 2.4 and cg < 2.53:

    # Checke ob das Gewicht zu hoch ist und gib eine entwprechende Anweisung
    if capacity >= 0:
        print('You are ready for lift off. \nYour weight is ' + str(capacity) + 'kg under maximal capacity and center of gravity is ' + str(round(cg, 2)) + 'm\nEnjoy your flight!')


    elif capacity < 0:
        print('Starting could be dangerous! \nYou total weight is ' + str(-capacity) + 'kg over the recommended threshold.')

    else:
        print("The Weight could not be calculated. \nSorry I'm not sure if lift off is save.")

# Wenn cg am falschen Ort ist, tritt dies Warnung auf
else:
    print('Starting could be dangerous! The center of gravity is out of bounds.')