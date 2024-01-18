


def berg_hoehe(berge):
    highest = 0
    for i in range(1, len(berge), 2):
        height = berge[i]
        if height > highest:
            highest = height
            berg = berge[i-1]

    return((berg, highest))

bergliste = ["Dom", 4545, "Saentis", 2502, "Dufourspitze", 4634,
"Matterhorn", 4478]
berg_und_hoehe = berg_hoehe(bergliste)

print(berg_und_hoehe)
