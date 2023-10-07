# ==== einfache Version ====

# stars = ["*", "* *", "* * *", "* *", "*"]
# for s in stars:
#     print(s*str("* "))

# ===== erweiterte Version - Anzahl Sterne kann gewählt werden ======

stars = "*"
max_stars = int(input("How many stars do you want? \n Enter an integer > 0")) - 1

while len(stars) < (max_stars*2):
    print(stars)
    stars = stars + " *"


else:
    while len(stars) > 0:
        print(stars)
        stars = stars[:-2]

