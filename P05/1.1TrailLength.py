import math

# Ein Trail im Viereck der Grösse 1 -> Distanz sollte insgesamt 4 sein
trail = [(1,1), (2,1), (2,2), (1,2), (1,1)]

def path_length(trail):
    segments = []

    # Erstelle x, y der Punkte i und i+1; das letzte Element wird nicht in den for-Loop genommen -> len(trail-1)
    for i in range(0, len(trail)-1):
        x1 = trail[i][0]
        y1 = trail[i][1]
        x2 = trail[i+1][0]
        y2 = trail[i+1][1]

        # Berechne die Distanz zwischen den zwei Punkten i und i+1 und speichere es in einer Liste
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

        segments.append(dist)

    # Gib die Summe der Werte in der Liste zurück
    return(sum(segments))
        


print(path_length(trail))