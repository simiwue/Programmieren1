
#Version 1: print every single domino

# for i in range(0,7):
#     for n in range(i,7):
#         print("(" + str(i) + "|" + str(n) + ")")





#Version 2: add domino to a list and print the list and the number of items

dominos = []

for i in range(0,7):
    for n in range(i,7):
        dominos.append("(" + str(i) + "|" + str(n) + ")")

print(dominos, len(dominos))